#include <cstdio>
#include <stack>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

int n, m;
pair<int, int> muchii[500000];
int viz[500000];
vector<int> vecini[100000];

void citire() {
	scanf("%d %d", &n, &m);

	int x, y;
	for (int i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);
		x--; y--;
		muchii[i] = { x, y };

		vecini[x].push_back(i);
		vecini[y].push_back(i);

		viz[i] = 0;
	}
}

void eulerCycle() {
	stack<int> S;
	S.push(0);
	vector<int> sol;
	
	while (!S.empty()) {
		int x = S.top();

		if (vecini[x].size() > 0) {
			int i = vecini[x].back();
			vecini[x].pop_back();

			if (viz[i] == 0) {
				viz[i] = 1;
				
				int x1 = muchii[i].first;
				int x2 = muchii[i].second;

				if (x2 == x) {
					swap(x1, x2);
				}

				S.push(x2);
			}
		}
		else {
			S.pop();
			sol.push_back(x);
		}
	}

	reverse(sol.begin(), sol.end());
	sol.pop_back();
	for (auto el : sol) {
		printf("%d ", el + 1);
	}
}

bool isEuler() {
	for (int i = 0; i < n; i++) {
		if (vecini[i].size() % 2 != 0) {
			return false;
		}
	}
	return true;
}

int main() {
	freopen("ciclueuler.in", "r", stdin);
	freopen("ciclueuler.out", "w", stdout);

	citire();
	if (isEuler()) {
		eulerCycle();
	}
	else {
		printf("-1\n");
	}

	return 0;
}