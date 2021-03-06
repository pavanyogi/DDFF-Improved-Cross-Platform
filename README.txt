# DDFF - Duplicate Directories and Files Finder

... by dennis(a)yurichev.com

Written in Python 3.x.

So far, only for Linux, sorry.

Finds both duplicate files and directories.

## For users

Just run it:

	./ddff.py ~

Or:

	python ddff.py ~

Multiple directories allowed:

	./ddff.py ~/Music /mnt/external_HDD/Music

Here is an example: the script processed Linux kernel source trees for versions 
2.6.11.10, 2.6.26, 2.6.31, 3.10.43, 3.18.37, 3.2.1, 4.11, 4.1.22.

```
* dir size=5.9MB
/home/dennis/tmp/1/linux-4.1.22/firmware
/home/dennis/tmp/1/linux-3.18.37/firmware
* dir size=3.5MB
/home/dennis/tmp/1/linux-4.1.22/fs/nls
/home/dennis/tmp/1/linux-4.11/fs/nls
/home/dennis/tmp/1/linux-3.18.37/fs/nls
* dir size=2.3MB
/home/dennis/tmp/1/linux-4.1.22/arch/m68k/ifpsp060
/home/dennis/tmp/1/linux-3.10.43/arch/m68k/ifpsp060
/home/dennis/tmp/1/linux-3.2.1/arch/m68k/ifpsp060
/home/dennis/tmp/1/linux-3.18.37/arch/m68k/ifpsp060
* dir size=1.8MB
/home/dennis/tmp/1/linux-2.6.26/arch/m68k/ifpsp060/src
/home/dennis/tmp/1/linux-2.6.31/arch/m68k/ifpsp060/src
* dir size=1.7MB
/home/dennis/tmp/1/linux-4.1.22/firmware/bnx2x
/home/dennis/tmp/1/linux-3.10.43/firmware/bnx2x
/home/dennis/tmp/1/linux-3.2.1/firmware/bnx2x
/home/dennis/tmp/1/linux-4.11/firmware/bnx2x
/home/dennis/tmp/1/linux-3.18.37/firmware/bnx2x
* dir size=1.1MB
/home/dennis/tmp/1/linux-4.1.22/arch/cris/include/arch-v32/arch/hwregs
/home/dennis/tmp/1/linux-3.10.43/arch/cris/include/arch-v32/arch/hwregs
/home/dennis/tmp/1/linux-4.11/arch/cris/include/arch-v32/arch/hwregs
/home/dennis/tmp/1/linux-3.18.37/arch/cris/include/arch-v32/arch/hwregs
* file size=1.1MB
/home/dennis/tmp/1/linux-4.1.22/crypto/testmgr.h
/home/dennis/tmp/1/linux-3.18.37/crypto/testmgr.h
* file size=1.0MB
/home/dennis/tmp/1/linux-4.1.22/drivers/media/dvb-frontends/drx39xyj/drxj_map.h
/home/dennis/tmp/1/linux-4.11/drivers/media/dvb-frontends/drx39xyj/drxj_map.h
/home/dennis/tmp/1/linux-3.18.37/drivers/media/dvb-frontends/drx39xyj/drxj_map.h

...

```
( linux_ddff.txt )

Now you can see what hasn't been modified across several Linux kernel versions (larger than 100KB).

By default, only files/directories larger than 1MB are dumped.
Modify the LIMIT variable in ddff.py to change this.

## Internals, etc

Files are not compared as a wholes, rather 5 4Kb consequtive spots are taken from it and then hashed using SHA256.
Hashes are then compared.
Surely, file/directory names are not compared.
If entropy of these 5 spots are suspiciosly low (less than 7 bits per byte), the whole file is hashed.
Read more about entropy in my ["Reverse Engineering for Beginners"](https://beginners.re/) book.
If you feel paranoid, turn on "PARANOID" option in the ddff.py file, and full hashes will be calculated for each file (this is just slow, especially for videos).

Rationale: for compressed files, only these 5 4KB spots are seems to be enough, maybe even less.
However, a patched byte(s) in low-entropy text/executable file can be located between spots and 
files would be treated as similar, erroneously.

Directories are compared using Merkle trees,
read [here](compare_two_folders.md) about my short example, what this is.
Merkle trees are also used in torrents and blockchains.
I.e., SHA256 hash is also calculated for all directories.

File hashes are then stored (serialized) into ddff.db file
(Python's [pickle library](https://docs.python.org/3/library/pickle.html) is used).
This is a text file, you can see there filename, SHA256 hash, file size, modify time for each file,
 and which hash (full/partial) is stored.
Preserve it, so DDFF will not need to reread a file again.
However, if you reorganize your file structure significantly, you can kill it.

The interface of the script is somewhat user-unfriendly.
I did the script just for myself.
If someone wants to do more, like GUI, win32 version, etc, take it and modify it freely.
Or write new, using these algorithms.

