#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n,o,p,i,j,k,l,m,q;
    scanf("%d%d",&n,&o);
    p = n/o;
    for(i=0;i<o;i++)
    {
        for(j=0;j<p;j++)
        {
            printf("  |  ");
        }
        printf("\n");
        for(k=0;k<p;k++)
        {
            printf(" / \\ ");
        }
        printf("\n");
        for(l=0;l<p;l++)
        {
            printf(" | | ");
        }
        printf("\n");
        for(m=0;m<p;m++)
        {
            printf(" | | ");
        }
        printf("\n");
        for(q=0;q<p;q++)
        {
            printf("  -  ");
        }
        printf("\n");
    }
    return 0;
}
