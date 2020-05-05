#pragma once
#include "Colectie.h"
class Colectie;

class IteratorColectie {
	friend class Colectie;

private:
	//iteratorul memoreaza o referinta catre container
	Colectie& con;
	//aici alte atribute specifice: curent, etc
	int curent, frecv;
	IteratorColectie(Colectie& c);

public:
	TElem element();
	bool valid();
	void urmator();
	void prim();
	bool del();
};
