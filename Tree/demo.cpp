#include <iostream>
using namespace std;
void sum(int a,int b, int & c){
    a=b+c;
    b=a+c;
    c=a+b;
}
int main(){
    int x=2,y=3;
    sum(x,y,y);
    cout<<x<<" "<<y;
    return 0;
}