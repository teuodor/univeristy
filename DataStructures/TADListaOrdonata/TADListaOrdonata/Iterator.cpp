#include "Iterator.h"

Iterator::Iterator(const LO &c) : lista(c)
{
	prim();
}
//theta(1)
void Iterator::prim()
{
	this->curent = lista.prim;
}
//theta(1)
void Iterator::urmator()
{
	if (valid()) {
		curent = lista.elems[curent].urm;
	}
	else
		throw std::exception();
}
//theta(1)
bool Iterator::valid() const
{
	if (curent == -1 || !lista.size)
		return false;
	return true;
}
//theta(1)
TElement Iterator::element()
{
	return lista.elems[curent].elem;
}
