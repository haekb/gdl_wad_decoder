#
# It sure is ugly, but most of it is from decompilation
# It heavily relies on integer overflows, and most of the _c32() calls were placed via a script
# It works, so don't touch it!!! (And also don't read it, because it sure is ugly...)
#
from ctypes import c_int, c_uint

def _c32(val):
    return c_uint(val).value
# End Def

# Straight from Ghidra
def mix(param_1, param_2, param_3):
    uVar1 = 0
    uVar2 = 0
    uVar2 = _c32(param_1)
    uVar1 = _c32(param_2)
    param_1 = _c32(uVar2) - _c32(uVar1)
    uVar2 = _c32((uVar2 - uVar1) - _c32(param_3))
    param_1 = _c32(uVar2)
    param_1 = _c32(_c32(param_3) >> 0xd ^ _c32(uVar2))
    uVar2 = _c32(param_2)
    uVar1 = _c32(param_3)
    param_2 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_1))
    param_2 = _c32(uVar2)
    param_2 = _c32(_c32(param_1) << 8 ^ _c32(uVar2))
    uVar2 = _c32(param_3)
    uVar1 = _c32(param_1)
    param_3 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_2))
    param_3 = _c32(uVar2)
    param_3 = _c32(_c32(param_2) >> 0xd ^ _c32(uVar2))
    uVar2 = _c32(param_1)
    uVar1 = _c32(param_2)
    param_1 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_3))
    param_1 = _c32(uVar2)
    param_1 = _c32(_c32(param_3) >> 0xc ^ _c32(uVar2))
    uVar2 = _c32(param_2)
    uVar1 = _c32(param_3)
    param_2 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_1))
    param_2 = _c32(uVar2)
    param_2 = _c32(_c32(param_1) << 0x10 ^ _c32(uVar2))
    uVar2 = _c32(param_3)
    uVar1 = _c32(param_1)
    param_3 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_2))
    param_3 = _c32(uVar2)
    param_3 = _c32(_c32(param_2) >> 5 ^ _c32(uVar2))
    uVar2 = _c32(param_1)
    uVar1 = _c32(param_2)
    param_1 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_3))
    param_1 = _c32(uVar2)
    param_1 = _c32(_c32(param_3) >> 3 ^ _c32(uVar2))
    uVar2 = _c32(param_2)
    uVar1 = _c32(param_3)
    param_2 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_1))
    param_2 = _c32(uVar2)
    param_2 = _c32(_c32(param_1) << 10 ^ _c32(uVar2))
    uVar2 = _c32(param_3)
    uVar1 = _c32(param_1)
    param_3 = _c32(_c32(uVar2) - _c32(uVar1))
    uVar2 = _c32((_c32(uVar2) - _c32(uVar1)) - _c32(param_2))
    param_3 = _c32(uVar2)
    param_3 = _c32(_c32(param_2) >> 0xf ^ _c32(uVar2))

    return (param_1, param_2, param_3)
# End Def

def hash_me(dir_str):
    _iVar1 = len(dir_str)
    iVar1 = _iVar1
    local_5c = _c32(-0x61c88647)
    local_60 = _c32(-0x61c88647)
    local_58 = [ 0xd, 0x0 ]

    iVar2 = iVar1
    dir_string_process = dir_str
    while 0xb < _iVar1:
        local_60 = _c32(local_60) + ord(dir_string_process[0]) + ord(dir_string_process[1]) * 0x100 + ord(dir_string_process[2]) * 0x10000 + ord(dir_string_process[3]) * 0x1000000
        local_5c = _c32(local_5c) + ord(dir_string_process[4]) + ord(dir_string_process[5]) * 0x100 + ord(dir_string_process[6]) * 0x10000 + ord(dir_string_process[7]) * 0x1000000
        local_58[0] = _c32(local_58[0]) + ord(dir_string_process[8]) + ord(dir_string_process[9]) * 0x100 + ord(dir_string_process[10]) * 0x10000 + ord(dir_string_process[0xb]) * 0x1000000
        (local_60, local_5c, local_58[0]) = mix(local_60, local_5c, local_58[0])
        iVar2 = _iVar1 + -0xc
        _iVar1 = iVar2
        dir_string_process = dir_string_process[0xc:]
    # End While

    local_58[0] = _c32(iVar1) + _c32(local_58[0])

    # Mimic switch case fall through....
    fall_through = False

    if iVar2 == 0xb:
        local_58[0] = ord(dir_string_process[10]) * 0x1000000 + _c32(local_58[0])
        fall_through = True
    if iVar2 == 10 or fall_through:
        local_58[0] = ord(dir_string_process[9]) * 0x10000 + _c32(local_58[0])
        fall_through = True
    if iVar2 == 9 or fall_through:
        local_58[0] = ord(dir_string_process[8]) * 0x100 + _c32(local_58[0])
        fall_through = True
    if iVar2 == 8 or fall_through:
        local_5c = ord(dir_string_process[7]) * 0x1000000 + _c32(local_5c)
        fall_through = True
    if iVar2 == 7 or fall_through:
        local_5c = ord(dir_string_process[6]) * 0x10000 + _c32(local_5c)
        fall_through = True
    if iVar2 == 6 or fall_through:
        local_5c = ord(dir_string_process[5]) * 0x100 + _c32(local_5c)
        fall_through = True
    if iVar2 == 5 or fall_through:
        local_5c = ord(dir_string_process[4]) + _c32(local_5c)
        fall_through = True
    if iVar2 == 4 or fall_through:
        local_60 = ord(dir_string_process[3]) * 0x1000000 + _c32(local_60)
        fall_through = True
    if iVar2 == 3 or fall_through:
        local_60 = ord(dir_string_process[2]) * 0x10000 + _c32(local_60)
        fall_through = True
    if iVar2 == 2 or fall_through:
        local_60 = ord(dir_string_process[1]) * 0x100 + _c32(local_60)
        fall_through = True
    if iVar2 == 1 or fall_through:
        local_60 = ord(dir_string_process[0]) + _c32(local_60)
        fall_through = True
    
    (local_60, local_5c, local_58[0]) = mix(local_60, local_5c, local_58[0])
    return local_58[0]
    # End If
# End Def
