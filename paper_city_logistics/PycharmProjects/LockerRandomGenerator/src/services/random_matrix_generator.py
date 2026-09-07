import random

from src.config.config import Config
from src.services.utils import read_probability_csv


def generate_random_matrix(columns):
    rows = Config.TOTAL_SCENARIOS
    return [[random.randint(0, 2) for i in range(columns)] for j in range(rows)]


def substitute_matrix_values(random_matrix, probabilities):
    substituted_matrix = []
    for i, row in enumerate(random_matrix):
        substituted_row = []
        for j, value in enumerate(row):
            substituted_value = probabilities[j][value]
            substituted_row.append(substituted_value)
        substituted_matrix.append(substituted_row)
    return substituted_matrix


def create_initial_solution(input_file_path):
    clients_probabilities = read_probability_csv(input_file_path)
    random_matrix = generate_random_matrix(len(clients_probabilities))
    substituted_matrix = substitute_matrix_values(random_matrix, clients_probabilities)
    return substituted_matrix
