# DDFF-Improved-Cross-Platform
DDFF - Duplicate Directories and Files Finder. Written in Python 3.x, it works with Python 2.x as well. It finds both duplicate files and directories. It is also compatible with Windows, Linux, and Mac.It is cross-platform.



clone the repo

cd to repo

// sort all files from largest size to smallest
python3 sort-all-files-largest-to-smallest.py /

sort-all-files-largest-to-smallest.py creates two new files:
1. all-files-sorted.txt
2. sort-files.db

The file all-files-sorted.txt contains list of all files sorted and grouped by same file size. eg.
```bash
* file size=62.5Kb
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/c/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/linux_ddff-2.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/c/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/linux_ddff-2.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/linux_ddff-3.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/linux_ddff.txt
```


// delete too much large files (size greater than 4GB) or move them to a separate direcotry or external pen-drive/hard-disk then remove that hard-disk or pen-drive. The reason is, sometimes this script seems to be stuck when reading too much large files.

python3 ddff.py /

Note: we can close the program execution by pressing the ctrl+c and can resume the program execution again. When a user interruppts the program exection then script saves the required results into db and resumes in the next run.

ddff.py creates two new files:
1. ddff.txt
2. ddff.db

ddff.txt contains a list of all duplicate files and folders (sorted by size)

eg.
```bash
* dir size=187.4Kb
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p

* file size=62.5Kb
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/c/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/linux_ddff-2.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/c/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/linux_ddff-2.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/linux_ddff.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/linux_ddff-3.txt
/home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/linux_ddff.txt
```
// keep only one copy of duplicated folder/files and delete others using the following python script.
python3 remove-duplicates.py

```bash
eg. pavan@u-20:~/.../DDFF-Improved-Cross-Platform$ python3 remove-duplicates.py
LINE_SEPERATOR 

* dir size=187.4Kb
1 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b
2 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p
keep index: 


* file size=62.5Kb
1 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/c/linux_ddff.txt
2 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/linux_ddff-2.txt
3 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/b/linux_ddff.txt
4 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/c/linux_ddff.txt
5 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/linux_ddff-2.txt
6 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/p/linux_ddff.txt
7 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/linux_ddff-3.txt
8 /home/pavan/Documents/aux/tmp-git/DDFF-Improved-Cross-Platform/test1/linux_ddff.txt
keep index: 


pavan@u-20:~/.../DDFF-Improved-Cross-Platform$
```

type the index of file or line number which you wants to keep, other duplicate directory/file will be removed. If you don't want to delete any folder or file then just type enter instead of providing a input.

