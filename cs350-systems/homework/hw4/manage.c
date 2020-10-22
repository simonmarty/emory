// THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING A TUTOR
// OR CODE WRITTEN BY OTHER STUDENTS - Simon Marty

#include <fcntl.h>
#include "defs.h"

int mem_id;
shared_memory *mem;
int msg_id;
message *msg;

void init_shared_mem() {
    if ((mem_id = shmget(SHARED_MEM_KEY, sizeof(shared_memory), IPC_CREAT | 0666)) == -1) { //| IPC_EXCL
        perror("failed to obtain shared memory");
        exit(EXIT_FAILURE);
    }
    mem = shmat(mem_id, NULL, 0);
    memset(mem, 0, sizeof(*mem));
    mem -> handler_pid = getpid();
}

void send_message(int type, int content) {
    msg -> type = type;
    msg -> content = content;
    msgsnd(msg_id, msg, sizeof(msg -> content), 0);
}

void read_messages() {
    if((msg_id = msgget(MSG_Q_KEY, IPC_CREAT | 0666)) == -1) {
        perror("Failed to create message queue");
        exit(EXIT_FAILURE);
    }

    msg = malloc(sizeof(*msg));

    for(;;) {
        memset(msg, '\0', sizeof(*msg));

        if(msgrcv(msg_id, msg, sizeof(msg ->content), -2, 0) == -1) {
            exit(EXIT_SUCCESS);
        }

        if(msg -> type == NEW_COMPUTE_PROCESS_MSG) {
            if(mem -> current_pid < 20) {
                mem -> processes[mem -> current_pid].pid = msg ->content;
            }
            else {
                break;
            }

            send_message(START_COMPUTING_MSG, mem -> current_pid++);
        }
        else if(msg -> type == PERFECT_NUM_FOUND_MSG) {
            int i;
            for(i = 0; i < 20; i++) {
                if(mem -> perfect_numbers[i] == msg -> content) {
                    break;
                }
                if(mem -> perfect_numbers[i] == 0) {
                    mem -> perfect_numbers[i] = msg -> content;
                    break;
                }
            }
            if(i >= 20) break;
        }

    }
}

void cleanup(int signal) {
    for(int i = 0; i < 20; i++) {
        pid_t process = mem -> processes[i].pid;
        if(process != 0) {
            kill(process, SIGINT);
        }
    }

    sleep(5);

    shmdt(mem);
    free(msg);
    msgctl(msg_id, IPC_RMID, NULL);
    shmctl(mem_id, IPC_RMID, NULL);
    exit(EXIT_SUCCESS);
}

int main(int argc, char **argv) {
    init_shared_mem();

    struct sigaction handler;
    handler.sa_handler = cleanup;
    sigaction(SIGHUP, &handler, NULL);
    sigaction(SIGINT, &handler, NULL);
    sigaction(SIGQUIT, &handler, NULL);


    read_messages();

    cleanup(0);
    exit(EXIT_SUCCESS);
}