"""German Kokoro (Thorsten-Voice fine-tune) without the kokoro package __init__ (avoids spacy/misaki deps).
G2P via piper's espeak-ng (German IPA)."""
import sys, types, os, importlib.util, json, numpy as np, torch
import site
kdir = None
for p in sys.path:
    if os.path.isdir(os.path.join(p, "kokoro")) and os.path.exists(os.path.join(p, "kokoro", "model.py")): kdir = os.path.join(p, "kokoro"); break
if kdir is None:
    kdir = "/home/claude/tvenv/lib/python3.13/site-packages/kokoro"
pkg = types.ModuleType("kokoro"); pkg.__path__ = [kdir]; sys.modules["kokoro"] = pkg
from kokoro.model import KModel
D = "/home/claude/tts/tvkokoro"
_m = {}
def load():
    if "m" not in _m:
        _m["m"] = KModel(config=D + "/config.json", model=D + "/model.pth").eval()
        _m["v"] = torch.load(D + "/voices/thorsten.pt", map_location="cpu", weights_only=True)
        _m["vocab"] = json.load(open(D + "/config.json"))["vocab"]
    return _m
def phonemize(text):
    from piper.phonemize_espeak import EspeakPhonemizer
    if "ph" not in _m: _m["ph"] = EspeakPhonemizer()
    sents = _m["ph"].phonemize("de", text)
    return [("".join(s)).replace("ʏ", "y") for s in sents]
def synth(text, speed=1.0):
    m = load(); out = []
    for ps in phonemize(text):
        ps = "".join(c for c in ps if c in m["vocab"])[:510]
        if not ps.strip(): continue
        ref = m["v"][len(ps) - 1]
        with torch.no_grad():
            a = m["m"](ps, ref, speed)
        out.append(a.numpy() if hasattr(a, "numpy") else np.asarray(a))
        out.append(np.zeros(int(0.12 * 24000), np.float32))
    return np.concatenate(out).astype(np.float32), 24000
if __name__ == "__main__":
    import soundfile as sf
    a, sr = synth(sys.argv[1], float(sys.argv[3]) if len(sys.argv) > 3 else 1.0); sf.write(sys.argv[2], a, sr); print(len(a) / sr)
