
main: main.o project.o header.h
	gcc  -o main  main.o project.o 

%.o: %.c  header.h
	gcc -g -c $<