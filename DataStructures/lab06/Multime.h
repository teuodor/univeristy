#pragma once

typedef int TElem;

class Multime {
	friend class IteratorMultime;

	private:
		TElem* elemente;
		int *nempty;
		int *deleted;
		int size, capacity;

		int hash1(int x) const {
			x = abs(x);
			while (x < 0) {
				x += capacity;
			}
			return x % capacity;
		}

		int hash2(int x) const{
			x = abs(x);
			return (1 + x % (capacity - 1));
		}

		int abs(int x) const {
			if (x < 0) {
				return -x;
			}

			return x;
		}

		void resizeIfNecesary() {
			if (((float)size) / capacity < 0.75) {
				return;
			}

			int _capacity = capacity;
			TElem *_elemente = elemente;
			int *_nempty = nempty;
			int *_deleted = deleted;

			capacity *= 5;

			elemente = new TElem[capacity];
			nempty = new int[capacity];
			deleted = new int[capacity];
			size = 0;

			for (int i = 0; i < capacity; i++) {
				elemente[i] = 0;
				nempty[i] = 0;
				deleted[i] = 0;
			}

			for (int i = 0; i < _capacity; i++) {
				if (_deleted[i] == 0 && _nempty[i] == 1) {
					adauga(_elemente[i]);
				}
			}

			//delete[] _elemente;
			//delete[] _nempty;
			//delete[] _deleted;
		}
		
	public:
		//constructorul implicit
		Multime() {
			size = 0;
			capacity = 3;

			elemente = new TElem[capacity];
			nempty = new int[capacity];
			deleted = new int[capacity];

			for (int i = 0; i < capacity; i++) {
				elemente[i] = 0;
				nempty[i] = 0;
				deleted[i] = 0;
			}
		}

		Multime(const Multime &m) {
			capacity = m.capacity;
			size = m.size;

			elemente = new TElem[capacity];
			nempty = new int[capacity];
			deleted = new int[capacity];

			for (int i = 0; i < capacity; i++) {
				elemente[i] = m.elemente[i];
				nempty[i] = m.nempty[i];
				deleted[i] = m.deleted[i];
			}
		}

		//adauga un element in multime
		//returneaza adevarat daca elementul a fost adaugat (nu exista deja in multime)
		bool adauga(TElem e) {
			resizeIfNecesary();

			for (int i = 0; i < capacity; i++) {
				int poz = (hash1(e) + i * hash2(e)) % capacity;
				if (elemente[poz] == e && deleted[poz] == 0 && nempty[poz] == 1) {
					return false;
				}
				else if (deleted[poz] == 1 || nempty[poz] == 0) {
					elemente[poz] = e;
					deleted[poz] = 0;
					nempty[poz] = 1;
					size++;
					return true;
				}
			}

			return false;
		}

		//sterge un element din multime
		//returneaza adevarat daca elementul a existat si a fost sters
		bool sterge(TElem e) {
			for (int i = 0; i < capacity; i++) {
				int poz = (hash1(e) + i * hash2(e)) % capacity;

				if (deleted[poz] == 0 && nempty[poz] == 0) {
					return false;
				}
				else if (elemente[poz] == e && deleted[poz] == 0) {
					deleted[poz] = 1;
					nempty[poz] = 0;
					size--;
					return true;
				}
			}
			return false;
		}

		//verifica daca un element se afla in multime
		bool cauta(TElem elem) const {
			for (int i = 0; i < capacity; i++) {
				int poz = (hash1(elem) + i * hash2(elem)) % capacity;

				if (deleted[poz] == 0 && nempty[poz] == 0) {
					return false;
				}
				else if (elemente[poz] == elem) {
					return true;
				}
			}
			return false;
		}

		//intoarce numarul de elemente din multime;
		int dim() const {
			return size;
		}

		//verifica daca multimea e vida;
		bool vida() const {
			return size == 0;
		}

		//returneaza un iterator pe multime
		IteratorMultime iterator() const;

		// destructorul multimii
		~Multime() {
			delete[] elemente;
			delete[] nempty;
			delete[] deleted;
		}

};
