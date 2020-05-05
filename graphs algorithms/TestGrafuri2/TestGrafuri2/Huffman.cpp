#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

vector<pair<char, string> > coduri;

struct Nod {
	Nod *st, *dr;
	int frecventa;
	char caracter;
	Nod(char caracter, int frecventa) : caracter{ caracter }, frecventa{ frecventa }, st{ NULL }, dr{ NULL } {}
	Nod(int frecventa) : caracter{0},frecventa{frecventa}, st{NULL}, dr{NULL} {}
};

class cmp {
public:
	bool operator()(Nod* n1, Nod* n2) {
		return n1->frecventa >= n2->frecventa;
	}
};


vector<pair<char, int> > citire() {
	ifstream in("date.in");
	vector<pair<char, int> > toReturn;
	int frecvente[260];
	int n;
	in >> n;
	for (int i = 0; i < n; i++) {
		char c; 
		int frecv;
		in >> c >> frecv;
		toReturn.push_back({ c,frecv });
	}

	return toReturn;
}

void afisare(vector<pair<char, string> > p) {
	for (int i = 0; i < p.size(); i++) {
		if(p[i].first != 0)
			cout << p[i].first << " : " << p[i].second << " \n";
	}
}

Nod* Huffmann(vector<pair<char, int> > frecv) {
	priority_queue <Nod*, vector<Nod*>, cmp> priorQ;

	for (auto el : frecv) {
		priorQ.push(new Nod(el.first, el.second));
	}

	while (priorQ.size() > 1) {
		Nod* nod1 = priorQ.top();
		priorQ.pop();
		Nod* nod2 = priorQ.top();
		priorQ.pop();

		Nod* papa = new Nod(nod1->frecventa + nod2->frecventa);
		papa->st = nod1;
		papa->dr = nod2;

		priorQ.push(papa);
	}

	return priorQ.top();
}

void genereazaCod(Nod* nod, string cod) {
	if (nod->st) {
		genereazaCod(nod->st, cod + "0");
	}
	if (nod->dr) {
		genereazaCod(nod->dr, cod + "1");
	}

	coduri.push_back({ nod->caracter,cod });
}

int main() {
	vector<pair<char, int> > frecv = citire();

	Nod* final = Huffmann(frecv);

	genereazaCod(final, "");

	afisare(coduri);

	while (true);
	return 0;
}

/*
f 0
c 100
d 101
a 1100
b 1101
e 111
*/

