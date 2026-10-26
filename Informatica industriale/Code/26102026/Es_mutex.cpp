#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

typedef struct 
{
    pthread_mutex_t* mut;
    char car[3];
    int id;
    /* data */
}Mutex;


void * body(void * arg);


int main()
{
    pthread_t thread[3];
    pthread_attr_t myattr;
    int err;
    pthread_mutex_t mut;
    Mutex m[3];


    err = pthread_mutex_init(&mut,0);
    for(int i = 0; i < 3 ;i++){
        m[i].id = i;
        m[i].mut = &mut;
    }
    m[0].car[0] = '.';
    m[1].car[1] = '#';
    m[2].car[2] = 'o';

    pthread_attr_init(&myattr);

    for(int i = 0; i < 3; i++){
        err = pthread_create(&thread[i],&myattr,body,(void *)&m[i]);
    }


    /*err = pthread_create(&t1, &myattr, body, (void *)&s1); // Boxing of parameters
    err = pthread_create(&t2, &myattr, body, (void *)&s2);
    err = pthread_create(&t3, &myattr, body, (void *)&s3);*/
    pthread_attr_destroy(&myattr);

    for(int i = 0; i < 3; i++){
        pthread_join(thread[i],NULL);
    }

    err = pthread_mutex_destroy(&mut);

    return 0;
}

void * body(void * arg)
{
    Mutex* m = (Mutex *) arg; // Unboxing of function params

    pthread_mutex_lock(m->mut);
    //printf("%d",s->id);
    for (int i=0; i<40; i++)
    {
        for (int j=0; j<20; j++)
        {
            printf("%c", m->car[m->id]);
        }
        printf("\n");
    }
    pthread_mutex_unlock(m->mut);
}