// 202135842 조태완
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

# define true 1
# define false 0

int cnt = 0;
pthread_mutex_t mutex;

int cntPrime(int num){
    int cnt = 0;
    int i;
    if(num < 2) return false;
    
    for(i=0; i*i<num; i++){
        if(num%i == 0) cnt++;
    }
    if(i*i == num) cnt++;
    if(cnt == 1) return true;
    else return false;
}

void *partial_prime(void* param){
    int range = *(int *)param;
    printf("thread for range (%d ~ %d)\n", range, range+99999);

    // add logic to count the number of prime numbers within the range (increase cnt with mutex lock)
    /* acquire the mutex lock */
    pthread_mutex_lock(&mutex);

    /* critical section */
    for (int i=range; i<range+99999; i++) {
		if (cntPrime(i) == true) cnt++;
	}

    /* release the mutex lock */
    pthread_mutex_unlock(&mutex);

    pthread_exit(0);
}

int main(int argc, char* argv[]){
    int range = atoi(argv[1]);

    struct timespec start, finish;
    double elapsed;

    // add logic to get time clock(i.e., start)
    clock_gettime(CLOCK_MONOTONIC, &start);

    // add logic to initialize mutex lock
    pthread_mutex_init(&mutex, NULL);

    int num_thread = 0;
    pthread_t tids[1024];
    int limit[1024];

    int idx = 0;
    while(idx < range){
        limit[num_thread] = idx;
        // add logic to create threads
        pthread_create(&tids[num_thread], NULL, partial_prime, (void*) &limit[num_thread]);
        num_thread++;
        idx += 100000;
        if (idx+1 > range) idx = range;
    }

    // add logic to wait all the threads until they finish the prime number computation
    for(int i=0; i<num_thread; i++){
        pthread_join (tids[i], (void **) NULL);
    }

    // add logic to measure the time clock difference
    clock_gettime(CLOCK_MONOTONIC, &finish);
    elapsed = (finish.tv_sec - start.tv_sec);
	elapsed += (finish.tv_nsec - start.tv_nsec) / 1000000000.0;

    printf("elapsed time: %f sec \n", elapsed);
    printf("The number of prime numbers between 1~%d is %d\n", range, cnt);
    return 0;
}
