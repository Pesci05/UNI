#include <iostream>
#include <pthread.h>
#include <semaphore.h>

using namespace std;

int a;
sem_t semaphore;


void* consumer(void* args);
void* producer(void* args);


int main(){
    pthread_t prod,cons;
    pthread_attr_t myattr;
    int err;

    err = sem_init(&semaphore,0,0);

    pthread_attr_init(&myattr);
    err = pthread_create(&prod,&myattr,producer,NULL);
    err = pthread_create(&cons,&myattr,consumer,NULL);
    
    pthread_join(prod,NULL);
    pthread_join(cons,NULL);

    err = sem_destroy(&semaphore);

    return 0;
}
void* consumer(void* args){
    sem_wait(&semaphore);
    cout << a+5 << endl;
}
void* producer (void* args){
    sem_post(&semaphore);
    a = 11;
}