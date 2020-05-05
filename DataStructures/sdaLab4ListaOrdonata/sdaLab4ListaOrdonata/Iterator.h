#pragma once
#include "LO.h"
#include <exception>

typedef int TComparabil;

typedef TComparabil TElement;

typedef bool(*Relatie)(TElement, TElement);

class Iterator
{
private:
	friend class LO;
	friend class LSI;
	//constructorul primeste o referinta catre Container
	//iteratorul va referi primul element din container
	Iterator(const LO& c);

	//contine o referinta catre containerul pe care il itereaza
	const LO& c;

	/* aici e reprezentarea specifica a iteratorului*/
	int current;

public:

	//reseteaza pozitia iteratorului la inceputul containerului
	void prim();

	//muta iteratorul in container
	// arunca exceptie daca iteratorul nu e valid
	void urmator();

	//verifica daca iteratorul e valid (indica un element al containerului)
	bool valid() const;

	//returneaza valoarea elementului din container referit de iterator
	//arunca exceptie daca iteratorul nu e valid
	TElement element() const;

};

