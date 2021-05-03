import copy
import math
import time
import os
import random
import sys


def anneal(temp, cool_rate, coordinates, distance_matrix, start_time, time_limit):
    tour = random.sample(range(0, len(coordinates)), len(coordinates))
    while temp > 1:
        if time.perf_counter() - start_time > time_limit:
            return tour
        [i, j] = sorted(random.sample(range(len(coordinates)), 2))
        new_tour = tour[:i] + tour[j:j + 1] + tour[i + 1:j] + tour[i:i + 1] + tour[j + 1:]
        # Calculate the distances of the current tour and the new tour
        old_distances = sum(
            distance_matrix[tour[(k + 1) % len(coordinates)]][tour[k % len(coordinates)]] for k in
            [j, j - 1, i, i - 1])
        new_distances = sum(
            distance_matrix[new_tour[(k + 1) % len(coordinates)]][new_tour[k % len(coordinates)]] for k in
            [j, j - 1, i, i - 1])
        # Probability of taking a new tour in order to bypass local minimums
        try:
            exponent = math.exp((old_distances - new_distances) / temp)
        except OverflowError:
            exponent = math.inf
        if exponent > random.random():
            tour = copy.copy(new_tour)
        temp *= abs(1 - cool_rate)
    return tour


# distance formula helper method
def distance_helper(x1, y1, x2, y2):
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return round(distance)


def get_path(tour, coordinates):
    path = []
    for i in range(len(tour)):
        path.append(coordinates[tour[i]])
    return path


def get_path_len(tour, distance_mat):
    return sum(distance_mat[tour[(k + 1) % len(distance_mat)]][tour[k % len(distance_mat)]] for k in
               range(0, len(distance_mat)))


def main():
    start_time = time.perf_counter()
    try:
        in_file = str(sys.argv[1]).strip()
        out_file = str(sys.argv[2]).strip()
        time_limit = int(str(sys.argv[3]).strip())
    except IndexError:
        print("Must have 3 args: <input-coordinates.txt> <output-tour.txt> <time>")
        sys.exit(2)
    out_file = open(out_file, "w")


    # Loads each line in from the specified coordinates file and converts them into floats as X and Y coordinates.
    # The resulting coordinates are stored in the coords list.
    coords = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.strip() == in_file:
            with open(in_file, 'r') as in_stream:
                while True:
                    line = in_stream.readline().strip("\n").split(' ')
                    if len(line) >= 3:
                        coords.append((float(line[1]), float(line[2])))
                    else:
                        break

    # Create nxn array for all distances between each coordinate O(n^2) time
    # Iterates through coords list and calculates distance from each node to each other node and stores it in dist_mat.
    # The matrix is set up in such a way that the X-axis is the distance from the first node in each row to each other
    # node in the coordinate list. EX. The last element in the dist_mat is the distance from the last coord to itself.
    dist_mat = []
    for i in range(0, len(coords)):
        row = []
        for j in range(0, len(coords)):
            row.append(distance_helper(coords[i][0], coords[i][1], coords[j][0], coords[j][1]))
        dist_mat.append(row)

    coolingrate = 0.00001
    temperature = 10000
    for i in range(0, 1):
        tour = anneal(temperature, coolingrate, coords, dist_mat, start_time, time_limit)
        out_file.write("\nTotal Cost: " + str(get_path_len(tour, dist_mat)) + "\n")
        out_file.write("Tour: \n")
        for j in range(len(tour) + 1):
            out_file.write(str(tour[j % len(tour)] + 1) + " ")
    out_file.close()

    exit(2)
if __name__ == "__main__":
    main()
