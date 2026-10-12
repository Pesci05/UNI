#include <iostream>

using namespace std;

#define CHUNK 5

struct arrayD{
    int* p;
    int numElem=0;
    int size;
};

typedef struct arrayD Array;

void add(Array &arr, int n);
void stampaArr(Array &arr);
void remove(Array &arr);
void init(Array &arr);

int main(){
    Array arr;
    
    init(arr);
    add(arr,10);
    add(arr,2);
    add(arr,9);

    stampaArr(arr);

    remove(arr);
    stampaArr(arr);

    return 0;
}

void add(Array &arr, int n){
    if(arr.numElem == arr.size){
        int *newArr = new int[arr.size+CHUNK];
        for (int i = 0; i < arr.numElem; i++){
            newArr[i] = arr.p[i];
        }
        delete[] arr.p;
        arr.p = newArr;
        arr.size++;
    }else{
        arr.p[arr.numElem] = n;
        arr.numElem++;
    }
}

void stampaArr(Array &arr){
    for (int i = 0; i < arr.numElem ; i++){
        cout << arr.p[i] << endl;
    }
}

void remove(Array &arr){
    arr.numElem--;
}

void init(Array &arr){
    arr.size = CHUNK;
    arr.numElem = 0;
    arr.p = new int[3];
}