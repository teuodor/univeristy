#pragma once
#include "container.h"

class Container;

class IteratorContainer
{
	friend class Container;

private:
	//iteratorul memoreaza o referinta catre container
	const Container& con;
	//aici alte atribute specifice: curent, etc
	int curent, frecvCurenta;
	IteratorContainer(const Container& c);

public:
	TElem element();
	bool valid();
	void urmator();
	void prim();
};