import struct

'''
Utility functions for reading from the file.
# (From io_scene_abc)

fmt reference:
https://docs.python.org/3/library/struct.html#format-characters

'''
def unpack(fmt, f):
    return struct.unpack(fmt, f.read(struct.calcsize(fmt)))


def pack(fmt, f, values):
    f.write(struct.pack(fmt, values))
