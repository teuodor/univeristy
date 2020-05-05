#include "LO.h"
#include "Iterator.h"
#include <exception>
#include <iostream>
//O(cap)
void LO::resize()
{
	if (cap == 0)
		cap = 1;

	cap = 2 * cap;
	LSI *newList = new LSI[cap];
	for (int i = 0; i < size; i++)
		newList[i] = elems[i];
	for (int i = size; i < cap; i++)
		newList[i].urm = i + 1;

	newList[cap - 1].urm = -1;
	primLiber = size;
	delete elems;
	elems = newList;
}

LO::LO(Relatie r)
{
	rel = r;
	size = 0;
	cap = 0;
	elems = new LSI[cap];
	prim = 0;
	primLiber = -1;
}
//theta(1)
int LO::dim() const
{
	return size;
}
//theta(1)
bool LO::vida() const
{
	if (size == 0)
		return true;
	return false;
}
//O(size)
TElement LO::element(int i) const
{
	if (i >= 0 && i < size) {
		int aux = prim;
		for (int j = 0; j < i; j++)
			aux = elems[aux].urm;
		return elems[aux].elem;
	}
	throw std::exception();
}
//O(size) amortizat
void LO::adauga(TElement e)
{
	if(size == cap)
		resize();
	if (size == 0) { 

		elems[primLiber].elem = e;
		elems[primLiber].urm = -1;
		prim = primLiber;
		primLiber++;
	
	}
	else {
		int post = prim, pre = -1;
		while (rel(elems[post].elem, e) && post != -1) {
			pre = post;
			post = elems[post].urm;
		}
		if (pre == -1) { // inceputul listei
			int aux = elems[primLiber].urm;
			elems[primLiber].elem = e;
			elems[primLiber].urm = prim;
			prim = primLiber;
			primLiber = aux;
		}
		else if (post == -1) { // finalul listei
			elems[pre].urm = primLiber;
			elems[primLiber].elem = e;
			elems[primLiber].urm = -1;
			primLiber = size;
		}
		else { // interiorul listei
			int aux = elems[primLiber].urm;
			elems[primLiber].elem = e;
			elems[primLiber].urm = post;
			elems[pre].urm = primLiber;
			primLiber = aux;
		}

	}

	size++;
}
//theta(i)
TElement LO::sterge(int i)
{
	if (i < prim || i >= size)
		throw std::exception();
	if (i == 0)
	{
		int aux = prim;
		prim = elems[prim].urm;
		elems[aux].urm = primLiber;
		primLiber = aux;
		size--;
		return elems[aux].elem;
	}
	else
	{
		int contor = i, prev, post = prim;
		while (contor && post != -1) {
			prev = post;
			post = elems[post].urm;
			contor--;
		}
		elems[prev].urm = elems[post].urm;
		elems[post].urm = primLiber;
		primLiber = post;
		if (primLiber == -1)// ultimul element
			primLiber = size;
		size--;
		return elems[post].elem;
	}

}
//O(size)
int LO::cauta(TElement e) const
{
	int p = prim;
	for (int i = 0; i < size; i++) {
		if (rel(elems[p].elem, e) && rel(e, elems[p].elem))
			return i;
		p = elems[p].urm;
	}
	return -1;
}

Iterator LO::iterator()
{
	return Iterator(*this);
}
/*
	subalgoritm stergeCuPas(k):
		if size = 0:
			@throw exception;
		end if
		if k > size:
			stergeCuPas <- false
		else:
			i <- 0;
			p <- [size/k];
			if size % k :
				p <- p + 1;
			end if
			while p :
				sterge(i);
				i <- i + k - 1;
				p <- p - 1;
			stergeCuPas <- true;
*********************************
Complexitati:
Best case: theta(1) daca size > k sau daca lista este vida;
Worst case: theta(n) daca k = 1;
Average case: O(n);
Overall complexity: O(n)
*/
bool LO::stergeCuPas(int k)
{
	if (size == 0) {
		std::cout << "S";
		throw std::exception("S");
		
	}
	else if (k > size)
		return false;
	else {
		int i = 0;
		while (i < size) {
			sterge(i);
			i += k - 1;
		}
		return true;
	}
}

LO::~LO()
{
	delete elems;
}

