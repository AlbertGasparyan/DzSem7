def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        table = []
        for j in range(1, num_columns + 1):
            table.append(str(operation(i, j)))
        print(''.join(f'{e}' for e in table))

print_operation_table(lambda x, y: x*y)