/*  Given an array[] of N integers include 0. the tast is to find 
  the smallest positive number missing from the array 
  CONSTRAINTS:
  1 <= N <= 10^6
  -10^6 <= Ai <= 10^6
  */

#include "bits/stdc++.h"
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    
    bool check[n];
    for(int i=0;i<n;i++){
        if(arr[i]<0){
            check[i]=false;
        }
        else{
            check[i]=true;
        }
        
    }
    int ans=-1;
    for  (int i=1;i<n;i++){
        if(check[i]==false){
            ans=i;
            break;

        }

    }
    
    
    cout<<ans;
    return 0;
} 