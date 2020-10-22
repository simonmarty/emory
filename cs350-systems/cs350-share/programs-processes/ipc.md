# IPC (Cont.)

## `int pipe(int fd[2])`

* create 2 new fds
  * fd[0] input
  * fd[1] output
* Write to fd[1]
  * can be read back from fd[0] in FIFO order
* Pipe size is limited (4k)

### Example:
```
$ ls | wc    # wc = Word count
```
| Parent  | Child 1 | Child 2 |
|:---:|:----:|:---:|
| `fork()` | `fork()` | 
| `fork()` | `close(fd[0])` |`fork()` |
| `close fd[0]` | `dup2(fd[1], 1)` |  `close(fd[1])` |
| `close fd[1]` | `close(fd[1])` |`dup2(fd[0], 0)` | 
| `wait()` | `execl("ls", "ls", 0)` |`close(fd[0])` |
|`wait()` | |`execl("wc", "wc", 0)`|

## Blocking Behavior of pipes
* read
  * non-empty
  * min(rogues, avail)
  * empty
    * Blocks as long as a write end is still open
    * Otherwise returns 0
  * If you don't get end of file and write ends are open, we never exit
* write
  * if the write request is greater than the space available in the pipe, write in blocks

*producer-consumer* behavior

### `pipe(int fd[0])`
* fd[0] - input
* fd[1] - output

### Blocking behavior

* read
  * != 0: get partial data
  * Otherwise
    * Another end block
    * EOF

* write
  * Insufficient space block

### Review

* files
* pipes
* fifos (named pipes)
  * Default: blocking behavior on open
  * Non default behavior: O_NONBLOCK
    * IN the cases where you would have blocked,instead of blocking, it returns immediately.

### Missing stuff
* Transaction
* Records
* One to many, many to one communication

## Message Queue

Series of IPC methods
* framework is

```
int msg get(key_t key, int flag)
msgsnd(int msg id, char *buff, size_t size, int flag)
```
`flag` can be `IPC_NOBLK`

Buffer: 
| type | data |
|:---:|:---:|
| long | anything |

```
msgrcv(------------)
```


```
msgctl(msg id, int cmd, IPC_RMIL)
```

flag can also be `IPC_STAT`, `IPC_SET`

Application where multiple processes want to operate on the same data
* May not be practicalto move the data between processes

## MMU

* Each process has its own page table
* The OS makes sure the page tables don't have common pages on the right side. THis makes the address spaces disjoint
* Allows contiguous logical address spaces when there is no corresponding physical contiguous space