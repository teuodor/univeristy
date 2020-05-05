#pragma once

#include<vector>


using namespace std;

//MDO.h

typedef int TCheie;
typedef int TValoare;

typedef std::pair<TCheie, TValoare> TElem;

typedef bool(*Relatie)(TCheie, TCheie);

class IteratorMDO;

class MDO {
	friend class IteratorMDO;
private:
	TElem* Elemente;
	int* urmator;
	int* Stanga;
	int* Dreapta;

	int radacina;//pozitia radacinii in vectorul Elemente
	int primLiber;

	int capacitate;
	int nrElemente;

	Relatie relatie;

	void resize();

public:

	// constructorul implicit al MultiDictionarului Ordonat
	MDO(Relatie r);

	// adauga o pereche (cheie, valoare) in MDO
	void adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza vectorul de valori asociate
	vector<TValoare> cauta(TCheie c) const;

	//sterge o cheie si o valoare 
	//returneaza adevarat daca s-a gasit cheia si valoarea de sters
	bool sterge(TCheie c, TValoare v);

	//returneaza numarul de perechi (cheie, valoare) din MDO 
	int dim() const;

	//verifica daca MultiDictionarul Ordonat e vid 
	bool vid() const;

	// se returneaza iterator pe MDO
	// iteratorul va returna perechile ordine dupa relatia de ordine
	IteratorMDO iterator() const;

	// destructorul 	
	//~MDO();

	/*
	Returneaza pozitia elementului minim incepand de la pozElement
	*/
	int Minim(int pozElement);

};
