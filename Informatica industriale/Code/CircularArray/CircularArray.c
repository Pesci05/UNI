// We need to include this because of the definition of CircularArray_t
#include "CircularArray.h"

int init_CA (struct CircularArray_t *c)
{
    // TODO implement this
    int res_e = 0;
    int res_f = 0;

    c->head = 0;
    c->tail = SIZE_CA;
    for(int i = 0; i < SIZE_CA; i++)    
        c->array[i] = 0;
    
    res_f = sem_init(&c->full, 0,SIZE_CA);
    res_e = sem_init(&c->empty, 0,0);

    if(res_e != 0 || res_f != 0){
        return -1;
    }else{
        return 0;
    }
}

void insert_CA (struct CircularArray_t *c, int elem)
{
    sem_wait(c->full);
    c->array[c->head] = elem;
    c->head = (c->head+1) % SIZE_CA;
    sem_post(c->empty);
    
}

void extract_CA (struct CircularArray_t *c, int *elem)
{
    // TODO implement extraction
    
    sem_wait(c->empty);
    *elem = c->array[c->tail];
    c->tail = (c->tail+1) % 10;
    sem_post(c->full);

}
