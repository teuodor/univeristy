#include "Iterator.h"

Iterator::Iterator(const LO& c) : c(c)
{
	prim();
}

//theta(1)
void Iterator::prim()
{
	this->current = c.prim;
}

//theta(1)
void Iterator::urmator()
{
	if (valid())
		current = c.lista[current].urm;
	else
	{
		throw std::exception();
	}
}

//theta(1)
bool Iterator::valid() const
{
	if (current == -1)
		return false;
	return true;
}

//theta(1)
TElement Iterator::element() const
{
	return c.lista[current].elem;
}
