# Homework 3: Uniquity

HelLosqmy_friend
My66HEllO

Output
1 friend
2 hello
3 my

2 pipes:  
parse &rarr; sort &rarr; suppress

sort out:
* friend
* hello
* hello
* my
* my

suppress: counts

* parse reads from stdin
* suppress writes to stdout
* parse is parent, does two forks
* sort and suppress are the children of parse
* No grandchildren
* Don't forget wait()s
* parse makes the two pipes
* Make sure to close them
* 

  
### C library subroutines you should use
* isalpha
* islower
* sort
* fgetc(stdin) # Use this, it uses the stdio routine
* fdopen() # Give it an fd, it gives you a stream