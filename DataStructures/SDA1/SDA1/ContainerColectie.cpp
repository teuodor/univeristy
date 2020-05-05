#include "Container.h"
#include "iteratorContainer.h"
#include <iostream>

//constructorul implicit
Container::Container() {
	capacitate = 10;
	elems = new TElem[capacitate];
	lungime = 0;
}

//aici operatiile specifice

//realizeaza redimensionarea vectorului
void Container::redimensionare(){
	int* elemsNou = new TElem[capacitate*2];
	for (int i = 0; i < lungime; i++)
		elemsNou[i] = elems[i];
	elems = elemsNou;
	capacitate += 10;
}

//adauga un element in colectie
void Container::adauga(TElem e) {
	if (lungime == 0) {
		maxim = e;
		minim = e;
		elems[0] = 1;
		lungime++;
	}
	else
		if (lungime == 1) {
			if (e == maxim)
				elems[0]++;
			else
				if (e > maxim) {
					for (int i = 1; i < e - minim; i++)
						elems[i] = 0;
					elems[e - minim] = 1;
					maxim = e;
					lungime = e - minim + 1;
				}

				else
					if (e < minim) {
						int frecvMin = elems[0];
						int i = 0;
						for (i = minim - e - 1; i >= 1; i--)
							elems[i] = 0;
						elems[0] = 1;
						elems[minim - e] = frecvMin;
						lungime = minim - e + 1;
						minim = e;
					}

		}

		else
						if (e == minim)
							elems[0]++;
						else
							if (e > maxim) {
								int frecvMaxim = elems[maxim - minim];
								int pozitie = maxim - minim;
								if (e - minim + 1 > capacitate) {
									for (int i = pozitie + 1; i < capacitate; i++)
										elems[i] = 0;
									redimensionare();
									for (int j = capacitate; j < e - minim; j++)
										elems[j] = 0;
									elems[e - minim] = 1;
									elems[pozitie] = frecvMaxim;
									maxim = e;
									lungime = maxim - minim + 1;
								}
								else {
									for (int i = pozitie + 1; i < e - minim; i++)
										elems[i] = 0;
									elems[e - minim] = 1;
									maxim = e;
									lungime = maxim - minim + 1;
								}

							}
							else
								if (e == maxim)
									elems[maxim - minim]++;
								else
									if (e<maxim and e>minim)
										elems[e - minim]++;
									else
										if (minim - e + 1 > capacitate) {
											redimensionare();
											int nrPoz = minim - e;
											int* aux = new TElem[lungime];
											for (int x = 0; x < lungime; x++)
												aux[x] = elems[x];
											for (int x = 0; x < lungime; x++)
												elems[x] = 0;

											for (int i = minim - e; i <= maxim - e; i++)
												elems[i] = aux[i - minim + e];
											for (int j = nrPoz - 1; j >= 1; j--)
												elems[j] = 0;
											elems[0] = 1;
											minim = e;
											lungime += nrPoz;
											delete(aux);
										}
										else {
											int nrPoz = minim - e;
											int* aux = new TElem[lungime];
											for (int x = 0; x < lungime; x++)
												aux[x] = elems[x];
											for (int x = 0; x < lungime; x++)
												elems[x] = 0;

											for (int i = minim - e; i <= maxim - e; i++)
												elems[i] = aux[i-minim+e];
											for (int j = nrPoz - 1; j >= 1; j--)
												elems[j] = 0;
											elems[0] = 1;
											minim = e;
											lungime += nrPoz;
											delete(aux);
                                        }
		}



//sterge o aparitie a unui element din colectie
//returneaza adevarat daca s-a putut sterge
bool Container::sterge(TElem e) {
	if (vida())
		return false;
	if (e > maxim or e < minim )
		return false;
	if (elems[e - minim] < 1)
		return false;
	else{
		elems[e - minim]--;
		return true;
	}
}

//verifica daca un element se afla in colectie
bool Container::cauta(TElem elem) const {
	if (vida())
		return false;
	if (elem <= maxim and elem >= minim and elems[elem - minim] != 0)
		return true;
	return false;
}


//returneaza numar de aparitii ale unui element in colectie
int Container::nrAparitii(TElem elem) const {
	//if (elem<minim or elem>maxim)
		//return 0;
	if (vida())
		return 0;
	return elems[elem - minim];
}

//intoarce numarul de elemente din colectie;
int Container::dim() const {
	int nrElem = 0;
	if (vida())
		return 0;
	for (int i = 0; i <= maxim-minim; i++)
		nrElem += elems[i];
	return nrElem;
}

//verifica daca colectia e vida;
bool Container::vida() const {
	if (lungime == 0)
		return true;
	return false;
}

//returneaza un iterator pe container
IteratorContainer Container::iterator() const {
	return IteratorContainer::IteratorContainer(*this);
}

 int Container::getMIN() const {
	 return minim;
}
 int Container::getMAX() const {
	 return maxim;
 }
 int Container::getLUN() const {
	 return lungime;
 }

// destructor
Container::~Container() {
	delete(elems);
}