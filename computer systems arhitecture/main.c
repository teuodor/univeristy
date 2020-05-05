#include <stdio.h>
#include <stdlib.h>

int paritate(int);

int main()
{
    FILE*fila;
    int pare[100], impare[100],ip=0, pp=0, numar,i;
    fila = fopen("numere.txt","r");
    while(fscanf(fila,"%d",&numar)!=EOF)
    {

        if(!paritate(numar))
        {
            pare[pp] = numar;
            pp++;
        }
        else {
            impare[ip] = numar;
            ip++;
        }
    }
    printf("Numere pare:\n");
    for(i=0;i<pp;i++)
    {
        printf("%d ",pare[i]);
    }
    printf("\nNumere impare:\n");
    for(i=0;i<ip;i++)
    {
        printf("%d ",impare[i]);
    }
    return 0;
    //nasm paritate.asm -fwin32 -g -o paritate.obj
    //cl /Z7 main.c /link paritate.obj
    //main.exe
}
