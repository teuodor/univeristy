#include<iostream>
using namespace std;
void afisare_matrice2(int a[100][100], int n)
{
    int i,j;
    for(i=1; i<=n; i++)
    {
        for(j=1; j<=n; j++)
            if(a[i][j] != -1)
                cout<<a[i][j]<<" ";
            else
                cout<<"| ";
        cout<<"\n";
    }
    cout<<"\n";

}
int ce()
{
    int a[100][100],n,i,j,cost;
    cout<<"Numarul de noduri: ";
    cin>>n;


    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
        {
            a[i][j] = -1;
            if(i==j)
                a[i][j] = 0;
        }


    while(i!=0&&j!=0&&cost!=0)
    {
        cin>>i>>j>>cost;
        a[i][j] = a[j][i] = cost;
    }
    cout<<"Matricea ponderilor: \n";
    afisare_matrice2(a,n);
}

