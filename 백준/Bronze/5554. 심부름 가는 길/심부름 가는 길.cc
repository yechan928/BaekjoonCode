#include <stdio.h>

int main(){
    int num;
    int x=0;
    for(int i=0;i<4;i++){
        scanf("%d",&num);
        x += num;
    }
    printf("%d\n",x/60);
    printf("%d",x%60);

    return 0;

}