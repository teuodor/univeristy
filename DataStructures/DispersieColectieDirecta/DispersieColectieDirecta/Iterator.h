#pragma once

#include "Colectie.h"


class IteratorColectie {
	
	friend class Colectie;

private:

	Colectie col;
	int poz;

public:

	IteratorColectie(Colectie col) : col{ col } {
		prim();
	}

	void prim();

	bool valid();

	TElem element();

	void urmator();
	 
	void anterior();
};