import csv


def read_probability_csv(file_path):
    probabilities = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header
        for row in reader:
            probabilities.append((float(row[1].strip()), float(row[2].strip()), float(row[3].strip())))
    return probabilities


def write_matrix_to_csv(matrix, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in matrix:
            writer.writerow(row)


def read_matrix_to_csv(file_path):
    matrix = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            matrix.append([float(value) for value in row])
    return matrix


def create_probability_lookup(probabilities):
    lookup = []
    for row in probabilities:
        lookup.append({float(value): index for index, value in enumerate(row)})
    return lookup


def substitute_values_with_indices(final_solution, lookup):
    indexed_solution = []
    for row in final_solution:
        indexed_row = [lookup[j][float(value)] for j, value in enumerate(row)]
        indexed_solution.append(indexed_row)
    return indexed_solution
