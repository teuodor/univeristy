#include "Colectie.h"
#include "Iterator.h"

int Colectie::dim() const
{
	return size;
}

bool Colectie::vida() const
{
	return size == 0;
}

IteratorColectie Colectie::iterator() const
{
	return IteratorColectie(*this);
}

Colectie::~Colectie()
{
	delete[]elemente;
	delete[]deleted;
	delete[]notEmpty;
}

Colectie::Colectie()
{
	size = 0;
	capacity = 13;


	elemente = new TElem[capacity];
	deleted = new int[capacity];
	notEmpty = new int[capacity];

	for (int i = 0; i < capacity; i++) {
		elemente[i] = 0;
		deleted[i] = 0;
		notEmpty[i] = 0;
	}
}

Colectie::Colectie(const Colectie & col)
{
	capacity = col.capacity;
	size = col.size;

	elemente = new TElem[capacity];
	notEmpty = new int[capacity];
	deleted = new int[capacity];

	for (int i = 0; i < capacity; i++) {
		elemente[i] = col.elemente[i];
		notEmpty[i] = col.notEmpty[i];
		deleted[i] = col.deleted[i];
	}
}

void Colectie::adauga(TElem e)
{
	resize();

	for (int i = 0; i < capacity; i++) {
		int poz = abs((hash1(e) + i * hash2(e)) % capacity);
		if (deleted[poz] == 1 || notEmpty[poz] == 0) {
			elemente[poz] = e;
			deleted[poz] = 0;
			notEmpty[poz] = 1;
			size++;
			return;
		}
	}
}

bool Colectie::sterge(TElem e)
{
	for (int i = 0; i < capacity; i++) {
		int poz = abs((hash1(e) + i * hash2(e)) % capacity);

		if (deleted[poz] == 0 && notEmpty[poz] == 0)
			return false;
		else if (elemente[poz] == e && deleted[poz] == 0) {
			deleted[poz] = 1;
			notEmpty[poz] = 0;
			size--;
			return true;
		}
	}
	return false;
}

bool Colectie::cauta(TElem elem) const
{
	for (int i = 0; i < capacity; i++) {
		int poz = abs((hash1(elem) + i * hash2(elem)) % capacity);
		if (deleted[poz] == 0 && notEmpty[poz] == 0)
			return false;
		else if (elemente[poz] == elem && deleted[poz] == 0)
			return true;
	}

	return false;
}

int Colectie::nrAparitii(TElem elem) const
{
	int nrAparitii = 0;
	for (int i = 0; i < capacity; i++) {
		int poz = abs((hash1(elem) + i * hash2(elem)) % capacity);
		if (deleted[poz] == 0 && notEmpty[poz] == 0)
			break;
		else if (elemente[poz] == elem && deleted[poz] == 0) {
			nrAparitii++;
		}
	}
	return nrAparitii;
}


