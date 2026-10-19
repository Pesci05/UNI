#include <iostream>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

#define MAX 17
#define NUM_THREADS 5

struct ThreadData
{
    int* arr;
    int sum;
    int index = 0;
};


void *mediaThread(void *args);

int main(){
    srand(time(NULL));

    int res;
    ThreadData data[NUM_THREADS];
    pthread_t myThread[NUM_THREADS];
    int vec[MAX];
    
    for(int i = 0; i < MAX; i++){
        vec[i] = rand() % 10;
        cout << vec[i] << "\t";
    }
    cout << endl;
    
    for(int i = 0; i < NUM_THREADS; i++){
        data[i].arr = vec;
        data[i].index = i;
        res = pthread_create(&myThread[i],NULL,mediaThread,(void *)&data[i]);

        if(res != 0)
        {
            printf("ERROR in pthread_create. OS returned %d\n", res);
            return -1;
        }

    }

    void * returnvalue;    
    
    for (unsigned int i = 0; i < NUM_THREADS; i++)      // <== JOIN
        res = pthread_join (myThread[i], &returnvalue);

    int sum = 0;

    for(int i = 0; i < NUM_THREADS;i++){
        cout << data[i].sum << endl;
        sum = sum + data[i].sum;
    }
    cout << "La somma :" << sum << "\tLa media : " << (double)sum/MAX << endl;
    

    return 0;
}

void *mediaThread(void *args) { 
    ThreadData* data = (ThreadData*) args; // This cast might generate a warning
    int start,end,lastChunk;
    int index = data->index;
    int chunk = MAX/NUM_THREADS;

    if(MAX % NUM_THREADS == 0){
        start = index * chunk;
        end = start + chunk;
    }else{
        chunk = MAX/NUM_THREADS + 1;
        start = index * chunk;
        lastChunk = MAX%chunk;

        if(index == NUM_THREADS-1){
            end = start + lastChunk;
        }else{
            end = start + chunk;
        }
    }
    int sum = 0;
    for(int i = start; i < end; i++){
       sum = sum + data->arr[i];
    }
    data->sum = sum;
    return NULL;
}