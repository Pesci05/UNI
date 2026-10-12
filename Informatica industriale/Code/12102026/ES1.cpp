#include <iostream>

using namespace std;

struct counter{
    int i = 0;
};

typedef struct counter counter;

void stampaCounter(counter c);
void incrementaCounter(counter* c);
void decrementaCounter(counter* c);

int main(){
    counter c;
    stampaCounter(c);
    
    for(int i = 0; i < 5; i++){
        incrementaCounter(&c);
    }

    stampaCounter(c);

    for(int i = 0; i < 3; i++){
        decrementaCounter(&c);
    }

    stampaCounter(c);

    return 0;
}

void stampaCounter(counter c){
    cout << "Valore contatore: " << c.i << endl;
}
void incrementaCounter(counter* c){
    c->i = c->i +1;
    stampaCounter(*c);
}
void decrementaCounter(counter* c){
    c->i = c->i - 1;
    stampaCounter(*c);
}