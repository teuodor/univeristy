#include <cstdio>
#include <vector>

using namespace std;

const int MAX_N = 100;

void citire(int &n, int &m, vector<int> vecini[MAX_N]) {
	scanf("%d %d", &n, &m);
	int x, y;

	for (int i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);
		x--; y--;

		vecini[x].push_back(y);
		vecini[y].push_back(x);
	}
}

bool canBeEuler(int n, vector<int> vecini[MAX_N]) {
	for (int i = 0; i < n; i++) {
		if (vecini[i].size() % 2 != 0) {
			return false;
		}
	}

	return true;
}

int viz[2][MAX_N];
void dfs(int nod, int which, vector<int> vecini[MAX_N], int x, int y) {
	viz[which][nod] = 1;

	for (auto el : vecini[nod]) {
		if (viz[el] == 0) {
			if (which == 1 && x == nod && y == el) {
				continue;
			}
			if (which == 1 && y == nod && x == el) {
				continue;
			}
			dfs(el, which, vecini, x, y);
		}
	}
}

bool isBridge(int n, int x, int y, vector<int> vecini[MAX_N]) {
	for (int i = 0; i < n; i++) {
		viz[0][i] = 0;
		viz[1][i] = 0;
	}

	dfs(0, 0, vecini, x, y);
	dfs(0, 1, vecini, x, y);
	
	for (int i = 0; i < n; i++) {
		if (viz[0][i] != viz[1][i]) {
			return true;
		}
	}
	return false;
}

void generareCiclu(int n, int m, vector<int> vecini[MAX_N]) {
	int curent = 0;


}

int main() {
	freopen("date.in", "r", stdin);

	int n, m;
	vector<int> vecini[MAX_N];

	citire(n, m, vecini);
	if (canBeEuler(n, vecini)) {
		generareCiclu(n, m, vecini);
	}
	else {
		printf("Graful nu este eulerian!");
	}

	return 0;
}