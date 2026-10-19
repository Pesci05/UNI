#include <iostream>
#include <pthread.h>

using namespace std;

#define MAX 20
#define NUM_THREADS 5

int arr[MAX];

void *my_pthread_fn(void *args);

int main(){
    int res;
    pthread_attr_t attr[NUM_THREADS];
    pthread_t myThread[NUM_THREADS];
    
    for(int i = 0; i < MAX; i++){
        arr[i] = i;
        cout << arr[i] << "\t";
    }
    cout << endl;
    
    for(int i = 1; i < NUM_THREADS; i++){
        res = pthread_attr_init(&attr[i]);
        res = pthread_create(&myThread[i],&attr[i],my_pthread_fn,(void *)i);

        if(res != 0)
        {
            printf("ERROR in pthread_create. OS returned %d\n", res);
            return -1;
        }
        res = pthread_attr_destroy(&attr[i]);
    }

    my_pthread_fn((void *)0); // I am thread #0

    void * returnvalue;
    printf("Hello World! I am the MASTER thread, before joining slaves\n");
    
    for (unsigned int i = 1; i < NUM_THREADS; i++)      // <== JOIN
        res = pthread_join (myThread[i], &returnvalue);


    for(int i = 0; i < MAX;i++)
        cout << arr[i] << "\t";
    cout << endl;

    return 0;
}

void *my_pthread_fn(void *args) { 
    int my_id = (intptr_t) args; // This cast might generate a warning
    int chunk,start,end,lastChunk;

    if(MAX % NUM_THREADS == 0){
        chunk = MAX/NUM_THREADS;
        start = my_id * chunk;
        end = start + chunk;

    }else{
        chunk = MAX/NUM_THREADS + 1;
        start = my_id * chunk;
        lastChunk = MAX%chunk;

        if(my_id == NUM_THREADS-1){
            end = start + lastChunk;
        }else{
            end = start + chunk;
        }
    }

    for(int i = start; i < end; i++){
        arr[i] *= 2;
    }

    cout << start << endl;

    return NULL;
}