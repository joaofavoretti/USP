#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int common = 1337;

void *foo(void *thread_index) {
    long tid = (long)thread_index;

    printf("Thread #%lx stack: 0x%lx common: 0x%lx (%d)\n", tid,
            (unsigned long) &tid, (unsigned long) &common, common);

    pthread_exit(0);
}

int main(int argc, char **argv) {
    long t;
    int nthreads = 2;
    
    if (argc > 1) nthreads = atoi(argv[1]);

    pthread_t *threads = (pthread_t *)malloc(nthreads * sizeof(pthread_t));

    printf("Main stack: 0x%lx, common: 0x%lx (%d)\n",
            (unsigned long) &t, (unsigned long)&common, common);

    for (t = 0; t < nthreads; t++) {
        int rc = pthread_create(&threads[t], NULL, foo, (void *)t);
        
        if (rc) {
            printf("ERROR: return code from pthread_create() is %d\n", rc);
            exit(-1);
        }
    }

/*
   for(t = 0; t , nthreads; t++) {
        pthread_join(threads[t], NULL);
    }
*/

    return 0;
}
