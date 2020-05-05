#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

const int MAX_CAPACITY = 100;
const int INF = 1000000000;

void citire(int &n, int &m, vector<pair<int, int> > vecini[MAX_CAPACITY]) {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		int x, y, z;
		scanf("%d %d %d", &x, &y, &z);
		x--;
		y--;
		vecini[x].push_back({ y, z });
		vecini[y].push_back({ x, z });
	}
}

void prim(const int &n, const int &m, vector<pair<int, int> > vecini[MAX_CAPACITY]) {
	int cost[MAX_CAPACITY];
	bool viz[MAX_CAPACITY];
	int parinte[MAX_CAPACITY];
		
	for (int i = 0; i < n; i++) {
		cost[i] = INF;
		viz[i] = false;
		parinte[i] = i;
	}

	cost[0] = 0;

	for (int i = 0; i < n; i++) {
		int minVal = INF;
		int minPoz = 0;

		for (int j = 0; j < n; j++) {
			if (viz[j] == false && minVal > cost[j]) {
				minVal = cost[j];
				minPoz = j;
			}
		}

		if (parinte[minPoz] != minPoz) {
			printf("(%d, %d)\n", minPoz + 1, parinte[minPoz] + 1);
		}

		if (minVal != INF) {
			viz[minPoz] = true;

			for (auto el : vecini[minPoz]) {
				if (cost[el.first] > el.second && viz[el.first] == false) {
					cost[el.first] = el.second;
					parinte[el.first] = minPoz;
				}
			}
		}
		else {
			printf("WTF MAN?");
		}
	}
	
}

int main() {
	freopen("date.in", "r", stdin);

	int n, m;
	vector<pair<int, int> > vecini[MAX_CAPACITY];
	citire(n, m, vecini);
	prim(n, m, vecini);

	while (true);

	return 0;
}