from __future__ import print_function
import threefry
import numpy as np

Random123_deadbeef_badcafe = \
"""dc1e842f4112bf11 46a388d784b2f52d
60a646481acb081a dd49fc6023718fc2
eee8a29306f467ca 1b88e50b14435b8b
b544060c8cb1a658 29ec365ecdab0402
44495a5bab8b1677 392368c679c80bff
319a58f11e1dc63c c611918ed445030f
673ae0682f10b0e5 196dde621618b964
a8f221275729a06f 37604d5a2cc6adf3
7e92af6203517c5b 12d8424b33b99ed1
7b4caa0c35ef583c dc06c31a464a68
"""

r = threefry.rng(0xdeadbeef, 0xbadcafe)

def hex_no_0x(i):
    """
    Return the equivalent of the C PRIx64 format macro. The removal of the extra L is to
    ensure Python 2/3 compatibility.
    """
    tmp = str(hex(i)[2:])
    if tmp[-1] == 'L':
        tmp = tmp[:-1]
    return tmp

def test_reference():
    s = ''
    for i in range(10):
        x0, x1 = r.random_uint64_pair()
        s += "%s %s\n" % (hex_no_0x(x0), hex_no_0x(x1))

    print("Actually doing something")
    print(s)

    assert s == Random123_deadbeef_badcafe

