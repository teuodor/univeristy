import matplotlib.pyplot as plot
import networkx as nx
import numpy as np

from Lab3.Chromosome import Chromosome
from Lab3.GA import GA


file_names = ['dolphins', 'football', 'karate', 'krebs']


def run():
    file_name = file_names[3]
    nr_pop = 250
    nr_gen = 1000
    generation_type = 'normal'

    run_test(file_name, generation_type, nr_pop, nr_gen)


def normalize_communities(representation):
    communities_dict = {}
    communities_number = 0
    result = []
    for x in representation:
        if x not in communities_dict:
            communities_number += 1
            communities_dict[x] = communities_number
        result.append(communities_dict[x])

    return result


def write_solution_to_file(file_name, best_chromosome, generation_type):
    with (open('real/' + file_name + '/' + file_name + '_' + generation_type + '_result.txt', 'w')) as fopen:
        fopen.write('Number of communities of best chromosome ' + str(
            len(best_chromosome.no_communities())) + '\nFitness of best chromosome: ' + str(
            best_chromosome.fitness()) + '\n')

        data = normalize_communities(best_chromosome.representation())

        for i in range(len(data)):
            fopen.write(str(i) + " | " + str(data[i]) + '\n')


def draw_result(file_name, best_chromosome, param, generation_type):
    A = np.matrix(param['mat'])
    G = nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)
    plot.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_size=600, node_color=best_chromosome.representation())
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plot.savefig('real/' + file_name + '/' + file_name + '_' + generation_type + '_plot.png')
    plot.clf()


def run_test(file_name, generation_type, nr_pop, nr_gen):
    G = nx.read_gml('real/' + file_name + '/' + file_name + '.gml', label='id')

    param ={
        'nr_nodes': G.number_of_nodes(),
        'mat': nx.to_numpy_array(G),
        'degrees': [x[1] for x in G.degree()],
        'nr_edges': G.number_of_edges(),
        'nr_pop': nr_pop,
        'nr_gen': nr_gen,
        'max_communities': G.number_of_nodes()
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
            if same_fitness == 100:
                break
            else:
                same_fitness += 1
        else:
            same_fitness = 1
            last_fitness = best_chromosome.fitness()
        print('Best chromosome of generation ' + str(i + 1) + ' : ' + str(best_chromosome.fitness()) + ' '
              + ' and ' + str(best_chromosome.no_communities()))

        if generation_type == 'normal':
            ga.one_generation()
        elif generation_type == 'elitism':
            ga.one_generation_elitism()
        elif generation_type == 'steady':
            ga.one_generation_steady_state()

    write_solution_to_file(file_name, best_chromosome, generation_type)
    draw_result(file_name, best_chromosome, param, generation_type)


run()
