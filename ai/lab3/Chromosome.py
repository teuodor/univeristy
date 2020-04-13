from random import randint
from random import uniform
import numpy


class Chromosome:
    def _init_(self):
        self.__param = None
        self.__representation = None
        self.__fitness = 0.0

    def initialize(self):
        nr_leaders = self.__param['nr_nodes'] // 5

        self.__representation = [None for _ in range(self.__param['nr_nodes'])]
        for i in range(self.__param['nr_nodes']):
            if self.__representation[i] is None:
                self.__representation[i] = randint(1, self.__param['max_communities'])
                opp = self.__param['nr_nodes']
                if uniform(0, 1) <= nr_leaders / opp:
                    nr_leaders -= 1
                    indices = (self.__param['mat'][i] > 0).nonzero()[0]
                    for j in indices:
                        if self.__representation[j] is None:
                            self.__representation[j] = self.__representation[i]

    def representation(self):
        return self.__representation

    def fitness(self):
        return self.__fitness

    def set_representation(self, representation):
        if representation is None:
            representation = []

        self.__representation = representation

    def set_fitness(self, fitness=0.0):
        self.__fitness = fitness

    def param(self, param):
        self.__param = param

    def crossover(self, other):
        self.normalize()
        other.normalize()
        index = randint(0, len(self.__representation) - 1)
        community = self.__representation[index]
        new_representation = [x if x == community else y for x, y in zip(self.representation(), other.representation())]

        chromosome = Chromosome()
        chromosome.param(self.__param)
        chromosome.set_representation(new_representation)

        return chromosome

    def mutate(self):
        index = randint(0, len(self.__representation) - 1)
        unique = numpy.unique(self.__representation)
        x = numpy.random.choice(unique)
        self.__representation[index] = x

    def __str__(self):
        return "Chromosome: " + str(self.__param) + " " + str(self.__fitness)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__representation == other.representation()

    def normalize(self):
        communities = {}
        communities_nr = 0
        result = []
        for x in self.__representation:
            if x not in communities:
                communities_nr += 1
                communities[x] = communities_nr
            result.append(communities[x])

        self.__representation = result

    def no_communities(self):
        return numpy.unique(self.__representation).shape[0]
