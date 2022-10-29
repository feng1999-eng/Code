//
// Created by Administrator on 2022/10/17.
//

#include "iostream"
using namespace std;
const int N=101;
bool st[N];
int prime[N],cnt=0;
bool isPrime(int n) //�ж��Ƿ�Ϊ����
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
void divde_prime(int n) //��һ�����ж��ٸ���������
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
    if(n>1)//�����һ������sqrt(n)��������
        printf("%d %d\n",1,n);
}
void get_primes_ai(int n)//ʹ�ð�ʽɸ�����ж��ٸ�������ÿ������ֹ��ɸһ��
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
void get_primes(int n)  //ʹ������ɸ����1-n֮���ж��ٸ�������ÿ������౻ɸһ�Σ����Խ�����ɸ��
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
//        cout<<"������"<<endl;
//    else
//        cout<<"��������"<<endl;
    get_primes(n);
    for(int i=0;i<cnt;i++)
    {
        cout<<prime[i]<<" ";
    }
    cout<<endl;
    cout<<cnt<<endl;
}