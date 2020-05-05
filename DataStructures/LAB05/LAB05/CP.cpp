#include "CP.h"
#include <algorithm>

const int inf = 1000000000;

//theta(dim)
void CP::checkCap()
{
	if (dim == cap) {
		cap += cap*4;
		cap = (cap == 0) ? 1 : cap;
		Element *newElem = new Element[cap];
		for (int i = 0; i < dim; i++)
			newElem[i] = elems[i];

		delete[] elems;
		elems = newElem;
	}
}
//O(log 2 dim)
void CP::heapifyUp()
{
	if (dim == 1) {
		return;
	}

	int x = dim - 1;
	while (x) {
		if (rel(elems[x].second, elems[getParent(x)].second)) {
			std::swap(elems[x], elems[getParent(x)]);
		}
		else {
			break;
		}

		x = getParent(x);
	}
}
//O(log 2 dim)
void CP::heapifyDown()
{
	int x = 0;
	while (x < dim) {
		bool swapped = false;
		int bestChild;
		int bestVal = inf;
		for (int i = 1; i <= 4; i++) {
			if (getChild(x, i) > dim) {
				break;
			}
			if (!rel(elems[x].second, elems[getChild(x, i)].second)) {
				if (elems[getChild(x, i)].second < bestVal) {
					bestVal = elems[getChild(x, i)].second;
					bestChild = i;
				}
				swapped = true;
			}
		}
		if (!swapped) {
			break;
		}
		std::swap(elems[x], elems[getChild(x, bestChild)]);
		x = getChild(x, bestChild);
	}
}
//theta(1)
int CP::getParent(int index)
{
	return (index - 1) / 4;
}
//theta(1)
int CP::getChild(int index, int nr)
{
	return index * 4 + nr;
}
//O(log 2 dim) amortizat
void CP::adauga(TElem e, TPrioritate p)
{
	checkCap();
	elems[dim] = {e,p};
	dim++;
	heapifyUp();
}
//theta(1)
Element CP::element() const
{
	if (dim == 0)
		throw std::exception("Salut.");

	return elems[0];
}
//O(log 2 dim)
Element CP::sterge()
{
	if(dim == 0)
		throw std ::exception("Salut.");

	Element toReturn = elems[0];
	elems[0] = elems[dim - 1];
	dim--;
	//Element x = elems[0];
	heapifyDown();
	return toReturn;
}
//theta(1)
bool CP::vida() const
{
	return dim == 0;
}

CP::~CP()
{
	delete[] elems;
}
