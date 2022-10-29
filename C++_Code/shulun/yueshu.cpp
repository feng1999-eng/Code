//
// Created by Administrator on 2022/10/17.
//

#include "iostream"
#include "vector"
#include "algorithm"
#include "unordered_map"
using namespace std;
vector<int> res;
unordered_map<int,int> primes;
typedef long long LL;
LL mod=1e9+7;
void get_res(int n)//得到n的所有约数
{
    for(int i=1;i<=n/i;i++)
    {
        if(n%i==0)
        {
            res.emplace_back(i);//通过小的约数，同时把大的约数也加进来
            if(i*i!=n)
                res.emplace_back(n/i);
        }

    }
    sort(res.begin(),res.end());
}

LL get_all_res(int n) //求约数个数
{
    LL res=1;
    while(n--)
    {
        int a;
        cin>>a;
        for(int i=2;i<=a/i;i++)
        {
            while(a%i==0)
            {
                primes[i]++;
                a/=i;
            }
        }
        if(a>1) //把大于a/i的那个质数得到，由于a=x*x,所以有且只有一个约数大约sqrt(a)
            primes[a]++;
    }
    for(auto prime:primes)
    {
        res=res*(prime.second+1)%mod;
    }
    return res;
}
LL sum_all_res(int n) //求所有约数之和
{
    LL res=1;
    while(n--)
    {
        int a;
        cin>>a;
        for(int i=2;i<=a/i;i++)//把所有是质数的约数存起来
        {
            while(a%i==0)
            {
                primes[i]++;
                a/=i;
            }
        }
        if(a>1) //把大于a/i的那个质数得到，由于a=x*x,所以有且只有一个约数大约sqrt(a)
            primes[a]++;
    }
    for(auto prime:primes)//对hash表中每个质数的所有可能相乘，eg:prime[2]=2,prime[3]=2,
                            //那么prime[2]可以给出(2^2+2^1+2^0),
                            //prime[3]可以给出(3^2+3^1+3^0),将其相乘可以得到所有约数之和。
    {
        int p=prime.first,a=prime.second;
        LL t=1;
        while(a--)
        {
            t=(t*p+1)%mod;
        }
        res=res*t;
    }
    return res;
}
int GCD(int a,int b)//辗转相除法求最大公约数
{
    return b?GCD(b,a%b):a;//若b不为0，那么执行（a,b)的最大公约数等于(b,a%b)的最大公约数，规定(a,0)的最大公约数为a
                                //gcd(a,0)=gcd(0,a)=|a|
}
int main()
{
    int a,b;
    cin>>a>>b;
    int res=GCD(a,b);//a整除b,代表b为被除数,a为除数
    cout<<res<<endl;
}