#pragma once

//LO.h

typedef int TComparabil;

typedef TComparabil TElement;

typedef bool(*Relatie)(TElement, TElement);
struct LSI {
	TElement elem;
	int urm;
};
class LO {
	friend class Iterator;
private:
	Relatie rel;
	/* aici e reprezentarea */
	int size;
	int cap;
	LSI *elems;
	int prim;
	int primLiber;
	void resize();

public:
	// constructor
	LO(Relatie r);

	// returnare dimensiune
	int dim() const;

	// verifica daca LO e vida
	bool vida() const;

	// returnare element
	//arunca exceptie daca i nu e valid
	TElement element(int i) const;

	// adaugare element in LO
	void adauga(TElement e);

	// sterge element de pe o pozitie i si returneaza elementul sters
	//arunca exceptie daca i nu e valid
	TElement sterge(int i);

	// cauta element si returneaza prima pozitie pe care apare (sau -1)
	int cauta(TElement e) const;

	// returnare iterator
	Iterator iterator();

	// fiind dat  un pas k,sterge toate elementele din lista din k in k
	bool stergeCuPas(int);

	//destructor
	~LO();

};