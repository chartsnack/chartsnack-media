import sys, types, importlib.abc, importlib.machinery
class _Dummy:
    def __init__(self, *a, **k): pass
    def __call__(self, *a, **k): return _Dummy()
    def __getattr__(self, n): return _Dummy()
class _Mod(types.ModuleType):
    def __getattr__(self, n):
        if n.startswith("__"): raise AttributeError(n)
        return _Dummy
class _Finder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, name, path, target=None):
        if name == "deepspeed" or name.startswith("deepspeed."):
            return importlib.machinery.ModuleSpec(name, self, is_package=True)
    def create_module(self, spec): m = _Mod(spec.name); m.__path__ = []; return m
    def exec_module(self, m): pass
sys.meta_path.insert(0, _Finder())
