import csv


def multiply_row_values(row):
    product = 1
    for value in row:
        product *= float(value)
    return product


def sum_of_row_products(file_path):
    total_sum = 0
    with open(file_path, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            row_product = multiply_row_values(row)
            total_sum += row_product
    return total_sum
