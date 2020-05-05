#include "IteratorColectie.h"



IteratorColectie::IteratorColectie(const Colectie& c) : con(c) {
	// initializare curent si alte atribute specifice
	curent = 0;
	frecv = 1;
}

TElem IteratorColectie::element() {
	int contor = 0;
	if (valid() && con.vida() == false)
	{
		if (contor == curent)
			return con.elems[0];
		for (int i = 0; i < con.num; i++)
			if (rel(con.elems[i], con.elems[i + 1]) && !rel(con.elems[i + 1], con.elems[i]))
			{
				contor++;
				if (contor == curent)
					return con.elems[i + 1];
			}

	}
	return -1;
}

bool IteratorColectie::valid() {
	int contor = 0;
	for (int i = 0; i < con.num; i++)
		if (rel(con.elems[i], con.elems[i + 1] && !rel(con.elems[i + 1], con.elems[i])))
			contor++;
	return curent <= contor;
}

void IteratorColectie::urmator() {
	if (valid())
	{
		curent++;
		frecv = 1;
	}
}

void IteratorColectie::prim() {
	curent = 0;
	frecv = 1;
}

//void IteratorColectie::del(TElem e)
//{
//	int nr = con.nrAparitii(e);
//	while (con.sterge(e))
//	{
//		frecv--;
//	}
//	con.num -= nr;
//}