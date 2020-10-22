# Homework 2

`myar.c`

```
ar {key} {archive} {file1} {file2}
ar q arch abc
ar t arch
ar tv arch
ar x arch xyz
ar xo arch xyz
ar d arch xyz
ar A arch   # Added


```

arch - compatible with system version


## AR archive

|AR Archive|
|:---:|
| ARMAG |
| AR HDR 1 |
| file1 |
| AR HDR 2 |
| file2 |

By default, modern Linux distros don't include metadata when ar-ing. Use `U` to add metadata

Padding has to be added for some architectures that can't reference a pointer at an odd address

```
!<arch> # magic string
one/    1571329221  8620    70  100644  4   `
ONE
```

`` `\n`` is `ar_fmag`

No null characters in the ar_hdr members.

Write of the ar_hdr in ONE system call

## More info for hw2

### stat structure
* `mode_t` int that stores file type and mode
* `off_t` `st_size` is the size of
* `blksize_t` st_blksize tells you how big to make the buffer
* S_ISREG(m) etc give you info on common macros, modes, permission
* Read/write/seek
  * System calls
  * Context switch
  * Do enough work during each r/w operation
  * Small read/writes are not slowed down by excessive disk IO
    * Buffer cache
  * Only slowed down by the context switches
  * For many programs the algorithm is not compatible with large read/writes
  * Need a way to
    * Efficient (large IO)
    * convenient
* Solution: write/ use a library
  * Buffered IO library

Conventions
* System Calls
  * Standard input: fd 0
  * Standard output: fd 1
  * Standard error: fd 2
* Buffered I/O
  * stdin
  * stdout
  * stderr
  * All `FILE`s where fd = Standard vals

```
a.out > x < y
```
fd 1 = x
fd 2 = y