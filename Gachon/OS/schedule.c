#include <stdio.h>
#include <stdlib.h>
// #include "schedule.h" 아마 없는듯 하다..
#define MAX_N 11

int total_process = 0, mode = -1;

struct node{
    int pid; // pid number
    int arrive; // arrive time
    int burst; // cpu burst time
    int start; // start time
    int finish; // finish time
    int remain; // each nodes burst time
}nodes[MAX_N];

void read_proc_list(const char* file_name){
    /* open text file and store each variance */
    FILE* fp_inlist = fopen(file_name, "r");
    fscanf(fp_inlist, "%d", &total_process);
    for (int i = 0; i < total_process; i++){
        fscanf(fp_inlist, "%d %d %d", &nodes[i].pid, &nodes[i].arrive, &nodes[i].burst);
        /* reset finish and start */
        nodes[i].finish = -1;
        nodes[i].start = -1;
        nodes[i].remain = nodes[i].burst;
    }
    fclose(fp_inlist);
}

void set_schedule(int method){
    /* print what type of scheduling */
    mode = method;
    switch (mode){
    case 1: // Run FCFS: Non-preemtive type
        printf("Scheduling method: FCFS (Non-preemptive)\n");
        break;
    case 2: // Run SJF: Non-preemtive type
        printf("Scheduling method: Shortest Job First (Non-preemptive)\n");
        break;
    case 3: // Run SRTF: preemtive type
        printf("Scheduling method: Shortest Remaining Time First (Preemptive) \n");
        break;
    }
    return;
}

int idx_process = -1; // reset pid number
int remain_time = 10000; // reset remain_time;
int i;
int min_t;
int next;

int do_schedule(int tick){
    /* Doing scheduling each case */
    int n;
    switch (mode){
    case 1: // Run FCFS: Non-preemtive type
        remain_time--; // used 1 remain time
        if (idx_process == -1 || remain_time == 0){
            if (idx_process != -1){
                nodes[idx_process].finish = tick; // set finish time
            }
            idx_process++; // next pid
            if (idx_process >= total_process) return -1; // end
            remain_time = nodes[idx_process].burst; // update remain time
            nodes[idx_process].start = tick; // start time
        }
        break;
    case 2: // Run SJF: Non-preemtive type
        remain_time--; // used 1 remain time
        if (idx_process == -1 || remain_time == 0){
            if (idx_process != -1) nodes[idx_process].finish = tick; // set finish time
            next = -1; // reset 
            min_t = 10000; // reset min time
            for (i = 0; i < total_process; i++){
                if (nodes[i].start == -1 && nodes[i].burst < min_t && nodes[i].arrive <= tick){
                    min_t = nodes[i].burst; // min_t is each pid's min burst time
                    next = i; // run what pid next time
                }
            }
            if (next == -1) return -1; // error
            idx_process = next; // run what pid?
            nodes[next].start = tick; // each pid's start time
            remain_time = nodes[next].burst; // each pid use time 
        }
        break;
    case 3: // Run SRTF: preemtive type
        if (idx_process != -1){
            nodes[idx_process].remain--; 
            if (nodes[idx_process].remain == 0) nodes[idx_process].finish = tick;
        }
        next = -1; // reset
        min_t = 10000; // reset
        for (i = 0; i < total_process; i++){
            if (nodes[i].remain != 0 && nodes[i].remain < min_t && nodes[i].arrive <= tick){
                next = i; // run what pid next time
                min_t = nodes[i].remain; // min_t is each pid's min burst time
            }
        }
        if (next == -1) return -1; // error
        if (nodes[next].start == -1) nodes[next].start = tick; // each pid's start time
        if (idx_process != next) idx_process = next; // run what pid?
        break;
    default:
        break;
    };
    return nodes[idx_process].pid; // return pid number
}

void print_performance() {
    /* print each data */
    int i, trt = 0, wt = 0, rt = 0;
    printf("============ ======== ============ ======== ============ ======== ============\n");
    printf("PID   begin   finish   Turn around time   Waiting time   Response time\n");
    printf("============ ======== ============ ======== ============ ======== ============\n");
    for (i = 0; i < total_process; i++){
        printf("%d\t ", nodes[i].pid); // print pid num
        printf("%d\t ", nodes[i].arrive); // print arrive time
        printf("%d\t\t ", nodes[i].finish); // print finish time
        trt += (nodes[i].finish - nodes[i].arrive); // sum each pid's turn around time
        printf("%d\t\t ", nodes[i].finish - nodes[i].arrive); // print turn around time
        wt += (nodes[i].finish - nodes[i].arrive - nodes[i].burst); // sum each pid's waiting time
        printf("   %d\t\t", nodes[i].finish - nodes[i].arrive - nodes[i].burst); // print waiting time
        rt += (nodes[i].start - nodes[i].arrive); // sum each pid's respons time
        printf("  \t%d\t\n", nodes[i].start - nodes[i].arrive); // print respons time
    }
    printf("============ ======== ============ ======== ============ ======== ============\n");
    printf("average: \t\t\t%5.2f \t\t%5.2f \t   \t%5.2f\n", (float)trt / (float)total_process, (float)wt / (float)total_process, (float)rt / (float)total_process);
    printf("============ ======== ============ ======== ============ ======== ============\n");
}

