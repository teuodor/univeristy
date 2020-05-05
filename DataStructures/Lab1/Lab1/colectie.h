//Colectie.h

typedef int TElem;

class Colectie {
private:
	/* aici e reprezentarea*/
public:
	Colectie();

		void adauga(TElem e);

		bool sterge(TElem e);

		bool cauta(TElem e) const;

		int nr_aparitii(TElem e) const;


		int dim() const;

		bool vida() const;


		IteratorColectie iterator() const;

		~Colectie();
};
