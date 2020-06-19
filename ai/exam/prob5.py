from sklearn.cluster import KMeans
import numpy as np

training_x = []


def load_data():
    f = open("wine.txt", 'r')
    line = f.readline()
    tmp = 0
    alcohol_mean = 0
    while line != "":
        if tmp > 0:
            split = line.split(",")
            inside_x = []
            for i in range(len(split)):
                inside_x.append(float(split[i]))
                if i == len(split) - 1:
                    alcohol_mean += float(split[i])
            training_x.append(inside_x)
        tmp += 1
        line = f.readline()
    alcohol_mean /= len(training_x)
    density_mean = 0
    density_nr = 0
    for i in range(len(training_x)):
        if training_x[i][-1] > alcohol_mean:
            density_nr += 1
            density_mean += training_x[i][-4]
    print("Problema A, Densitatea medie: " + str(density_mean / density_nr))


load_data()


def kmeans_tool():
    k_means = KMeans(n_clusters=5, random_state=0)
    k_means.fit(training_x)
    new_wine = [[8.1, 0.545, 0.18, 1.9, 0.08, 13, 35, 0.9972, 3.3, 0.59, 9.8]]
    print("Problema B: " + str(k_means.predict(new_wine)))

    wine_means = [0] * len(training_x[0])
    for i in range(len(training_x)):
        for j in range(len(training_x[i])):
            wine_means[j] += training_x[i][j]

    for i in range(len(wine_means)):
        wine_means[i] /= len(training_x)

    wine_means[0] = 7.9
    wine_means[3] = 1.8
    wine_means[-4] = 0.9969
    wine_means[-3] = 3.04
    wine_means[-1] = 9.8

    print("Problema C: " + str(k_means.predict([wine_means])))


kmeans_tool()

# Rezultate:
# Problema A, Densitatea medie: 0.996435
# Problema B: [4]
# Problema C: [0]
