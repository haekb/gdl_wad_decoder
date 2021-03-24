#
# WAD DECODER
# Decodes WAD.BIN from the ps2 version of Gauntlet Dark Legacy
# Works off a name list check name_list.py
#

import zlib

import os
from pathlib import Path
from name_list import name_list
from gdl_hash import hash_me
from io_utils import unpack

hash_table = {}

# Globals
file_count = -1
file_list = []

def read_table_of_contents(f):
    file_count = unpack('I', f)[0]

    for _i in range(file_count):
        file_list.append({
            'uncompressed_file_size': unpack('i', f)[0],
            'file_pointer': unpack('i', f)[0],
            'hash': unpack('I', f)[0],
            'compressed_file_size': unpack('i', f)[0],
        })
    # End For
# End Def


def main():
    print("WAD Decoder by @HeyThereCoffeee")
    print("For Gauntlet Dark Legacy (PS2)")
    print("Building hash table...")

    for name in name_list:
        file = name.replace('/', '\\')
        file = file.upper()
        file = hash_me(file)
        hash_table[file] = { 'name': name, 'used': False }
    # End For

    print("Hash table built!")
    print("Extracting WAD.BIN - This may take a minute!")

    root_out = './out/'

    # Create our root output directory
    path = Path(root_out)
    path.mkdir(parents=True, exist_ok=True)

    f_wad = open('./WAD.BIN', 'rb')

    read_table_of_contents(f_wad)

    unknown_file_count = 0

    # Get extractin'!
    for file_entry in file_list:
        out = 'unknown/unk.%d' % unknown_file_count

        # Find out file name via the hash
        if file_entry['hash'] in hash_table:
            out = hash_table[file_entry['hash']]['name']
            hash_table[file_entry['hash']]['used'] = True
        else:
            unknown_file_count += 1
        # End If

        # Create our path
        out_path = Path(os.path.dirname("%s/%s" % (root_out, out)))
        out_path.mkdir(parents=True, exist_ok=True)

        # Go to our file
        f_wad.seek(file_entry['file_pointer'], 0)

        buffer = ''

        # It's not compressed!
        if file_entry['compressed_file_size'] == -1:
            buffer = f_wad.read(file_entry['uncompressed_file_size'])
        else:
            buffer = f_wad.read(file_entry['compressed_file_size'])
            buffer = zlib.decompress(buffer)
        # End If

        # Write it all out at once!
        f_file = open("%s/%s" % (root_out, out), 'wb')
        f_file.write(buffer)
        f_file.close()


    # End For

    f_wad.close()

    print("Finished extracting files!")

    print("Writing out any non-used hashes to not_used.txt")

    f_not_used = open("./not_used.txt", 'w')
    for hash_num in hash_table:
        hash_entry = hash_table[hash_num]
        if hash_entry['used'] == False:
            f_not_used.write("%s\n" % hash_entry['name'])
        # End If
    # End For

    f_not_used.close()

    print("All done!")

    
# End Def

main()