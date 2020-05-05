#include "IteratorColectie.h"



IteratorColectie::IteratorColectie(Colectie& c) : con(c) {
	// initializare curent si alte atribute specifice
	curent = 0;
	frecv = 1;
}
//O(n)
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
//theta(n)
bool IteratorColectie::valid() {
	if (con.vida())
		return false;
	int contor = 0;
	for (int i = 0; i < con.num - 1; i++)
		if (rel(con.elems[i], con.elems[i + 1]) && !rel(con.elems[i + 1], con.elems[i]))
			contor++;
	return curent <= contor;
}
//theta(1)
void IteratorColectie::urmator() {
	if (valid())
	{
		curent++;
		frecv = 1;
	}
}
//theta(1)
void IteratorColectie::prim() {
	curent = 0;
	frecv = 1;
}
//O(n) - mostenita de la sterge
bool IteratorColectie::del() { 
	bool ok = con.sterge(element());
	if (ok) {
		frecv--;
		urmator();
	}
	return ok;
}