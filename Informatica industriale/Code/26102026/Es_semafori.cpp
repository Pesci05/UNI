#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

typedef struct 
{
    sem_t* sem;
    char car[3];
    int id;
    /* data */
}Semaforo;


void * body(void * arg);


int main()
{
    pthread_t thread[3];
    pthread_attr_t myattr;
    int err;
    sem_t semaphore;
    Semaforo s[3];


    err = sem_init(&semaphore,0,1);
    for(int i = 0; i < 3 ;i++){
        s[i].id = i;
        s[i].sem = &semaphore;
    }
    s[0].car[0] = '.';
    s[1].car[1] = '#';
    s[2].car[2] = 'o';

    pthread_attr_init(&myattr);

    for(int i = 0; i < 3; i++){
        err = pthread_create(&thread[i],&myattr,body,(void *)&s[i]);
    }


    /*err = pthread_create(&t1, &myattr, body, (void *)&s1); // Boxing of parameters
    err = pthread_create(&t2, &myattr, body, (void *)&s2);
    err = pthread_create(&t3, &myattr, body, (void *)&s3);*/
    pthread_attr_destroy(&myattr);

    for(int i = 0; i < 3; i++){
        pthread_join(thread[i],NULL);
    }

    err = sem_destroy(&semaphore);

    return 0;
}

void * body(void * arg)
{
    Semaforo* s = (Semaforo *) arg; // Unboxing of function params

    sem_wait(s->sem);
    //printf("%d",s->id);
    for (int i=0; i<40; i++)
    {
        for (int j=0; j<20; j++)
        {
            printf("%c", s->car[s->id]);
        }
        printf("\n");
    }
    sem_post(s->sem);
}