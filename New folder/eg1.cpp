#include<bits/stdc++.h>
using namespace std;

vector<int> parent, spf;

void sieve(int N, vector<int> &spf) {
    spf = vector<int> (N);
    for(int i = 1; i < N; ++i)
        spf[i] = i;
    for(int i = 2; i < N; i += 2)
        spf[i] = 2;
    for(int i = 3; i < N; i += 2)
        if (spf[i] == i)
            for(int j = i; j < N; j += i)
                if (spf[j] == j)
                    spf[j] = i;
}

int find(int node) {
    return node == parent[node] ? parent[node] : parent[node] = find(parent[node]);   
}

// int power(long long int xx,int count,int MOD ) {
//     if(xx==0 || xx==1) return xx%MOD;
//     if(count==0) return 1;
//     if(MOD==1) return 0;
//     long long int ans=1;

//     while(count){
//         if(count%2) ans=(ans*xx)%MOD;
//         xx=(xx*xx)%MOD;
//         count/=2;
//     }
//     return ans;
// }

void countStablePartitions(int n, vector<int>& values) {
    sieve(*max_element(values.begin(), values.end()) + 1, spf);
    unordered_map <int, unordered_set<int>> primes;
    for(int i = 0; i < n; ++i) {
        int num = values[i];
        while(num != 1) {
            primes[spf[num]].insert(i);
            num /= spf[num]; 
        }
    }
    
    parent = vector<int> (n); 
    for(int i = 0; i < n; ++i)
        parent[i] = i;
    for(auto x: primes) {
        int i = *x.second.begin();
        x.second.erase(x.second.begin());
        for(int j: x.second)
            parent[find(i)] = find(j);
    }
    int unique=0;
    vector<int> components(n); 
    for(int x: parent){
        int p=find(x);
        components[p]++;
        if(components[p]==1)unique++;
    }
    if(unique<2){
        cout<<"NO"<<endl;
        cout<<0<<endl;
    } 
    else{
        cout<<"YES"<<endl;
            if(unique==0){ cout<<1;
             return;}
        cout<<((((int)(pow(2,unique)))%1000000007)-2);
    }
}

int main(){
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   int n;
   cin >> n;
   vector<int> values(n);
   for (int i = 0; i < n; ++i) {
        cin >> values[i];
   }
   countStablePartitions(n, values);
   return 0;
}