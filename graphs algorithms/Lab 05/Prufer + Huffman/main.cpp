#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

const int MAX_CAPACITY = 100;

void citire(vector<int> vecini[MAX_CAPACITY], int &n){
    scanf("%d", &n);

    for(int i = 1; i < n; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        vecini[x].push_back(y);
        vecini[y].push_back(x);
    }
}

void afisare(vector<int> vecini[MAX_CAPACITY], int n){
    for(int i = 1; i <= n; i++){
        printf("Vecinii lui %d: ", i);

        for(auto el : vecini[i]){
            printf("%d ", el);
        }
        printf("\n");
    }
}

void codificarePrufer(vector<int> vecini[MAX_CAPACITY], int n, int prufer[MAX_CAPACITY]){
    int viz[MAX_CAPACITY];
    int nr = 0;

    for(int i = 0; i < MAX_CAPACITY; i++){
        viz[i] = 0;
        prufer[i] = 0;
    }

    priority_queue<int, vector<int>, greater<int> > q;

    for(int i = 1; i <= n; i++){
        if(vecini[i].size() == 1){
            q.push(i);
        }
    }


	for (int ramas = n; ramas > 2; ramas--) {
        int x = q.top();
        int y = vecini[x][0];
        q.pop();

        prufer[nr] = vecini[x][0];
		nr++;
        vecini[x].clear();

        for(int i = 0; i < vecini[y].size(); i++){
            if(vecini[y][i] == x){
                vecini[y].erase(vecini[y].begin() + i);
                break;
            }
        }

        if(vecini[y].size() == 1){
            q.push(y);
        }
    }
}

void decodificarePrufer(int n, int prufer[MAX_CAPACITY]) {
	int viz[MAX_CAPACITY];

	for (int i = 0; i < MAX_CAPACITY; i++) {
		viz[i] = 0;
	}

	for (int i = 0; i < n; i++) {
		viz[prufer[i]]++;
	}

	for (int i = 0; i < n - 2; i++) {
		for (int j = 1; j <= n; j++) {
			if (viz[j] == 0) {
				printf("(%d, %d) ", j, prufer[i]);
				viz[prufer[i]]--;
				viz[j]--;
				break;
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		if (viz[i] == 0) {
			printf("(%d, ", i);
			for (int j = i + 1; j <= n; j++) {
				if (viz[j] == 0) {
					printf("%d)", j);
					return;
				}
			}
		}
	}
}

int main()
{
    freopen("date.in", "r", stdin);

    vector<int> vecini[MAX_CAPACITY];
    int n;
    citire(vecini, n);

    int prufer[MAX_CAPACITY];
    codificarePrufer(vecini, n, prufer);

    for(int i = 0; i < n - 2; i++){
        printf("%d ", prufer[i]);
    }

	decodificarePrufer(n, prufer);

	while (true);

    return 0;
}
