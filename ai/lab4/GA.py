from random import randint

from Lab4.Chromosome import Chromosome


class GA:
    def __init__(self, param):
        self.__param = param
        self.__population = []

    def initialize(self):
        for _ in range(0, self.__param['nr_pop']):
            c = Chromosome()
            c.param(self.__param)
            self.__population.append(c)

    def evaluate(self):
        for c in self.__population:
            c.set_fitness(self.modularity(c.representation()))

    def best_chromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness() < best.fitness():
                best = c

        return best

    def worst_chromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if c.fitness() > worst.fitness():
                worst = c

        return worst

    def selection(self):
        pos1 = randint(0, self.__param['nr_pop'] - 1)
        pos2 = randint(0, self.__param['nr_pop'] - 1)
        if self.__population[pos1].fitness() < self.__population[pos2].fitness():
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
            if son.fitness() < self.__population[-1].fitness():
                self.__population[-1] = son

        self.evaluate()

    def modularity(self, representation):
        cost = self.__param['mat'][representation[0]][representation[1]][0]['weight']
        current = representation[0]

        for i in range(1, len(representation)):
            cost += self.__param['mat'][current][representation[i]][0]['weight']
            current = representation[i]

        return cost
