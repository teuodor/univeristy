#pragma once

#include"LO.h"
#include<exception>

typedef int TComparabil;

typedef TComparabil TElement;

typedef bool(*Relatie)(TElement, TElement);

class Iterator {
	friend class LO;
private:

	const LO& lista;

	int curent;

	Iterator(const LO&);
public:

	void prim();

	void urmator();

	bool valid() const;

	TElement element();
};