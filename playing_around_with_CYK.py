def CYK_parse(grammar, string):
    n = len(string)
    r = len(grammar)
    
    # Create a table to store results
    T = [[set() for _ in range(n)] for _ in range(n)]

    # Fill in the table for substrings of length 1
    for i in range(n):
        for lhs, rhs in grammar.items():
            if string[i] in rhs:
                T[i][i].add(lhs)
                print(f"{string[i]} found in {lhs, rhs}. Adding {lhs} to T[{i}][{i}]")
                print_table(T)

    # Fill in the table for substrings of length 2 to n
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for lhs, rhs in grammar.items():
                    for prod in rhs:
                        if len(prod) == 2 and prod[0] in T[i][k] and prod[1] in T[k + 1][j]:
                            print(f"{prod[0]} found in T[{i}][{k}] and {prod[1]} found in T[{k+1}][{j}]. {lhs} : {prod[0]}{prod[1]} is valid. Adding {lhs} to T[{i}][{j}]")
                            T[i][j].add(lhs)
                            print_table(T)


    # Return the table and whether the start symbol (assumed to be 'S') can derive the string
    print(f"Table filled. Checking if {T[0][n-1]} (T[0][{n-1}]) contains S")
    return T, 'S' in T[0][n - 1] #string only valid if S (start) is an option in the top right corner

def print_table(table):
    print("Parsing table:")
    for row in table:
        print(row)

# Example grammar in CNF
grammar = {
    'S': {'AB'}, #S: start sym
    'A': {'BB', 'a'},
    'B': {'AB', 'b'}
}

# Example string
string = "aabbb"

# Parse the string
table, result = CYK_parse(grammar, string)

# Print the result
print("Can the string be derived?", result)
# print_table(table)