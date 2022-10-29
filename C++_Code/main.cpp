#include "iostream"
#include "vector"
#include "algorithm"
#include "string.h"
using namespace std;
const int N=18;
int col[N],dg[N],xdg[N];
char g[N][N];
void eight_queue(int u,int n)
{
    if(u==n)
    {
        for(int i=0;i<n;i++)
            puts(g[i]);
        puts("");
        return;
    }
    for(int i=0;i<n;i++)
    {
        if(!col[i]&&!dg[u+i]&&!xdg[n-i+u])
        {
            g[u][i]='Q';
            col[i]=dg[u+i]=xdg[n-i+u]=true;
            eight_queue(u+1,n);
            col[i]=dg[u+i]=xdg[n-i+u]= false;
            g[u][i]='.';
        }
    }
}
int main()
{
    int n=8;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        {
            g[i][j]='.';
        }

    eight_queue(0,n);
}
