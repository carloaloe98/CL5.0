import random
from src.config.config import Config


def optimize_matrix(matrix, probabilities):
    while True:
        i = random.randint(0, Config.TOTAL_SCENARIOS - 1)
        j = random.randint(0, 5)

        value = matrix[i][j]
        max_value = max(probabilities[j])
        min_value = min(probabilities[j])
        medium_value = sorted(probabilities[j])[1]

        if value == max_value:
            continue  # Select new i and j

        if value == min_value or value == medium_value:
            matrix[i][j] = random.choice([max_value, medium_value])
            break  # Exit the loop after making the change

    return matrix
