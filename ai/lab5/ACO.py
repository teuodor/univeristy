from Lab5.Ant import Ant


class ACO:
    def __init__(self):
        self.__param = None
        self.__population = []

    def param(self, param):
        self.__param = param

    def population(self):
        return self.__population

    def set_population(self, population):
        self.__population = population

    def initialize(self):
        self.__population = []
        for i in range(self.__param['nr_pop']):
            ant = Ant()
            ant.param(self.__param)
            self.__population.append(ant)

    def best_ant(self):
        best = self.__population[0]
        for ant in self.__population:
            if ant.length() < best.length():
                best = ant
        return best

    def next_step(self):
        for ant in self.__population:
            current_city, next_city = ant.get_next_node()

    def final_step(self):
        for ant in self.__population:
            ant.return_start()
        for i in range(self.__param['nr_nodes']):
            for j in range(self.__param['nr_nodes']):
                pheromone = 0.0
                for ant in self.__population:
                    if ant.pheromone_path()[i][j] == 1:
                        pheromone += 1 / ant.length()
                evaporation = self.__param['evaporation']
                self.__param['pheromone_matrix'][i][j] = (1-evaporation) * self.__param['pheromone_matrix'][i][j] + pheromone

        return self.__param['pheromone_matrix']
