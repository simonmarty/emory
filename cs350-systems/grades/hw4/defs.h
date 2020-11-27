// THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING A TUTOR
// OR CODE WRITTEN BY OTHER STUDENTS - Simon Marty

#ifndef HW4_DEFS_H
#define HW4_DEFS_H

#include<sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/msg.h>
#include <signal.h>

#define MAXSIZE 1048576

#define NEW_COMPUTE_PROCESS_MSG 1
#define PERFECT_NUM_FOUND_MSG 2
#define START_COMPUTING_MSG 3

#define SHARED_MEM_KEY 38947
#define MSG_Q_KEY 48593

typedef struct message {
    long type;
    int content;
} message;

typedef struct process {
    pid_t pid;
    int perfect_numbers_count;
    int candidates_tested_count;
    int candidates_skipped_count;
} process;

typedef struct shared_memory {
    pid_t handler_pid;
    pid_t current_pid;
    process processes[20];

    int perfect_numbers[20];
    unsigned int nums[MAXSIZE];

} shared_memory;

#endif //HW4_DEFS_H
