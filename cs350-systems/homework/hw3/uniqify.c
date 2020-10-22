// THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING A TUTOR OR
// CODE WRITTEN BY OTHER STUDENTS 
// Simon Marty - 2283420

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>
#include <string.h>
#include <ctype.h>

int main() {
    pid_t pid1, pid2;
    int sort_pipe[2];
    int supp_pipe[2];
    int status1, status2;

    if (pipe(sort_pipe) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    if (pipe(supp_pipe) == -1) {
        perror("pipe 2");
        exit(EXIT_FAILURE);
    }

    if ((pid1 = fork()) == -1) {
        perror("pid 1");
        exit(EXIT_FAILURE);
    } else if (pid1 == 0) {    // sort child
        close(sort_pipe[1]);
        close(supp_pipe[0]);
        dup2(sort_pipe[0], STDIN_FILENO);
        dup2(supp_pipe[1], STDOUT_FILENO);
        close(sort_pipe[0]);
        close(supp_pipe[1]);

        execl("/usr/bin/sort", "sort", (char *) NULL);
        exit(EXIT_FAILURE);
    }

    if ((pid2 = fork()) == -1) {
        perror("pid2");
        exit(EXIT_FAILURE);
    } else if (pid2 == 0) {    // suppress child
        close(sort_pipe[0]);
        close(sort_pipe[1]);
        dup2(supp_pipe[0], STDIN_FILENO);
        close(supp_pipe[1]);
        close(supp_pipe[0]);

        int size = 37;
        char word[size];
        char next[size];

        fgets(word, size, stdin);
        int count = 1;

        while (fgets(next, size, stdin) != NULL) {
            if (strcmp(word, next) == 0) {
                count++;
            } else {
                printf("%-5d %s", count, word);
                count = 1;
                strcpy(word, next);
                memset(next, '\0', size);
            }
        }
        printf("%-5d %s", count, word);
        exit(EXIT_SUCCESS);
    }

    close(sort_pipe[0]);
    FILE *f = fdopen(sort_pipe[1], "w");
    char buffer[34];
    int pos = 0;
    char c;
    while ((c = fgetc(stdin)) != EOF) {
        if (isalpha(c)) {
            c = tolower(c);
            if(pos < 32)
                buffer[pos++] = c;

        }
        else {
            buffer[pos++] = '\n';
            buffer[pos++] = '\0';
            if(pos - 2 >= 5) {
                fputs(buffer, f);
            }
            pos = 0;
        }
    }

    fclose(f);
    close(supp_pipe[1]);
    close(supp_pipe[0]);
    close(sort_pipe[1]);

    wait(&status1);
    wait(&status2);
    return 0;
}
