from .threefry import rng

def get_include():
    import threefry
    import os.path
    return os.path.dirname(threefry.__file__)
