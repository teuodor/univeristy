#include "MDO.h"

void MDO::resize()
{
	if (capacitate > nrElemente)
		return;

	TElem* ElementeNoi = new TElem[capacitate * 2];
	int* StangaNou = new int[capacitate * 2];
	int* DreaptaNou = new int[capacitate * 2];
	int * urmatorNou = new int[capacitate * 2];

	for (int i = 0; i < capacitate; i++)
	{
		ElementeNoi[i] = Elemente[i];
		DreaptaNou[i] = Dreapta[i];
		StangaNou[i] = Stanga[i];
		urmatorNou[i] = urmator[i];
	}

	for (int i = capacitate; i < capacitate * 2; i++)
	{
		DreaptaNou[i] = -1;
		StangaNou[i] = -1;
		urmatorNou[i] = i + 1;
	}

	primLiber = capacitate;

	capacitate *= 2;

	delete[] Elemente;
	delete[] Stanga;
	delete[] Dreapta;
	delete[] urmator;

	Elemente = ElementeNoi;
	Stanga = StangaNou;
	Dreapta = DreaptaNou;
	urmator = urmatorNou;

}

MDO::MDO(Relatie r)
{
	Stanga = new int[50];
	Dreapta = new int[50];
	Elemente = new TElem[50];
	urmator = new int[50];

	for (int i = 0; i < 50; i++)
	{
		Stanga[i] = -1;
		Dreapta[i] = -1;
		urmator[i] = i + 1;
	}

	urmator[49] = -1;

	primLiber = 0;
	radacina = -1;

	capacitate = 50;
	nrElemente = 0;

	relatie = r;
}

void MDO::adauga(TCheie c, TValoare v)
{
	TElem pereche = make_pair(c, v);

	resize();

	if (radacina == -1)//daca nu exista elemente in arbore
	{
		radacina = primLiber;
		primLiber = urmator[primLiber];
		Elemente[radacina] = pereche;
	}
	else
	{
		int rad = Elemente[radacina].first;//cheia radacinii
		int poz = radacina;//pozitia radacinii
		while (true)
		{
			if (relatie(c, rad))//daca  se indeplineste relatia
			{
				if (Stanga[poz] != -1)//daca exista ramura stanga
				{
					poz = Stanga[poz];
					rad = Elemente[poz].first;
				}
				else//daca nu exista ramura stanga
				{
					Elemente[primLiber] = pereche;
					Stanga[poz] = primLiber;
					primLiber = urmator[primLiber];
					break;
				}
			}
			else//daca nu se indeplineste relatia
			{
				if (Dreapta[poz] != -1)//daca exsita ramura dreapta
				{
					poz = Dreapta[poz];
					rad = Elemente[poz].first;
				}
				else//daca nu exista ramura dreapta
				{
					Elemente[primLiber] = pereche;
					Dreapta[poz] = primLiber;
					primLiber = urmator[primLiber];
					break;
				}
			}
		}
	}
	nrElemente++;
}

vector<TValoare> MDO::cauta(TCheie c) const
{
	int pozAux = radacina;
	int nr = nrElemente;
	vector<TValoare> v;
	while (nr) //sa ajungem la coada
	{
		if (Elemente[pozAux].first == c)
			v.push_back(Elemente[pozAux].second);
		pozAux = urmator[pozAux];
		nr--;
	}
	return v;
}

bool MDO::sterge(TCheie c, TValoare v)
{
	int rad = Elemente[radacina].first;//cheia radacinii
	int poz = radacina;//pozitia radacinii
	int pozAnterioara = poz;//pozitia elementului anterior
	int st = 0;//ramura stanga 
	int dr = 0;//ramura dreapta

	while (true)
	{
		if (relatie(c, rad))//daca  se indeplineste relatia
		{
			if (Elemente[poz].first == c && Elemente[poz].second == v)//daca am gasit perechea
			{
				break;
			}
			else if (Stanga[poz] != -1)//daca exista ramura stanga
				{

					pozAnterioara = poz;
					poz = Stanga[poz];
					rad = Elemente[poz].first;
					st = 1;
					dr = 0;
				}
			else return false;
		}
		else if(relatie(c,rad) == false)//daca nu se indeplineste relatia
		{
			if (Elemente[poz].first == c && Elemente[poz].second == v)//daca am gasit perechea
			{
				break;
			}
			else if (Dreapta[poz] != -1)//daca exsita ramura dreapta
				{	
					pozAnterioara = poz;
					poz = Dreapta[poz];
					rad = Elemente[poz].first;
				
					st = 0;
					dr = 1;

				}
			else return false;
		}
		
	}

	if (Stanga[poz] == -1 && Dreapta[poz] == -1)
	{
			
		if (st)
			Stanga[pozAnterioara] = -1;
		if (dr)
			Dreapta[pozAnterioara] = -1;

		urmator[poz] = primLiber;
		primLiber = poz;

		nrElemente--;
		return true;
	}
	else if(Stanga[poz] != -1 && Dreapta[poz] == -1)
	{
		if (st == 0 && dr == 0)
		{
			radacina = Stanga[poz];
			Stanga[poz] = -1;
		}
		if (st)
		{
			Stanga[pozAnterioara] = Stanga[poz];
			Stanga[poz] = -1;
		}
		if (dr)
		{
			Dreapta[pozAnterioara] = Stanga[poz];
			Stanga[poz] = -1;
		}

		urmator[poz] = primLiber;
		primLiber = poz;

		nrElemente--;
		return true;
	}

	else if (Stanga[poz] == -1 && Dreapta[poz] != -1)
	{
		if (st)
		{
			Stanga[pozAnterioara] = Dreapta[poz];
			Dreapta[poz] = -1;
		}
		if (dr)
		{
			Dreapta[pozAnterioara] = Dreapta[poz];
			Dreapta[poz] = -1;
		}

		urmator[poz] = primLiber;
		primLiber = poz;

		nrElemente--;
		return true;
	}

	else if (Stanga[poz] != -1 && Dreapta[poz] != -1)
	{
		int pozitieMinim = Minim(Dreapta[poz]);

		Elemente[poz] = Elemente[pozitieMinim];

		//sterge(Elemente[pozitieMinim].first, Elemente[pozitieMinim].second);

		Dreapta[poz] = Dreapta[pozitieMinim];

		Dreapta[pozitieMinim] = -1;

		nrElemente--;
		urmator[pozitieMinim] = primLiber;
		primLiber = pozitieMinim;
		return true;
	}
}
/*
Returneaza pozitia elementului minim incepand de la pozElement 
*/
int MDO::Minim(int pozElement)
{
	int min = Elemente[pozElement].first;

	while (true)
	{
		if (Stanga[pozElement] != -1)
		{
			pozElement = Stanga[pozElement];
			if (Elemente[pozElement].first < min)
				min = Elemente[pozElement].first;
		}
		else
			break;
	}

	return pozElement;
}

int MDO::dim() const
{
	return nrElemente;
}

bool MDO::vid() const
{
	if (dim() == 0)
		return true;
	return false;
}


