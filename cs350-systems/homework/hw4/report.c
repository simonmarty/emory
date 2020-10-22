// THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING A TUTOR
// OR CODE WRITTEN BY OTHER STUDENTS - Simon Marty

#include "defs.h"

int mem_id;
shared_memory *mem;
int msg_id;
message *msg;

int main(int argc, char **argv) {
    if ((mem_id = shmget(SHARED_MEM_KEY, sizeof(*mem), 0666)) == -1) {
        perror("Failed to get shared memory");
        exit(EXIT_FAILURE);
    }

    mem = shmat(mem_id, NULL, 0);

    printf("%s ", "Perfect Numbers: ");
    for(int i = 0; i < 20; i++) {
        if(mem -> perfect_numbers[i] != 0) {
            printf("%i ", mem -> perfect_numbers[i]);
        }
    }

    printf("\nPID\tTESTED\tSKIPPED\tFOUND");
    for(int i = 0; i < 20; i++) {
        if(mem -> processes[i].pid > 0) {
            printf("\n%i\t%i\t%i\t%i\t", mem -> processes[i].pid, mem -> processes[i].candidates_tested_count,
                    mem -> processes[i].candidates_skipped_count, mem ->processes[i].perfect_numbers_count);

        }
    }

    printf("\n");

    if(argc >= 2) {
        if(strcmp(argv[1], "-k") == 0) {
            kill(mem -> handler_pid, SIGINT);
        }
    }
}