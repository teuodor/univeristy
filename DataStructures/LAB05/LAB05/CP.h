#pragma once
//CP.h
#include <utility>
#include <exception>

typedef int TElem;
typedef int TPrioritate;

typedef std::pair<TElem, TPrioritate> Element;

typedef bool(*Relatie)(TPrioritate, TPrioritate);

class CP {
private:
	/* aici e reprezentarea */
	Element *elems;
	Relatie rel;
	int dim, cap;

	void checkCap();

	void heapifyUp();

	void heapifyDown();

	int getParent(int);

	int getChild(int, int);


public:
	//constructorul implicit
	CP(Relatie r) : rel{ r } { 
		dim = 0;
		cap = 0;
	};

	//adauga un element in CP, avand o anumita pioritate
	void adauga(TElem e, TPrioritate p);

	//acceseaza elementul cel mai prioritar in raport cu relatia de ordine 
	//arunca exceptie daca CP e vida
	Element element()  const;

	//sterge elementul cel mai prioritar si il returneaza
	//arunca exceptie daca CP e vida
	Element sterge();

	//verifica daca CP e vida;
	bool vida() const;


	// destructorul cozii
	~CP();

};
