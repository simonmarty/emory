// THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING A TUTOR
// OR CODE WRITTEN BY OTHER STUDENTS - Simon Marty

#include "defs.h"

int mem_id;
shared_memory *mem;
int msg_id;
message *msg;
int process_index;

void quit(int signal) {
    if (process_index < 0 || process_index >= 20) {
        exit(EXIT_FAILURE);
    }

    memset(&mem->processes[process_index], 0, sizeof(process));

    if (mem_id != -1) shmdt(mem);

    free(msg);
    exit(EXIT_SUCCESS);
}

int is_perfect_number(int n) {
    if (n < 2) return 0; // irrelevant

    int m = 1;
    for (int i = 2; i < (n / 2 + 1); i++) {
        if (n % i == 0) {
            m += i;
        }
    }

    return n == m;
}

int main(int argc, char **argv) {
    int start = (argc < 2) ? 2 : atoi(argv[1]);

    if (start >= MAXSIZE * 32 + 1) {
        exit(EXIT_FAILURE);
    }

    // Signal handling
    struct sigaction handler;
    handler.sa_handler = quit;
    sigaction(SIGHUP, &handler, NULL);
    sigaction(SIGINT, &handler, NULL);
    sigaction(SIGQUIT, &handler, NULL);


    mem_id = shmget(SHARED_MEM_KEY, sizeof(*mem), 0666);
    mem = shmat(mem_id, NULL, 0);

    msg_id = msgget(MSG_Q_KEY, 0666);
    msg = malloc(sizeof(*msg));

    msg->type = NEW_COMPUTE_PROCESS_MSG;
    msg->content = getpid();
    if (msgsnd(msg_id, msg, sizeof(msg->content), 0) == -1) {
        perror("Failed to send a message");
        exit(EXIT_FAILURE);
    }

    if (msgrcv(msg_id, msg, sizeof(msg->content), START_COMPUTING_MSG, 0) == -1) {
        perror("Failed to receive message");
    }
    process_index = msg->content;

    int i = start;
    int j = MAXSIZE * 32;
    int secondRound = 0;

    for (;;) {
        for (; i < j; i++) {
            int segment = (i - 2) / 32;
            int bit = (i - 2) % 32;

            if ((mem->nums[segment] & (1 << bit)) == 0) {
                mem->processes[process_index].candidates_tested_count++;
                mem->nums[segment] |= (1 << bit);
                if (is_perfect_number(i)) {
                    msg->type = PERFECT_NUM_FOUND_MSG;
                    msg->content = i;
                    msgsnd(msg_id, msg, sizeof(msg->content), 0);
                    mem->processes[process_index].perfect_numbers_count++;
                }
            } else {
                mem->processes[process_index].candidates_skipped_count++;
            }
        }
        if (secondRound) {
            shmdt(mem);
            free(msg);
            execl("./report", "-k", NULL);
            exit(EXIT_SUCCESS);
        }

        if (i >= MAXSIZE * 32) {
            i = 0;
            j = start;
            secondRound = 1;
        }
    }
}

