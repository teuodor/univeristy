/*#include "MDO.h"
#include<iostream>
#include <stack>

using namespace std;

class IteratorMDO
{
private:
	MDO& c;
	TElem curent;

	stack<TElem> noduri;
	vector<TElem> Noduri;

public:
	IteratorMDO(MDO& c) :c{ c }, curent{ c.radacina } {
		inorder();
	}

	//reseteaza pozitia iteratorului la inceputul containerului
	void prim();

	//muta iteratorul in container
	// arunca exceptie daca iteratorul nu e valid
	void urmator();

	//verifica daca iteratorul e valid (indica un element al containerului)
	bool valid() const;

	//returneaza valoarea elementului din container referit de iterator
	//arunca exceptie daca iteratorul nu e valid
	TElem element() const;

	void inorder();
};*/