# WAD Decoder

Decodes Gauntlet Dark Legacy PS2 `WAD.BIN` file. 

## Usage
Place your `WAD.BIN` file into the same directory as the scripts, and run `wad_decoder.py`. Afterwords you should see a `out/` folder. You will also see a `not_used.txt`, which just contains a list of files from `name_list.py` that didn't match with any of the hashes in the `WAD.BIN`. (This is normal.)

## Structure
`WAD.BIN` is a very simple archive file. The first four bytes are the number of files. Following that is a list of files (* number of files.)
The file entries are structured like:
```
struct FileEntry {
    int UncompressedFileSize;
    int FilePointer;
    uint Hash;
    int CompressedFileSize;
};
```

If `CompressedFileSize` is `-1` then the file is not compressed. Otherwise it uses zlib compression. The file paths are hashed via the hashing function in `gdl_hash.py`.

## Name List
I use a giant list of paths in `name_list.py` generated via a script (based off the xbox version, which only has loose files), and then hand-tweaked. The remaining unknown files are dumped into `out/unknown/` as `unk.#`. There seems to be some type of `WAD` (not related to `WAD.BIN`) type data per textures.ps2, and some left-over script outputs.

## Credits
Some helper functions are from [io_scene_abc](https://github.com/cmbasnett/io_scene_abc), at least for the time being!
Research and development by [Haekb (HeyThereCoffeee)](https://github.com/haekb)