#include <stdio.h>
 
int Num[1000001];
 
int min(int a, int b){
    return a > b ? b : a;
}
 
int main(void){
 
    int N;
    scanf("%d", &N);
 
    Num[1] = 0;
 
    for (int i = 2; i <= N; i++)
    {
        Num[i] = Num[i - 1] + 1;
        if (i % 2 == 0)
            Num[i] = min(Num[i], Num[i / 2] + 1);
        if (i % 3 == 0)
            Num[i] = min(Num[i], Num[i / 3] + 1);
    }

    printf("%d\n", Num[N]);
    return 0;
}