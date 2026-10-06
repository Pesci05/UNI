#include <iostream>
#include <pthread.h>

using namespace std;

void *my_pthread_fn(void *arg) { 
     cout << "Ciao dal Pthread" << endl;
    return NULL;
}

int main(){
    int res;
    pthread_attr_t attr;
    pthread_t myThread;    

    cout << "Ciao mondo" << endl;

    pthread_attr_init(&attr); //Inizializzazione degli attributi
    res = pthread_create(&myThread, &attr, my_pthread_fn, NULL ); // FORK DEL TRHEAD MAIN
    pthread_attr_destroy(&attr);

    if (res != 0){
        cout << "Error creating error" << endl;
        return -1;
    }

    pthread_join(myThread,NULL);
    
    return 0;
}