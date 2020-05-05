#pragma once
#include "Multime.h"

class IteratorMultime {
	friend class Multime;
private:
	Multime multime;
	int poz;

public:

	IteratorMultime(Multime multime) : multime(multime), poz{ 0 } {}

	void prim() {
		poz = 0;
		while (poz < multime.capacity && (multime.deleted[poz] == 1 || multime.nempty[poz] == 0)){
			poz++;
		}
	}

	bool valid() {
		return (poz < multime.capacity && multime.deleted[poz] == 0 && multime.nempty[poz] != 0);
	}

	TElem element() {
		return multime.elemente[poz];
	}

	void urmator() {
		do {
			poz++;
		} while (poz < multime.capacity && (multime.deleted[poz] == 1 || multime.nempty[poz] == 0));
	}
};
