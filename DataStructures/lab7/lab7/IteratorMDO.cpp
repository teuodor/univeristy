/*#include "IteratorMDO.h"

void IteratorMDO::prim()
{
	int nr = c.Minim(c.radacina);
	curent = c.Elemente[nr];
}

void IteratorMDO::urmator()
{
	curent = Noduri.push_back();
}

bool IteratorMDO::valid() const
{
	if (curent == -1)
		return false;

	return true;
}

TElem IteratorMDO::element() const
{
	if (valid() == false)
		throw 1;

	TElem pereche = make_pair(c.Elemente[curent].first, c.Elemente[curent].second);
	
	return pereche;
}

void IteratorMDO::inorder()
{
	int radacina = c.radacina;
	int aux;

	while (noduri.empty() == false || radacina != -1)
	{
		aux = radacina;
		while (radacina != -1)
		{
			noduri.push(c.Elemente[radacina]);
			radacina = c.Stanga[radacina];
		}
		Noduri.push_back(noduri.top());
		noduri.pop();
		radacina = c.Dreapta[aux];
	}
}*/
