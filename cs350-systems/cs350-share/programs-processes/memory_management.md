# Memory Management

MMU &rarr; to Memory Physical addresses: p | d  
&darr;
page table: each process gets his own

By keeping the page table dijoint, the MMU imposes separation between processes address spaces

Logical as tare contiguous even if there is no physical set of contiguous pages

* Allows shared
  * Test
  * Libraries
* fork is fast
* exec
  * First time not affected
  * fast if another process running that code
* allows data sharing using the system API for share memory

# Shared Memory API (SystemV, POSIX)

`int shmget(key_t key, int size, int flag)`  
`shmat(int sid, void *addr, int flag)`  
`shmdt(void *addr)`  
`shm ctl(int sid, int cmd, ...)`

## How to deal with shared resource
* shared memory
* Peripheral for ex
  * Printer

### Lockfile
* contents
  * 0: available
  * 1: in use

```
lock=1
fd = open("Lockfile", 2)
while(lock) {
    read(fd, &lock, 4)
    lseek(fd, 0, 0);
}
lock = 1;
write(fd, &lock, 4)
lseek
```

# Review

Shared memory: reciever doesn't know when memory is changed, synchronization is important.
Lockfiles are a solution, but very coarse.
* Use semaphores

## Classic System V signals

* Way of communicating between an OS and a process
* Sending it directly to a process
* Default behavior on signal reception is to die
* Signal can be caught by a handler

### Signal table

* Can hold SIG_IGN, SIG_DFLT (default), or a handler address

### `signal(int signum, SIG_*** or handler address)

```
handler(int signum) {
    signal()
}
```

### Send a signal: `kill(int pid, int signum)`
