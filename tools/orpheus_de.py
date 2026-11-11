"""Kartoffel-Orpheus German TTS (llama.cpp GGUF + SNAC). synth(text, voice) -> (np.float32, 24000)"""
import os, numpy as np, torch
os.environ.setdefault("TQDM_DISABLE", "1")
GGUF = "/home/claude/tts/orpheus/kartoffel-q5.gguf"
_m = {}
def _load():
    if "llm" not in _m:
        from llama_cpp import Llama
        from snac import SNAC
        _m["llm"] = Llama(model_path=GGUF, n_ctx=4096, n_threads=2, verbose=False)
        _m["snac"] = SNAC.from_pretrained("hubertsiuzdak/snac_24khz").eval()
    return _m["llm"], _m["snac"]
def _codes(text, voice, temp=0.6, top_p=0.95, rep=1.1, max_new=2400):
    llm, _ = _load()
    ids = llm.tokenize(f"{voice}: {text}".encode(), add_bos=True, special=False)
    prompt = [128259] + ids + [128009, 128260]
    out = []
    llm.reset()
    for tok in llm.generate(prompt, temp=temp, top_p=top_p, repeat_penalty=rep, reset=True):
        if tok == 128258 or len(out) >= max_new: break
        out.append(tok)
    if 128257 in out: out = out[len(out) - out[::-1].index(128257):]
    out = [t for t in out if t != 128258]
    out = out[: (len(out) // 7) * 7]
    return [t - 128266 for t in out]
def synth(text, voice="Jakob", speed=1.0):
    _, snac = _load()
    c = _codes(text, voice)
    l1, l2, l3 = [], [], []
    for i in range(len(c) // 7):
        l1.append(c[7*i]); l2.append(c[7*i+1] - 4096); l3 += [c[7*i+2] - 2*4096, c[7*i+3] - 3*4096]
        l2.append(c[7*i+4] - 4*4096); l3 += [c[7*i+5] - 5*4096, c[7*i+6] - 6*4096]
    ok = all(0 <= x < 4096 for x in l1 + l2 + l3)
    if not ok or not l1: raise RuntimeError("bad codes")
    with torch.no_grad():
        a = snac.decode([torch.tensor(l).unsqueeze(0) for l in (l1, l2, l3)]).squeeze().numpy().astype(np.float32)
    return a, 24000
if __name__ == "__main__":
    import sys, time, soundfile as sf
    t0 = time.time(); a, sr = synth(sys.argv[1], sys.argv[3] if len(sys.argv) > 3 else "Jakob")
    sf.write(sys.argv[2], a, sr); print(round(len(a)/sr, 2), "s audio in", round(time.time()-t0), "s")
