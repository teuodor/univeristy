from random import randint

from Lab3.Chromosome import Chromosome


class GA:
    def __init__(self, param):
        self.__param = param
        self.__population = []

    def initialize(self):
        for _ in range(0, self.__param['nr_pop']):
            c = Chromosome()
            c.param(self.__param)
            c.initialize()
            self.__population.append(c)

    def evaluate(self):
        for c in self.__population:
            c.set_fitness(self.modularity(c.representation()))

    def best_chromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness() > best.fitness():
                best = c

        return best

    def worst_chromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if c.fitness() < worst.fitness():
                worst = c

        return worst

    def selection(self):
        pos1 = randint(0, self.__param['nr_pop'] - 1)
        pos2 = randint(0, self.__param['nr_pop'] - 1)
        if self.__population[pos1].fitness() > self.__population[pos2].fitness():
            return pos1
        else:
            return pos2

    def one_generation(self):
        new_population = []
        for _ in range(self.__param['nr_pop']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            son = p1.crossover(p2)
            son.mutate()
            new_population.append(son)

        self.__population = new_population
        self.evaluate()

    def one_generation_elitism(self):
        new_population = [self.best_chromosome()]
        for _ in range(self.__param['nr_pop'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            son = p1.crossover(p2)
            son.mutate()
            new_population.append(son)

        self.__population = new_population
        self.evaluate()

    def one_generation_steady_state(self):
        self.__population = sorted(self.__population, key=lambda x: x.fitness(), reverse=True)
        for _ in range(self.__param['nr_pop']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]

            son = p1.crossover(p2)
            son.mutate()
            son.set_fitness(self.modularity(son.representation()))
            if son.fitness() > self.__population[-1].fitness():
                self.__population[-1] = son

        self.evaluate()

    def modularity(self, representation):
        nr_nodes = self.__param['nr_nodes']
        mat = self.__param['mat']
        degrees = self.__param['degrees']
        nr_edges = self.__param['nr_edges']

        m = 2 * nr_edges
        q = 0.0
        for i in range(0, nr_nodes):
            for j in range(0, nr_nodes):
                if representation[i] == representation[j]:
                    q += (mat[i, j] - degrees[i] * degrees[j] / m)
        return q * 1 / m