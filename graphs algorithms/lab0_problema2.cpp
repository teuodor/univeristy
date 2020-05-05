#include <iostream>
using namespace std;
void copyMat(int mat1[100][100],int n,int mat2[100][100])
{
    for(int i = 1; i <= n; i++)
        for(int j = 0; j<=n; j++)
            mat2[i][j] = mat1[i][j];
}
void warshall(int a[100][100],int n)
{
    for(int k = 1 ; k <= n ; ++k)
        for(int i = 1 ; i <= n ; ++i)
            for(int j = 1 ; j <= n ; ++j)
                if( i != j && a[i][j] == 0)
                    a[i][j] = a[i][k] * a[k][j];
}
void afisareVect(int v[100],int lung)
{
    for(int i=0; i<lung; i++)
        cout<<v[i]<<" ";
    cout<<"\n";
}
int izolat(int adiac[100][100],int n,int noduri[100],int &lung)
{
    int i=0;
    for(int row = 1; row<=n; row++)
    {
        int s=0;
        for(int col = 1; col<=n; col++)
            s+=adiac[row][col];
        if(s==0)
        {
            noduri[i] = row;
            i++;
        }

    }
    lung = i;
    if(i==0)
        return 0;
    return 1;
}
int regular(int adiac[100][100],int n)
{
    int val;
    for(int row = 1; row <= n; row++)
    {
        int s = 0;
        for(int col = 1; col<=n; col++)
            s += adiac[row][col];

        if(row == 1)
            val = s;
        else if(s != val)
            return 0;
    }
    return 1;
}
int conex(int a[100][100],int n)
{
    for(int i = 1; i <= n; i++)
        for(int j = 1; j<=n; j++)
            if(i != j && a[i][j] == 0)
                return 0;
    return 1;
}
void afisare_matrice(int a[100][100], int n)
{
    int i,j;
    for(i=1; i<=n; i++)
    {
        for(j=1; j<=n; j++)
            cout<<a[i][j];
        cout<<"\n";
    }
    cout<<"\n";

}
int main()
{
    int n,adiac[100][100],row,col,noduri[100],ok,lung,drumuri[100][100],i,j;

    cout<<"Numarul de noduri: ";
    cin>>n;

    for(row = 1; row<=n; row++)
        for(col = 1; col<=n; col++)
            adiac[col][row] = 0;

    while(i != 0 && j != 0)
    {
        cin>>i>>j;
        adiac[i][j] = 1;
        adiac[j][i] = 1;
    }


    afisare_matrice(adiac,n);

    ok = izolat(adiac,n,noduri,lung);
    if (ok)
    {
        cout<<"Nodurile izolate: ";
        afisareVect(noduri,lung);
    }
    else
        cout<<"Nu exista noduri izolate.\n";


    copyMat(adiac,n,drumuri);
    warshall(drumuri,n);
    cout<<"Matricea drumurilor: \n";
    afisare_matrice(drumuri,n);


    ok = regular(adiac,n);

    if(ok)
        cout<<"Graful este regular.\n";
    else
        cout<<"Graful nu este regulat.\n";

    ok = conex(drumuri,n);

    if(ok)
        cout<<"Graful este conex.\n";
    else
        cout<<"Graful nu este conex.\n";




}
