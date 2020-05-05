#include <assert.h>

#include "Iterator.h"
#include "LO.h"

using namespace std;

bool relatie1(TElement cheie1, TElement cheie2) {
	if (cheie1 <= cheie2) {
		return true;
	}
	else {
		return false;
	}
}
void teststergeCuPas() {
	LO lo = LO(relatie1);
	try {
		lo.stergeCuPas(3);
		assert(false);
	}
	catch (std::exception &e) {
		assert(true);
	}
	lo.adauga(1);
	lo.adauga(2);
	lo.adauga(3);
	lo.adauga(4);
	lo.adauga(5);
	lo.adauga(6);
	lo.adauga(7);
	lo.adauga(8);
	lo.adauga(9);
	lo.adauga(10);
	assert(lo.dim() == 10);
	assert(!lo.stergeCuPas(11));
	assert(lo.stergeCuPas(2));
	assert(lo.dim() == 5);
}
void testAll() {
	teststergeCuPas();
	LO lo = LO(relatie1);
	assert(lo.dim() == 0);
	assert(lo.vida());
	lo.adauga(1);
	assert(lo.dim() == 1);
	assert(!lo.vida());
	Iterator iterator = lo.iterator();
	assert(iterator.valid());
	iterator.prim();
	assert(iterator.element() == 1);
	iterator.urmator();
	assert(!iterator.valid());
	iterator.prim();
	assert(iterator.valid());
	assert(lo.cauta(1) == 0);
	assert(lo.sterge(0) == 1);
	assert(lo.dim() == 0);
	assert(lo.vida());
}
