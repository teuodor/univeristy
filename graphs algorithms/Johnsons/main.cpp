#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <fstream>


using std::vector;
using std::queue;
using std::priority_queue;

struct  Node
{
	int y, cost;
	Node(const int &a, const int &b) {
		y = a;
		cost = b;
	}
	bool operator<(const Node &A) const {
		return cost > A.cost;
	}
};

std::ifstream in("in.txt");
std::ofstream out("out.txt");

vector <Node> M[500];

priority_queue <Node> priorQ;

queue <int> q;


int h[500];
int interm[500];
int dist[500][500];
int n = 0;
bool negative = false;


void read_data() {
	int x;
	std::cin >> n;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			std::cin >> x;
			if (i != j && x != 0)
				M[i].push_back(Node(j, x));
		}
}

void bellman_ford(int start) {
	int cycle[500];
	for (int i = 0; i <= n; i++) {
		h[i] = 1e9;
		cycle[i] = 0;
	}

	h[start] = 0;

	q.push(start);

	vector<Node>::iterator it;

	while (!q.empty()) {
		int nod = q.front();

		q.pop();

		for (it = M[nod].begin(); it <= M[nod].end(); it++) {
			if (h[nod] + it->cost < h[it->y]) {
				h[it->y] = h[nod] + it->cost;
				if (cycle[it->y] > n) {
					negative = true;
					return;
				}
				else {
					q.push(it->y);
					cycle[it->y]++;
				}
			}
		}

	}

}


void empty_q() {
	while (!priorQ.empty()) {
		priorQ.pop();
	}
}

void dijkstra(int start) {
	empty_q();

	for (int i = 1; i <= n; i++) {
		dist[start][i] = 1e9;
	}
	dist[start][start] = 0;
	priorQ.push(Node(start, dist[start][start]));
	vector<Node>::iterator it;

	while (!q.empty()) {
		Node fr = priorQ.top();
		int node = fr.y;
		int cost = fr.cost;
		q.pop();

		if (dist[start][node] != cost) {
			continue;
		}

		for (it = M[node].begin(); it != M[node].end(); it++) {
			if (dist[start][node] + it->cost < dist[start][it->y]) {
				dist[start][it->y] = dist[start][node] + it->cost;
				priorQ.push(Node(it->y, dist[start][it->y]));
			}
		}
	}
}

void add_node_reweight() {
	for (int i = 1; i <= n; i++) {
		M[0].push_back(Node(i, 0));
	}
}

void johnsons() {
	add_node_reweight();
	bellman_ford(0);
	if (negative == true) {
		std::cout << "Graful are un circuit negativ";
	}

	for (int i = 1; i <= n; i++) 
		for(int j = 0; j < M[i].size();j++) {
		Node nod = M[i][j];
		nod.cost += h[i] - h[nod.y];
	}

	for (int i = 1; i <= n; i++)
		dijkstra(i);
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) 
			if (dist[i][j] != 1e9) {
				dist[i][j] += h[j] - h[i];
				std::cout << dist[i][j] << " ";
			}
			else {
				std::cout << "0 ";
			}
	std::cout << "\n";
}

int main() {
	read_data();
	johnsons();

}