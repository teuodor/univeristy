#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

const int MAX_N = 1000;
const int INF = 1000000000;

int n, m;
int s, t;
vector<int> vecini[MAX_N];
int flux[MAX_N][MAX_N];
int capacitate[MAX_N][MAX_N];
int viz[MAX_N];

void citire() {
	scanf("%d %d", &n, &m);
	//scanf("%d %d", &s, &t);
	s = 0;
	t = n - 1;

	int x, y, z;
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &x, &y, &z);
		x--; y--;

		vecini[x].push_back(y);
		vecini[y].push_back(x);
		capacitate[x][y] += z;
	}
}

vector<int> dfsRes;

void dfs(int x) {
	if (x == t) {
		dfsRes.push_back(x);
		return;
	}

	for (auto el : vecini[x]) {
		if (viz[el] == false && capacitate[x][el] - flux[x][el] > 0) {
			viz[el] = true;
			dfs(el);
			if (dfsRes.size() > 0) {
				dfsRes.push_back(x);
				return;
			}
		}
	}
}

void resetDfs() {
	dfsRes.clear();
	for (int i = 0; i < n; i++) {
		viz[i] = false;
	}
}

void solve() {
	int fluxTotal = 0;

	while (true) {
		resetDfs();
		dfs(s);
		reverse(dfsRes.begin(), dfsRes.end());

		int val = INF;
		int l = dfsRes.size() - 1;

		if (dfsRes.size() == 0) {
			break;
		}

		for (int i = 0; i < l; i++) {
			int x = dfsRes[i];
			int y = dfsRes[i + 1];

			val = min(capacitate[x][y] - flux[x][y], val);
		}


		for (int i = 0; i < l; i++) {
			int x = dfsRes[i];
			int y = dfsRes[i + 1];

			flux[x][y] += val;
			flux[y][x] -= val;
		}

		if (val == INF) {
			printf("Mozzart");
			break;
		}

		fluxTotal += val;
	}

	printf("%d\n", fluxTotal);
}

int main() {
	freopen("maxflow.in", "r", stdin);
	freopen("maxflow.out", "w", stdout);
	//freopen("date.in", "r", stdin);

	citire();
	solve();

	//while (true);

	return 0;
}