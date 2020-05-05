import matplotlib.pyplot as plot
import networkx as nx
import numpy as np

from Lab4.GA import GA

file_names = ['easy1', 'easy2', 'easy3', 'easy_01_tsp', 'mediumF']


def run():
    file_name = file_names[4]
    nr_pop = 100
    nr_gen = 3000
    generation_type = 'steady'

    run_test(file_name, generation_type, nr_pop, nr_gen)


def read(file_name):
    f = open(file_name, 'r')
    n = int(f.readline())

    g = nx.MultiDiGraph()

    for i in range(n):
        weights = [int(k) for k in f.readline().strip().split(',')]
        for j in range(len(weights)):
            g.add_edge(i, j, weight=weights[j])

    return g


def run_test(file_name, generation_type, nr_pop, nr_gen):
    g = read('real/' + file_name+'.txt')
    param ={
        'nr_nodes': g.number_of_nodes(),
        'mat': g,
        'nr_edges': g.number_of_edges(),
        'nr_pop': nr_pop,
        'nr_gen': nr_gen,
        'max_communities': g.number_of_nodes()
    }

    ga = GA(param)
    ga.initialize()
    ga.evaluate()

    best_chromosome = ga.best_chromosome()
    last_fitness = 0
    same_fitness = 1
    for i in range(param['nr_gen']):
        best_chromosome = ga.best_chromosome()
        if last_fitness == best_chromosome.fitness():
            if same_fitness == 3000:
                break
            else:
                same_fitness += 1
        else:
            same_fitness = 1
            last_fitness = best_chromosome.fitness()
        print('Best chromosome of generation ' + str(i + 1) + ' : ' + str(best_chromosome.fitness()))

        if generation_type == 'normal':
            ga.one_generation()
        elif generation_type == 'elitism':
            ga.one_generation_elitism()
        elif generation_type == 'steady':
            ga.one_generation_steady_state()

    write_solution_to_file(file_name, best_chromosome, generation_type)
    #draw_result(file_name, best_chromosome, param, generation_type)


def write_solution_to_file(file_name, best_chromosome, generation_type):
    with (open('output/' + file_name + '_' + generation_type + '_result.txt', 'w')) as fopen:
        fopen.write('Fitness of best chromosome: ' + str(
            best_chromosome.fitness()) + '\n')

        for i in range(len(best_chromosome.representation())):
            fopen.write(str(i) + " - " + str(best_chromosome.representation()[i]) + '\n')


run()

