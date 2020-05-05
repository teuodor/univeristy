#include<iostream>
#include<assert.h>
#include"Colectie.h"
#include"IteratorColectie.h"
#include"TestExtins.h"
#include"TestScurt.h"
void testDel() {
	Colectie c;

	IteratorColectie ic = c.iterator();

	c.adauga(0);
	c.adauga(8);
	c.adauga(5);
	c.adauga(10);
	c.adauga(12);

	assert(ic.del());
	ic.urmator();
	ic.urmator();
	assert(ic.valid());

	ic.prim();
	ic.del();
	ic.del();
	ic.del();
	ic.del();

	assert(!ic.valid());

}
int main() {
	testDel();
	testAll();
	testAllExtins();
	Colectie c;
	// iterare
	IteratorColectie ic = c.iterator();
	while (ic.valid()) {
		TElem e = ic.element();
		// prelucrare element
		ic.urmator();
	}

	std::cout << "End";


}