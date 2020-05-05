from Lab5.ACO import ACO
import matplotlib.pyplot as plot

file_names = ['easy1', 'easy2', 'easy3', 'easy_01_tsp', 'mediumF']


def run():
    file_name = file_names[4]
    nr_pop = 200
    nr_gen = 500
    run_test(file_name, nr_pop, nr_gen, 3, 2, 0.7, 0.1, 'red')


def run_test(file_name, nr_pop, nr_gen, alpha, beta, quantifier, evaporation, color):
    matrix = read_tsp_matrix(file_name)
    param = {
        'nr_pop': nr_pop,
        'nr_gen': nr_gen,
        'alpha': alpha,
        'beta': beta,
        'quantifier': quantifier,
        'evaporation': evaporation,
        'matrix': matrix,
        'nr_nodes': len(matrix[0])
    }

    param['pheromone_matrix'] = create_pheromone_matrix(param['nr_nodes'])

    aco = ACO()
    aco.param(param)
    best_ants = []
    for generation in range(nr_gen):
        aco.initialize()
        for i in range(len(matrix[0]) - 1):
            aco.next_step()
        param["pheromone_matrix"] = aco.final_step()
        best_ants.append(aco.best_ant().length())
        print("Evolutie " + str(generation) + " : " + str(aco.best_ant().length()))

    write_to_file(file_name, aco.best_ant())

    draw_result(file_name, best_ants, color)


def create_pheromone_matrix(nr_nodes):
    result = []
    for i in range(nr_nodes):
        result.append([1 for i in range(nr_nodes)])
    return result


def read_tsp_matrix(file_name):
    result = []

    f = open('real/' + file_name + '.txt', 'r')
    n = int(f.readline())
    for i in range(n):
        weights = f.readline().strip().split(',')
        new_weights = []
        for j in range(len(weights)):
            new_weights.append(float(weights[j]))
        result.append(new_weights)

    return result


def write_to_file(file_name, best_ant):
    output = 'output/' + file_name + '_out.txt'
    with(open(output, 'w')) as f:
        f.write("Best ant path : \n" + str(best_ant.length()))
        for i in range(len(best_ant.path())):
            f.write(str(i) + " - " + str(best_ant.path()[i]) + '\n')


def draw_result(file_name, best_ants, color):
    plot.ylabel('Best_ants')
    plot.plot(best_ants, color)
    plot.savefig('output/' + file_name + '_out_plot.png')
    plot.clf()


run()
