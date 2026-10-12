#include <iostream>
using namespace std;

void inc(int* x);

int main()
{
    int a = 10;
    int* b = &a;
    cout << "valore a prima" << a << endl;
    inc(b);
    cout << "valore a dopo" << a << endl;
    return 0;
}
void inc(int* x){
    *x = *x +1;
    cout << "Valore di y: " << *x << endl;
}