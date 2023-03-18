def print_operation_table(operation, num_rows=6, num_columns=6):
    print("   | ", end="")
    for j in range(1, num_columns+1):
        print("{0:4d}".format(j), end="")
    print()
    print("---+" + "-"*4*num_columns)
    for i in range(1, num_rows+1):
        print("{0:3d}| ".format(i), end="")
        for j in range(1, num_columns+1):
            result = operation(i, j)
            print("{0:4d}".format(result), end="")
        print()