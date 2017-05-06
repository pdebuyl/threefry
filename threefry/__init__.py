from .threefry import rng
from .version import __version__ as __version__

def get_include():
    import threefry
    import os.path
    return os.path.dirname(threefry.__file__)
