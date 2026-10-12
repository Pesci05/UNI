#include <iostream>

using namespace std;

int* creaArray(int n){
    int* b = (int*) malloc(sizeof(int)*n);
    return b;
}

int main(){
    int n = 10;
    int* arr = creaArray(n);

    for (int i = 0; i < n ; i++){
        *(arr+i) = i;
    }
     
    for (int i = 0; i < n ; i++){
        cout << *(arr+i) << endl;
    }

    return 0;
}