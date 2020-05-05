
//LO.h

#pragma once
#include "Iterator.h"
#include <exception>

typedef int TComparabil;

typedef TComparabil TElement;
typedef int TPozitie;

typedef bool(*Relatie)(TElement, TElement);

class LSI {
public:
	TElement elem;
	int urm;
};

class LO {
private:
	friend class Iterator;
	Relatie rel;
	/* aici e reprezentarea */
	int size;
	int cap;
	LSI *lista;
	int primLiber;
	int prim;

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

	//destructor
	~LO();

	void stergereIntre(TPozitie inceput, TPozitie sfarsit);

};