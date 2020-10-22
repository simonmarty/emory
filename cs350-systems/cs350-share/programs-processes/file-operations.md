# File Operations

## File Descriptors

* Path
* open and creat give a file descriptor (small integer, cookie behavior)

File descriptor contains
* Inode
* Flag
* Offset

`operations(fd)` = 
* read
* write

U block contains a file descriptor table

--------------------------

```
int creat(char* path, int mode)
```

Example: `creat("abc", 0)`
* Returns -1 if fails
  * You can `perror(<something>)` if you want
  * Could fail because no perms
  * Could fail because there is a file with that name

```
int open(char* path, int flag)
```
* Open an existing file
* Returns the file description corresponding
* `flag`
  * 0 : read RD
  * 1 : write WR
  * 2 : read & write RD+WR

```
int open(char* path, int flag, int mode)
```
* `flag`
  * 0_RDONLY
  * 0_WRONLY
  * 0_RDWR
  * 0_CREAT
  * 0_TRUNC
  * 0_NONBLOCK
  * **...**
* OS compares flag passed to the flag of the corresponding file descriptor and determines if the operation requested is doable.
* `creat(...)` &#x2194; O_WRONLY | O_CREAT | O_TRUNC

```
read(int fd, char* buffer, int count)
write(int fd, char* buffer, int count)
```

`read()`/`write()` count bytes from/to the file with the `fd` (respectively), using the buffer pointed to by `buff` (address in memory).

The return value is the number of bytes transferred.

* `-1` indicates an error (check `errno`)
* `0` on read is EOF


### Example
* process contains an instruction: `write(5, 1000, 20)` (actually a trap instruction in Text block of process with parameters (`5, 1000, 20`) on the process stack)
* Move to T block of OS (syscall handler)
* Buffer pointer in stack points to the OS memory
  * Has to ultimately go to the `offset` inode
* Copy bytes at address `1000` for `20` bytes
* return `20`
* Offset is incremented by the amount transferred

* `buffer` has to be predeclared
* `char buff[50]` or `malloc` required space

`time ./copy /boot/initrd.img-*`
* real time is large
* Waits for the HDD controller to say it's finished

Context switching is expensive
* Single byte IO is not reasonable

# More File API stuff

So far...
* File Descriptors
  |   I   |   F   |   O   |
  | :---: | :---: | :---: |
* System calls
  * `open`/`creat` -> fd
  * `read`/`write`/`lseek`

## `lseek(int fd, long pos, int where)`
* `where`
  * *SEEK_SET*
  * *SEEK_CUR* - interpret `pos` relative to current position.
  * *SEEK_END* - relative to the end of the file

### Metadata
* *mode* from `create(char* path, int mode)
* *mode* is more than permission

*mode*
* 16-bit quantity
* 9 of the bits are in fact permissions

| 15  | 14  | 13            | 12       | 11   | 10   | 9          | 9 bits |     |     |
| --- | --- | ------------- | -------- | ---- | ---- | ---------- | ------ | --- | --- |
| ord | dir | char dev file | FIFO bit | SUID | SGID | Sticky bit | rwx    | rwx | rwx |

Ex: 1010 is a block special

### Bit 11 : SUID bit

real UID <- login UID
effective UID <- Used for checking permissions

Both in the U block

### Bit 10 : SGID bit

Analogous, for group

### Bit 9 : Sticky bit

Save the image of exec in RAM, as long as there's room.

```
man 2 stat
man inode
man 2 stat
```

## test

Macros

* S_ISREG(m)
* S_ISDIR(m)
* S_ISCHR(m)

User permission change

* chmod
* chown
* chgrp
* utime - change atime, utime
  * Also ends up changing the ctime for the inode

# File Names

* Not in the inode

## Directories
* Itself a file type
* A series of directory entries

| Name | Inode # |
|-----|----|

Where node number points to a list of entries

* Internal structure is not portable

## Directory API



```
struct dirent {
    ino_t   dino;
    char* d_name;
} DIR;
```
At least these two, `ino_t` is essentially an `int`

```
DIR* opendir(char* path) {}
struct dirent readdir(DIR* dirp)