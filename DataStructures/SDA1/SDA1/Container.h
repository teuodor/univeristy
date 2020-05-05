#pragma once


typedef int TElem;

//alte definitii daca e cazul (relatie, elemente nule)

class IteratorContainer;

class Container {

	friend class IteratorContainer;

private:
	//aici reprezentarea containerului
	int* elems ;
	int lungime;
	int capacitate;
	int minim;
	int maxim;


public:
	//constructorul implicit
	Container();
	

	//aici operatiile specifice

	//realizeaza redimensionarea vectorului
	void redimensionare();

	//adauga un element in colectie
	void adauga(TElem e);

	//sterge o aparitie a unui element din colectie
	//returneaza adevarat daca s-a putut sterge
	bool sterge(TElem e);

	//verifica daca un element se afla in colectie
	bool cauta(TElem elem) const;

	//returneaza numar de aparitii ale unui element in colectie
	int nrAparitii(TElem elem) const;


	//intoarce numarul de elemente din colectie;
	int dim() const;

	//verifica daca colectia e vida;
	bool vida() const;


	//returneaza un iterator pe container
	IteratorContainer iterator() const;

	

	int getMIN() const;
	int getMAX() const;
	int getLUN() const;

	// destructor
	~Container();

};


//adauga_incercare
/*
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
				for (i = 5; i >= 1; i--)
					elems[i] = 0;
				elems[0] = 1;
				elems[minim - e] = frecvMin;
				minim = e;
				lungime = minim - e + 1;
			}
}


else
if (e == minim)
elems[0]++;
else
if (e > maxim) {
	int frecvMaxim = elems[maxim - minim];
	int pozitie = maxim - minim;
	if (e - minim + 1 >= capacitate) {
		for (int i = pozitie + 1; i < capacitate; i++)
			elems[i] = 0;
		elems = new TElem[capacitate];
		for (int j = capacitate; j < e - minim; j++)
			elems[j] = 0;
		elems[e - minim] = 1;
		lungime = maxim - minim + 1;
	}
	else {
		for (int i = pozitie + 1; i < e - minim; i++)
			elems[i] = 0;
		elems[e - minim] = 1;
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
if (maxim - e + 1 >= capacitate) {
	elems = new TElem[capacitate];
	int nrPoz = minim - e;
	for (int i = maxim - e; i >= nrPoz; i--)
		elems[i] = elems[i - nrPoz];
	for (int j = nrPoz - 1; j >= 1; j--)
		elems[j] = 0;
	elems[1] = 1;
	minim = e;
	lungime += nrPoz;
}
}*/