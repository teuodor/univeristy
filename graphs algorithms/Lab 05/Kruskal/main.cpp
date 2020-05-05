#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<pair<int, pair<int, int> > > muchii;
int apmSum = 0;
vector<pair<int, int> > apm;
int parinte[100];

void citire() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		int x, y, z;
		scanf("%d %d %d", &x, &y, &z);
		x--;
		y--;

		muchii.push_back({ z, { x, y } });
	}
}

int getRoot(int x) {
	int y = x;

	while (y != parinte[y]) {
		y = parinte[y];
	}

	return y;
}

void join(int x, int y) {
	parinte[x] = y;
}

void solve() {
	for (int i = 0; i < n; i++) {
		parinte[i] = i;
	}

	sort(muchii.begin(), muchii.end());

	for (auto el : muchii) {
		int cost = el.first;
		int x = el.second.first;
		int y = el.second.second;

		if (getRoot(x) != getRoot(y)) {
			apm.push_back({ x + 1, y + 1 });
			apmSum += cost;
			join(getRoot(x), getRoot(y));
		}
	}
}

void afisare() {
	printf("%d\n%d\n", apmSum, n - 1);

	for (auto el : apm) {
		printf("%d %d\n", el.first, el.second);
	}
}

int main() {
	freopen("date.in", "r", stdin);

	citire();
	solve();
	afisare();

	while (true);

	return 0;
}