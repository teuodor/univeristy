#pragma once
#include<utility>
#define VECTOR_INIT_SIZE 2
class TElem{
public:
	int elem;
	int frecv;
};
class VectorDinamic {
private:
	int num;
	int sz;

/*
	The function frees the memory of a VectorDinamic entity	
	The function enlarge the size of a VectorDinamic entity
	:param: a VectorDinamic entity
*/
	void checkCapacity();
public:
	TElem *elems;
	VectorDinamic() {
		num = 0;
		sz = VECTOR_INIT_SIZE;
		elems = new TElem[sz];
	}

	int searchV(int e) const;

	/*
	The function adds a new element
	:param: a VectorDinamic entity
	:param Telem: the new element
	*/
	void addV(TElem);

	/*
	The function deletes an element 
	:param int: the position of the element
	*/
	bool delV(TElem);
	/*
	The function deletes an element after its position
	:param: a VectorDinamic entity
	:param int: the position
	*/
	int getLength() const;

	TElem firstElem() const ;
	~VectorDinamic(){
		delete elems;
	}
};