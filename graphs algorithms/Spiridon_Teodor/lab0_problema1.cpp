#include <iostream>

using namespace std;
void afisare_matrice_adiacenta(int a[100][100], int n)
{
    int i,j;
    for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
                cout<<a[i][j];
            cout<<"\n";
        }
    cout<<"\n";

}
void afisare_matrice_incidenta(int a[100][100],int row,int col)
{
    int i,j;
    for(i = 1;i<=row;i++)
    {
        for(j=0;j<col;j++)
            cout<<a[i][j];
        cout<<"\n";
    }

}
void afisare_lista(int a[100][100],int n)
{
    int i,j;
    for(i=1;i<=n;i++)
    {
        for(j = 1; j < a[i][0]; j++)
            cout<<a[i][j];

        cout<<"\n";
    }
}
int main()
{
    int n,i = 1,j = 1,adiac[100][100],incid[100][100],row,col,nr_muchii = 0,adiac2[100][100],lista[100][100];

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

    cout<<"Matricea de adiacenta: \n";
    afisare_matrice_adiacenta(adiac,n);


    for(row = 1; row<=n; row++)
        for(col = 1; col<=n; col++)
            if(adiac[col][row] && row<=col)
            {
                incid[row][nr_muchii] = incid[col][nr_muchii] = 1;
                nr_muchii++;
            }


    cout<<"Matricea de incidenta: \n";
    afisare_matrice_incidenta(incid,n,nr_muchii);

    for(row = 1; row<=n; row++)
        for(col = 1; col<=n; col++)
            adiac2[col][row] = 0;


    for(col = 0; col <= nr_muchii; col++)
        {
            int ind1 = 0,ind2 = 0;
            for(row = 1; row <= n; row++)
                if(incid[row][col])
                    break;
            ind1 = row;
            for(row = ind1 + 1; row <= n; row++)
                if(incid[row][col])
                    break;

            ind2 = row;

            if(ind1 && ind2)
                adiac2[ind1][ind2] = adiac2[ind2][ind1] = 1;

        }
    cout<<"Matricea de adiacenta 2: \n";
    afisare_matrice_adiacenta(adiac2,n);

    for(i=1;i<=n;i++)
       {
        int ind1=1;
        for(j=1;j<=n;j++)
            if(adiac2[i][j])
            {
              lista[i][ind1] = j;
              ind1++;
            }
        lista[i][0] = ind1;
       }

    cout<<"Lista: \n";
    afisare_lista(lista,n);

}
