#pragma once
//Colectie.h

typedef int TElem;

class Colectie {

	friend class IteratorColectie;

private:
	/* aici e reprezentarea */
	TElem *elemente;
	int *notEmpty;
	int *deleted;
	int size, capacity;
	
	int hash1(int x) const {
		x = abs(x);
		return x % capacity;
	}
	int hash2(int x) const {
		x = abs(x);
		return(1 + x % (capacity - 1));
	}
	int abs(int x) const {
		if (x < 0)
			return -x;
		return x;
	}
	void resize() {
		if (((float)size) / capacity < 0.75)
			return;

		int capx = capacity;
		TElem *elemx = elemente;
		int *emptx = notEmpty;
		int *delx = deleted;

		capacity *= 131;

		elemente = new TElem[capacity];
		notEmpty = new int[capacity];
		deleted = new int[capacity];
		size = 0;

		for (int i = 0; i < capacity; i++) {
			elemente[i] = 0;
			notEmpty[i] = 0;
			deleted[i] = 0;
		}

		for (int i = 0; i < capx; i++)
			if (delx[i] == 0 && emptx[i] == 1) {
				adauga(elemx[i]);
			}
	}
public:
	//constructorul implicit
	Colectie();

	Colectie(const Colectie &col);
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

	//returneaza un iterator pe colectie
	IteratorColectie iterator() const;

	// destructorul colectiei
	~Colectie();

};