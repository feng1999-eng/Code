//
// Created by Administrator on 2022/10/17.
//

#include "iostream"
using namespace std;
const int N=101;
bool st[N];
int prime[N],cnt=0;
bool isPrime(int n) //判断是否为质数
{
    if(n<2)
        return false;
    for(int i=2;i<=n/i;i++)
    {
        if(n%i==0)
            return false;
    }
    return true;
}
void divde_prime(int n) //求一个数有多少个质数因子
{
    for(int i=2;i<n/i;i++)
    {
        if(n%i==0)
        {
            int s=0;
            while(n%i==0)
            {
                s++;
                n/=i;
            }
            printf("%d %d\n",s,i);
        }
    }
    if(n>1)//最多有一个大于sqrt(n)的质因子
        printf("%d %d\n",1,n);
}
void get_primes_ai(int n)//使用埃式筛法求有多少个质数，每个数不止被筛一次
{
    for(int i=2;i<=n;i++)
    {
        if(!st[i])
        {
            prime[cnt++]=i;
        }
        for(int j=i+i;j<=n;j+=i)
        {
            st[j]=true;
        }

    }
}
void get_primes(int n)  //使用线性筛法求1-n之间有多少个质数，每个数最多被筛一次，所以叫线性筛法
{
    for(int i=2;i<n;i++)
    {
        if(!st[i])
        {
            prime[cnt++]=i;
        }
        for(int j=0;prime[j]<=n/i;j++)
        {
            st[prime[j]*i]=1;
            if(i%prime[j]==0)
                break;
        }
    }
}
int main()
{
    int n;
    cin>>n;
//    if(isPrime(n))
//        cout<<"是质数"<<endl;
//    else
//        cout<<"不是质数"<<endl;
    get_primes(n);
    for(int i=0;i<cnt;i++)
    {
        cout<<prime[i]<<" ";
    }
    cout<<endl;
    cout<<cnt<<endl;
}