#include "testScurt.h"
#include <assert.h>
#include "Container.h"
#include "iteratorContainer.h"
#include <stdio.h>





void testAll() { //apelam fiecare functie sa vedem daca exista
	Container c;
	assert(c.vida() == true);
	assert(c.dim() == 0); //adaug niste elemente
	c.adauga(5);
	assert(c.getMIN() == 5);
	assert(c.getMAX() == 5);
	c.adauga(1);
	assert(c.getMIN() == 1);
	assert(c.getMAX() == 5);
	assert(c.cauta(5) == true);
	assert(c.cauta(1) == true);
	c.adauga(10);
	assert(c.getMIN() == 1);
	assert(c.getMAX() == 10);
	assert(c.cauta(5) == true);
	assert(c.cauta(1) == true);
	assert(c.cauta(10) == true);
	c.adauga(7);
	assert(c.cauta(5) == true);
	assert(c.cauta(1) == true);
	assert(c.cauta(10) == true);
	assert(c.cauta(7) == true);
	assert(c.getMIN() == 1);
	assert(c.getMAX() == 10);
	c.adauga(1);
	assert(c.cauta(5) == true);
	assert(c.cauta(1) == true);
	assert(c.cauta(10) == true);
	assert(c.cauta(7) == true);
	assert(c.getMIN() == 1);
	assert(c.getMAX() == 10);
	c.adauga(11);
	assert(c.cauta(5) == true);
	assert(c.cauta(1) == true);
	assert(c.cauta(10) == true);
	assert(c.cauta(7) == true);
	assert(c.cauta(11) == true);
	assert(c.getMIN() == 1);
	assert(c.getMAX() == 11);
	assert(c.getLUN() == 11);
	assert(c.nrAparitii(5) == 1);
	assert(c.nrAparitii(1) == 2);
	assert(c.nrAparitii(10) == 1);
	assert(c.nrAparitii(7) == 1);
	assert(c.nrAparitii(11) == 1);
	assert(c.dim() == 6);
	c.adauga(-3);
	assert(c.getLUN() == 15);
	assert(c.getMIN() == -3);
	assert(c.getMAX() == 11);
	assert(c.dim() == 7);
	assert(c.nrAparitii(5) == 1);
	assert(c.cauta(5) == true);
	assert(c.cauta(1) == true);
	assert(c.cauta(10) == true);
	assert(c.cauta(7) == true);
	assert(c.cauta(11) == true);
	assert(c.cauta(-3) == true);
	assert(c.cauta(16) == false);
	assert(c.nrAparitii(1) == 2);
	assert(c.nrAparitii(7) == 1);
	assert(c.sterge(1) == true);
	assert(c.sterge(6) == false);
	assert(c.dim() == 6);
	assert(c.nrAparitii(1) == 1);
	IteratorContainer ic = c.iterator();
	ic.prim();
	while (ic.valid()) {
		TElem e = ic.element();
		ic.urmator();
	}
}
