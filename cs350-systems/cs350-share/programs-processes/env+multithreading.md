# Parameters

Parameters to the program before it runs

* Explicit: `a.out alpha -x beta.c`
* Implicit parameters
  * Many parameters shared by many programs
  * Too awkward to specify each time
  * Terminal Type, rows in the terminal, language for messages, organization, home dir

## Uses the environment
  * List of key value pairs
  * ROWS = 20
  * ORGANIZATION = EMORY

```
main(intc, char **argv, char **envp) {
    int i;
    printf("My PID is %d\nHere is my environment:\n", getpid());

    for(int i = 0; envp[i] != NULL; i++) {
        printf("%s \n", envp[i]);
    }

    exit(EXIT_SUCCESS);
}
```

## Creating a new process

### `int fork()`

* Clones the current process
* Copies the
  * Text
  * Data
  * BSS
  * Stack
  * Ublock
    * New PID
    * CPU Time reset
    * fd table unchanged


```
if(!fork()) {
  // child
}
else {
  // parent
}
```

Issue: right now both processese are running the same program. We need another system call to run two *different* programs

### `execl(char *path, char *arg0, char arg1, 0)`

* `path`: path to a aprogram
* replaces
  * text
  * data
  * bss
  * stack  
In the current process wrom the file at `path`
* sets
  * PC &rarr; main
  * SP &rarr; new stack containing `argv`, `envp`
  * UBlock keeps same fd table
  * (change in signal handling)

Now our program is like this

```
if(!fork()) {
  execl("newprog", ..., 0);
}
else {
  // parent
}
```
### `int wait(int *status)`
* Process block until a child dies

*Macros*
* `WIFEXITED(status)`
* `WIFSIGNALED`
* `WEXITSTATUS`
* `WTERMSIG`

```
if(!fork()) {
  execl("newprog", ...)
}
else {
  wait(&status);
}
```

* Parents should always wait for thei children - until then child is a zombie
* IF parent dies before child is waited for, Init PID 1 inherits the child.


# Midterm: Thursday Nov 14

```
int fork()
  - clones current process
  - child PID
```
```
int execl(char *path, char *arg0, arg1 ... , 0)
```


```
% prog abc -x <alph> beta
```

What the shell does

```
if(!fork()) {
  //child
  close(0); 
  open("alpha", O_RONLY);
  close(1);
  creat("beta", o664);
  execl("prog", "prog", "abc", "-x", 0);
} else {
  wait(&status);

  ...
}
```

### Several versions of `exec`
* `execl`
* `execv`
* `execle`
* `execve`
* `execi`

