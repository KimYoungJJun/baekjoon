#include<stdio.h>
#include<stdlib.h>
int find_max(int a,int b,int c){
    if(a>=b && a>=c) return a;
    else if(b>=a && b>=c) return b;
    else return c;
}
void main(){
    int i,n,result=0;
    int *arr=NULL;
    scanf("%d",&n);
    arr = (int*)malloc(sizeof(int)*3*n);
    for(i = 0;i<n;i++){
        scanf("%d %d %d",&arr[i*3],&arr[i*3+1],&arr[i*3+2]);
    }
    for(i =0 ;i<n;i++){
        
        if( (arr[i*3] != arr[i*3+1]) && (arr[i*3+1] != arr[i*3+2])){
            if(result < find_max(arr[i*3],arr[i*3+1],arr[i*3+2])*100)
                result = find_max(arr[i*3],arr[i*3+1],arr[i*3+2])*100;
        }
        else if((arr[i*3] == arr[i*3+1]) && (arr[i*3] != arr[i*3+2])){
            if(result < 1000+arr[i*3]*100)
                result = 1000+arr[i*3]*100;
        }
        else if((arr[i*3] != arr[i*3+1]) && (arr[i*3+1] == arr[i*3+2])){
            if(result < 1000+arr[i*3]*100)
                result = 1000+arr[i*3+1]*100;
        }
        else if((arr[i*3] != arr[i*3+2]) && (arr[i*3] == arr[i*3+1])){
            if(result < 1000+arr[i*3]*100)
                result = 1000+arr[i*3]*100;
        }
        else if((arr[i*3] == arr[i*3+1]) && (arr[i*3] == arr[i*3+2])){
            if(result < 10000+arr[i*3]*1000)
                result = 10000+arr[i*3]*1000;
        }
        else{
            continue;
        }
    }
    printf("%d\n",result);
    free(arr);
}