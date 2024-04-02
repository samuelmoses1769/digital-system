#include<iostream>
using namespace std;
int main()
{
    string s;
    cout<<"enter string ";
    cin>>s;
    for(int i=0;i<s.length();i=i+1)
    {
        cout<<s[i]-'a'<<endl;
    }
    return 0;
}