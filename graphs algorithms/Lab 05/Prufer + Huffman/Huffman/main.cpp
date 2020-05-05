#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <unordered_map>

using namespace std;

unordered_map<char, string> coduri;

struct Nod {
	Nod *st, *dr;
	int frecventa;
	char caracter;

	Nod() = default;

	Nod(char caracter, int frecventa) : frecventa{ frecventa }, caracter{ caracter }, st{ NULL }, dr{ NULL } { }
	Nod(int frecventa) : caracter{ 0 }, frecventa{ frecventa }, st{ NULL }, dr{ NULL } { }
};

class cmpNod {
public:
	bool operator() (const Nod *n1, const Nod *n2) {
		return n1->frecventa >= n2->frecventa;
	}
};

void afisareCodat() {
	freopen("date.in", "r", stdin);
	char x;

	while (EOF != (x = getchar())) {
		cout << coduri[x];
	}
}

vector<pair<char, int> > citireFrecvente() {
	freopen("date.in", "r", stdin);

	char x;
	int frecvente[260];
	vector<pair<char, int> > toReturn;

	for (int i = 0; i < 260; i++) {
		frecvente[i] = 0;
	}

	while (EOF != (x = getchar())) {
		frecvente[x]++;
	}

	for (int i = 0; i < 260; i++) {
		if (frecvente[i] != 0) {
			toReturn.push_back({ i, frecvente[i] });
		}
	}

	return toReturn;
}

Nod* buildTree(vector<pair<char, int> > frecvente) {
	priority_queue<Nod*, vector<Nod*>, cmpNod> pq;

	for (auto el : frecvente) {
		pq.push(new Nod{ el.first, el.second });
	}

	while (pq.size() > 1) {
		Nod *n1 = pq.top();
		pq.pop();
		Nod *n2 = pq.top();
		pq.pop();

		Nod *x = new Nod(n1->frecventa + n2->frecventa);
		x->st = n1;
		x->dr = n2;

		pq.push(x);
	}

	return pq.top();
}

void generateCodes(Nod* nod, string cod) {
	if (nod->st) {
		generateCodes(nod->st, cod + "0");
	}

	if (nod->dr) {
		generateCodes(nod->dr, cod + "1");
	}

	if (nod->caracter) {
		coduri[nod->caracter] = cod;
	}
}

int main() {
	vector<pair<char, int> > frecvente = citireFrecvente();
	Nod *root = buildTree(frecvente);
	generateCodes(root, "");

	for (auto el : coduri) {
		cout << el.first << " " << el.second << "\n";
	}

	afisareCodat();

	while (true);

	return 0;
}