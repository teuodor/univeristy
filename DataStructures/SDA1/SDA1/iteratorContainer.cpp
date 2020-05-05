#include "iteratorContainer.h"
#include "container.h"
#include<stdexcept>


IteratorContainer::IteratorContainer(const Container& c) : con(c) {
	// initializare curent si alte atribute specifice
	curent = 0;
	frecvCurenta = 0;
}

TElem IteratorContainer::element() {
	//TBA
	if (valid() and con.vida()!=true)
		return con.minim+curent;
	return -1;
}

bool IteratorContainer::valid() {
	//TBA
	if (curent < con.lungime)
		return true;
	return false;
}

void IteratorContainer::urmator() {
	//TBA
	if (valid())
		if (frecvCurenta == con.elems[curent]) {
			frecvCurenta = 0;
			curent++;
		}
		else
			frecvCurenta++;
	else
		throw std::exception(
			"Nu exista un element urmator"
		);
}

void IteratorContainer::prim() {
	//TBA
	curent = 0;
	frecvCurenta = 0;
}