# File Systems

Relevant Chapters: Ch1-1-29, 56-59
Lots of them

* FAT
* NTFS
* HFS
* HSFS
* Ext
* UFS
* MFS

## UFS

* Unix File System
* Developed at Bell Labs
* Research
    - Program Development
    - Documentation
* Many small files
* Some large, sequential ones
* No limit on the internal structure of files
* Ideally, we want the file system to be very efficient with **small files**, and somewhat efficient with **large files**

## File Types

* Ordinary file
    - Sequence of bytes
    - No significance to the OS
    - No EOF byte

| Disk section |            Content             |
| :----------: | :----------------------------: |
|     Boot     |                                |
|    SUPER     |             PARAMS             |
|   <br><br>   | Inodes<br>(physical directory) |
|   <br><br>   |          Data blocks           |
|     <br>     |              <br>              |

## Inode

* Metadata for a file (no name)
    - Owner
    - Group
    - Permissions
    - Timestamps
    - Size
* Blocklist
    - List of data blocks

## Directory

* Sequence of bytes
* Directory entries to inode numbers

| Node # | Name  |
| :----: | :---: |
|  ...   |  ...  |

### Root Director

* Special
* Inode 2

| Block # |                       Contents                        |
| :-----: | :---------------------------------------------------: |
|   101   |      [ home `52` , USR `77` , hb `99` , `...` ]       |
|   121   | [ KM `2001` , VSS `2002` , CS350001 `3000` , `...` ]  |
|   125   | [ share `1234` , priv `2222` , CS350 `2112` , `...` ] |
|   150   |   [ sample.c `2718` , tripleprime `2817` , `...` ]    |
|   155   |              `#include<stdio.h>\n .... `              |

| Inode # | Type  | Blocklist |
| :-----: | :---: | :-------: |
|    2    | `DIR` |    101    |
|   52    | `DIR` |    121    |
|  3000   | `DIR` |    125    |
|  1234   | `DIR` |    150    |
|  2718   | `DIR` |    155    |

The OS figures out sample.c is not a directory **not** by its file extension, but by the *type* field in its INode.

## Optimizing the Unix FIle System

1. Solid Logical Structure
2. Fix the expensive portions
    - Hash
    - Cashe
        - Cash inode#2
        - When you read a directory, cache it
            - Name Cache
            - inode cache

It is convenient to have more than one name of a file

* Shortcuts

### Symbolic links

``` 
# Creates a directory entry for "newfile with the
# same inode # as "oldfile"

ln [oldfile] [newfile]
```

**Problem**: 

``` 
rm [filename]
```

`1234` 
# UFS

* Types
    - Ordinary
    - Directories - structure:

| Name | inode # |
| ---- | ------- |
| ...  | ...     |

* Form a logical tree
* Links allow a file to have multiple paths
* `ln {oldname}{newname}` 
    - Creates a new directory entry

* `rm {anyfile}` 
    1. deletes the directory entry
    2. Deletes the inode
    3. Deletes the blocks associated with the file

### Fix:

`...` 
# Multiple Disks

* Windows: Forest by default
    - Nowadays, you can specify mount options too
* Unix: mount options
    - `mount {disk}{path}`
    - When the OS reaches a mount point, it switches inode tables
    - Unfortunately, this breaks links

## Fix: Symbolic Links

`ls -s {Source Path} {Destination Path}`

New file type - Symbolic Link
# Path Names

* Absolute Path Name
    - Starts at `/`
* Relative path
    - Starts at current directory

# Blocks

|                 |    Case 1 |      Case 2 |           General            |
| --------------- | --------: | ----------: | :--------------------------: |
| Blocksize       |        4K |          8K |             `B`              |
| Direct          |       48K |         96K |            `12B`             |
|                 |           |             |                              |
| Indirect        | 4K^2 = 4M | 16K^2 = 16M |     `B/4 * B = (B^2)/4`      |
| Doubly Indirect | 4M^2 = 4G |         32G | `(B/4)*((B^2)/4) = (B^3)/16` |
| Triply Indirect | 4G^2 = 4T |         64T |   `B/4 * B^3/16 = B^4/64`    |

# Special Files

Not disk files
* Device
  * Block
  * Character (RAW)

## Block Device
* Read/write fixed size blocks
* Data may be used by multiple running programs
* Data may be accessed multiple times
* Uses the buffer cache
* Similar to disk drive

## Character (RAW) device

* Read/Write variable amounts of data (even single bype)
* Used by a single running program
* Data used once
* goal : direct device-program interaction, little OS buffering
* Similar to terminal

Device file
* Has an inode
* Has path
* No blocklist
  * Major#: device driven
  * Minor#: instance

-------------------------------------

# Recap
## UFS
### Types
* Ordinary
* Directories
* Symbolic Links
* Special Files
  * Device
    * Block
    * Character (RAW)


### Device Files

Inodes-paths
* Metadata
* No block list
* Major #'s - which device driver
* Minor #'s - which instance
* put in `/dev`