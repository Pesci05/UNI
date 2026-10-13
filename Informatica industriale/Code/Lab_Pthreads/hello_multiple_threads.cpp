#include <iostream>
#include <pthread.h>

#define NUM_THREAD 5

using namespace std;

void *my_pthread_fn(void *args) { 
    int my_id = (int) args; // This cast might generate a warning

    cout << "Sono il thread numero" << my_id << endl;
    return NULL;
}

int main(){
    int res;
    pthread_attr_t attr[NUM_THREAD];
    pthread_t myThread[NUM_THREAD];    

    cout << "Ciao mondo" << endl;

    for(int i = 0; i < NUM_THREAD; i++){
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
    
    for (unsigned int i = 1; i < NUM_THREAD; i++)      // <== JOIN
        res = pthread_join (myThread[i], &returnvalue);

    printf("Hello World! I am the MASTER thread, after joining slaves\n");
    
    
    return 0;
}