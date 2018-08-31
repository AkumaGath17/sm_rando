from intervals import *
from compress import *
from decompress import *
from util import *

src = b"\x01\x01\x01\x01"
bf = find_bytefills(src)
assert len(bf) == 1

src = b"\x01" * 34
bf = find_bytefills(src)
assert bf[0].rep == 3

src = b"\x01" * 32
bf = find_bytefills(src)
assert bf[0].rep == 2

src = b"\x01\x02\x03\x04\x01\x02\x03\x04"
sf = find_sigmafills(src)
assert len(sf) == 2

"""
src = b"\x02\x03\x02\x03\x02\x03"
wf = find_wordfills(src)
assert len(wf) == 1
src = b"\x01\x02\x02\x02\x02\x03" * 2
assert len(compress(src)) == 9
src = b"\x02\x02\x02\x05\x01\x02\x03\x04"
assert len(compress(src)) == 7
# test overlaps
src = b"\x01\x01\x01\x01\x02\x03\x04\x05"
out = compress(src)
#f = open("dst.bin", "wb")
#f.write(out)
#f.close()
src = b"\x01\x02\x01\x04"*2
assert len(compress(src)) == 8
"""

src = random_r_bytes(256, 4)
c = compress(src)
print("Compression ratio: ", str(len(c) / len(src)))
dc = decompress(c)
d = differs(src, dc)
assert len(d) == 0, str(d)

