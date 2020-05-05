#include "LO.h"

//theta(size)
void LO::resize()
{
	if (cap == 0)
		cap = 1;

	cap *= 2;
	LSI* newList = new LSI[cap];
	for (int i = 0; i < size; ++i)
		newList[i] = lista[i];
	for (int i = size; i < cap; ++i)
		newList[i].urm = i + 1;
	newList[cap - 1].urm = -1;
	this->primLiber = size;
	delete lista;
	lista = newList;
}


LO::LO(Relatie r)
{
	this->rel = r;
	this->size = 0;
	this->cap = 0;
	this->lista = nullptr;
	this->primLiber = -1;
	this->prim = -1;
}

//theta(1)
int LO::dim() const
{
	return this->size;
}

//theta(1)
bool LO::vida() const
{
	if (this->size == 0)
		return true;
	return false;
}

//O(size)
TElement LO::element(int i) const
{
	if (i>=0&&i<this->size)
	{
		int aux = this->prim;
		for (int j = 0; j < i; j++)
			aux = lista[aux].urm;
		return lista[aux].elem;
	}
	throw std::exception();
}

//O(size)
void LO::adauga(TElement e)
{
	if (this->primLiber == -1)
		resize();
	int i = this->prim;
	int prev = -1;
	while (i != -1 && rel(lista[i].elem, e))
	{
		prev = i;
		i = lista[i].urm;
	}
	//daca elem este chiar primul adaugat la lista
	if (prev == -1)
	{
		lista[primLiber].elem = e;
		int aux = lista[primLiber].urm;
		lista[primLiber].urm = prim;
		prim = primLiber;
		primLiber = aux;
	}
	else
	{
		lista[primLiber].elem = e;
		int aux = lista[primLiber].urm;
		lista[primLiber].urm = i;
		lista[prev].urm = primLiber;
		primLiber = aux;
	}
	++size;
}

//O(size)
TElement LO::sterge(int i)
{
	if (i >=0 && i < this->size)
	{
		size--;
		//daca trebuie sters primul elem din lista
		if (i == 0)
		{
			int aux = prim;
			prim = lista[prim].urm;
			lista[aux].urm = primLiber;
			primLiber = aux;
			return lista[aux].elem;
		}
		
		else
		{
			int aux = this->prim;
			for (int j = 1; j < i; j++)
				aux = lista[aux].urm;
			int aux2 = lista[aux].urm;
			lista[aux].urm = lista[lista[aux].urm].urm;
			lista[aux2].urm = primLiber;
			primLiber = aux2;
			return lista[aux2].elem;
		}
	}
	throw std::exception();
}

//O(size)
int LO::cauta(TElement e) const
{
	int aux = this->prim;
	int i = 0;
	while (aux != -1)
	{
		if (lista[aux].elem == e)
			return i;
		i++;
		aux = lista[aux].urm;
	}
	//daca elem nu a fost gasit
	return -1;
}

Iterator LO::iterator()
{
	return Iterator(*this);
}

LO::~LO()
{
}

void LO::stergereIntre(TPozitie inceput, TPozitie sfarsit) {
	//O(size*abs(inceput-sfarsit))
	for (int i = inceput; i < sfarsit; i++)
		sterge(i);//O(size)

}

