import os

from src.config.config import Config
from src.services.matrix_optimizer import optimize_matrix
from src.services.random_matrix_generator import create_initial_solution
from src.services.solution_tester import sum_of_row_products
from src.services.utils import write_matrix_to_csv, read_matrix_to_csv, read_probability_csv, create_probability_lookup, \
    substitute_values_with_indices


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(base_dir, 'data\\clients_probabilities.csv')
    initial_solution_file_path = os.path.join(base_dir, 'output\\initial_solution.csv')
    partial_solution_file_path = os.path.join(base_dir, 'output\\partial_solution.csv')
    final_solution_file_path = os.path.join(base_dir, 'output\\final_solution.csv')
    final_indexed_solution_file_path = os.path.join(base_dir, 'output\\final_indexed_solution.csv')

    initial_matrix = create_initial_solution(input_file_path)
    probabilities = read_probability_csv(input_file_path)
    write_matrix_to_csv(initial_matrix, initial_solution_file_path)
    result = sum_of_row_products(initial_solution_file_path)

    if result >= Config.TARGET_VALUE:
        write_matrix_to_csv(initial_matrix, final_solution_file_path)
        print(f'Target value: {Config.TARGET_VALUE}')
        print(f'Result: {result}')

    while result < Config.TARGET_VALUE:
        optimized_matrix = optimize_matrix(initial_matrix, probabilities)
        write_matrix_to_csv(optimized_matrix, partial_solution_file_path)
        result = sum_of_row_products(partial_solution_file_path)
        if result >= Config.TARGET_VALUE:
            write_matrix_to_csv(optimized_matrix, final_solution_file_path)
            print(f'Target value: {Config.TARGET_VALUE}')
            print(f'Result: {result}')
            break
        initial_matrix = read_matrix_to_csv(partial_solution_file_path)

    lookup = create_probability_lookup(probabilities)
    indexed_solution = substitute_values_with_indices(read_matrix_to_csv(final_solution_file_path), lookup)
    write_matrix_to_csv(indexed_solution, final_indexed_solution_file_path)


if __name__ == "__main__":
    main()
