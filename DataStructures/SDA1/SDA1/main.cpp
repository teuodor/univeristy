#include <iostream>
#include "Container.h"
#include "IteratorContainer.h"
#include "testScurt.h"
#include "testExtins.h"
using namespace std;


int main() {

	testAll();
	testAllExtins();
	Container c;
	// iterare
	IteratorContainer ic = c.iterator();
	while (ic.valid()) {
		TElem e = ic.element();
		// prelucrare element
		ic.urmator();
	}

	cout << "End";


}