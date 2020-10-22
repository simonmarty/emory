# Midterm and Quiz Info

## Midterm

* Half
  * Short answer
  * True/False
* Other half is programming

One page, one side of notes

* IDC 
* Files
* Fork/exec

# Quiz Debrief

1. False. Linux doesn't use NULL bytes to detect EOF, it uses the file size
2. False. You can have two entries in the same directory that have the same inode number 
    * (`ln abc def`)
    * `abc` and `def` will have the same inode number
3. False. They are stored in the Ublock. the rest of the sentence is true.
4. False. First half is correct. Not because of TRAP instructions. You're gonna have to do a TRAP instruction. You're actually saving the context switch from user mode to system mode.
5. False. C doesn't have dynamic allocation. `malloc` is part of the C standard library, not the C language itself.
6. True
7. False. 
8. 64M ```16k/4*16k = 4k*16k = 64M```
9. True
10. True. 1 fork for each program, 1 exec for each program

## Writing code on the test

* Barebones
* No need to error check everything
* 

```
if(!fork) {
    fd = open("x", O_RDONLY);
    dup(fd, 0);
    close(fd);
    fd = creat("y", 0666);
    dup2(fd, 1);
    close(fd);
    execl("myprog", "myprog", "-l", "abc","def", NULL);
}
wait(&status);