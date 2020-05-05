#include "Multime.h"
#include "IteratorMultime.h"

IteratorMultime Multime::iterator() const
{
	return IteratorMultime(*this);
}
