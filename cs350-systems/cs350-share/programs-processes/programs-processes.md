# Programs and Processes

# Programs

A program is a file of executable code in "`a.out`" format
* ELF format (*Extended Linker Format*)

### ELF format
* Magic Number : Architecture
* Section sizes (text, data, bss, symbols)
* Text
* Data
* BSS
* Symbols (Optional)

BSS is compressed, since it just contains uninitialized static scope variables, EX: GCC file size is actually smaller than the sum of the sizes of `text`, `data` and `bss`.

--------------------------------
## Process

A process is a program in execution. It is a logical container for a running program and its resources
When executing a program:
* OS allocates an address space large enough for the program
* Copies the sections in the ELF file into the address space
* Sets PC <- Main and SP <- Bottom of the stack.

|  Process  |                            |
| :-------: | :------------------------: |
|     U     |                            |
|   stack   | (argv) SP <- bot. of stack |
| <br></br> |                            |
|    BSS    |                            |
|   DATA    |                            |
|   TEXT    |         PC <- main         |

* Stack contains `argv` vector
* U block (user block) PCB
  * All the info the OS needs to provice service to the process

The U block contains:
* UID
* GID
* CWD current working directory
* Process ID (PID)
* Parent Process ID (PPID)
* times
* file Table
* state - all the registers

Every process sits on the OS stack

|   OS Stack    |                                       |
| :-----------: | :-----------------------------------: |
|     Stack     |            Processes here             |
| Process Table / BSS | Holds pointers to processes' U blocks |
|     DATA      |                                       |
|     TEXT      |                                       |

Suppose a 1-core, 1-thread CPU

### Run Queue
* List of processes ready to run
* OS will switch between processes in the run queue
* When switching between processes, registers are dumped in the `state` portion of its corresponding U-block

* The run queue may contain priority values for each process, which will be used by the scheduler to determine which process to run next.   
* To ensure each program has a fair share of resources, each one is run for some time period (quantum) before it is paused and placed back into the run queue.   
* When a program is stopped to let another run, the program with the highest priority in the run queue is then allowed to execute.

Processes can be displayed with `ps [l]`

----------------------
## Quick Recap
* Program - compiled binary
* Process is a program in execution
  * Can only reference its address space
  * Envelope for the resources used by the running program.

# System Interface

Processes go through OS to interact with hardware
###  System calls
  * CPU modes
    * User mode
    * privilege mode
      * Access to all memory
      * Privilege constructs (I/O instructions)
  * Trap Instruction
    * Sets PC to an address in the OS
      * PC <-  Address in the OS (Syscall handler)
      * SP <- Stack pointer in OS
      * Put CPU into priv mode

### Executing a syscall process
* Push a syscall # onto stack (# corresponds to the service)
* Push parameters for the service onto the stack
* **trap**

System API is the system calls
* The system calls one function that are hardware and operating system specific - and contain assembly code

* POSIX defines a set of such functions
* On POSIX like operating systems, they are in (g)libc
  * Convenience functions written in C
    * strcpy
  * System calls
  * Header files
    * `/usr/include`
      * function prototypes
      * data type definitions (typedefs)
      * macros
      * 
Documentation
* System manual 
  * `$ man` command
    1. Shell commands
    2. System calls
    3. Functions

Errors from system calls
* If fail, return `-1`
* Set global variable `errno` with a code from the error.

### Example code

```
#include <sys/types.h> /* for creat */
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h> /* for exit */
#include <unistd.h> /* for close */

#include <stdio.h> /* for perror*/
#include <errno.h>

int main() {

    int fd;
    if ((fd=creat("abc",0))== -1) {
        perror("creat");
        exit (1);
    }
    close(fd);
}
```

# File API

path -> fd - file description

Actions operate on fd's
* Read
* Write Seek

`int creaf(char *path, int mode)`
* Creates a file at the path specified
* Returns a fd
* If the file did not exist
  * Requires write permissions in the directory (return -1 otherwise)
  * The mode is the permission of the new file
* If the file did exist
  * Truncate the file
  * Uses the existing Inode
  * Permission unchanged 
  * Fails if no write permission on existing file (-1)

# IPC

* files
* pipes
  * IPC between processes with common parent

```
ls | wc
```

Example

DB Server and
DB client: no common parent

## FIFO
* Special file type
* `mkfifo(char *path, int perm)`
* `open afifo(`
  * O_RDONLY &rarr; fdr
  * O_WRONLY &rarr; fdw

Actually
* pipe(fd[2])
* fdr &harr; fd[0]
* fdw &harr; fd[1]

works just like 
```
a pipe
```
A fifo is a named pipe

## Blocking

Same for pipes and fifo

Read:
* &ne; &empty; `min(request, avail)`
* &empty;
  * a process is on the other side
    * block
  * othewise returns 0

Write:
* not enough capacity to honor request blocks

FIFO Default: open blocks unless the other side has been opened

## Non Blocking behavior

Controlled by an open flag O_NONBLOCK

Example:

```
fdr = open("myfifo", O_RDONLY | O_NONBLOCK)
fdw = open("myfifo", O_WRONLY | O_NONBLOCK)
```
* Return a valid fdr without blocking
* Fails if no process on the other side (-1)

For both pipes and fifos: O_NONBLOCK
* read: from a non null pipe, never blocks
write: reqeust exceeds capacity, fails (-1)

### What's with these open flags? (review)

fd:
| I | &rarr; F &larr; | Off |
|:--:|:---:|:---:|

### `fcntl(int fd, F_SETFL, flag)`

Flags: F_SETFL, F_GETFL
* can use to set NONBLOCK for pipes

OS is essentially
* Run queues
* Waiting queues

Blocking is what syncs the two up

## Demo