#include "Iterator.h"
#include <exception>
void IteratorColectie::prim()
{
	poz = 0;
	while (poz < col.capacity && (col.deleted[poz] == 1 || col.notEmpty[poz] == 0))
		poz++;
}

bool IteratorColectie::valid()
{
	return (poz < col.capacity && col.deleted[poz] == 0 && col.notEmpty[poz] == 1);
}

TElem IteratorColectie::element()
{
	return col.elemente[poz];
}

void IteratorColectie::urmator()
{
	do {
		poz++;
	} while (poz < col.capacity && (col.deleted[poz] == 1 || col.notEmpty[poz] == 0));
}
/*
Subalgortim anterior()
	Daca valid() = false atunci
		@arunca exceptie
	
	Executa
		poz <- poz - 1;
	Cat timp ( poz >= 0 si (col.deleted[poz] == 1 sau col.notEmpty[poz] == 0))
	
	Daca poz < 0 atunci
		@arunca exceptie
--------------------------------------------------------------------------------------
Complexitati:
Best Case: theta(1) - elementul este inainte cu o pozitie
Worst Case: O(size) - daca un element este pe prima pozitie si celalalt este pe ultima (apelam anteriorul de la ultimul)
Average Case: 
*/
void IteratorColectie::anterior()
{
	if (!valid())
		throw std::exception();
	do {
		poz--;
	} while (poz >= 0 && (col.deleted[poz] == 1 || col.notEmpty[poz] == 0));
	if (poz < 0)
		throw std::exception();
}
