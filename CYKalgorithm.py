def CYK_parse(grammar, string):
    """
    Parses a string using the CYK algorithm to determine if it can be derived from a given context-free grammar in 
    Chomsky Normal Form (CNF).

    Args:
    grammar (dict): A dictionary representing the context-free grammar in CNF.
    string (str): The string to be parsed.

    Returns:
    tuple: A tuple consists of
        1. A 2D list representing the CYK parsing table, with each cell containing a set of non-terminal symbols.
        2. A boolean value indicating whether the string can be derived from the start symbol ('S').
    """

    n = len(string)
    r = len(grammar)
    
    # If statement to handle empty strings. Assumes 'e' symbol used for epsilon.
    if n == 0:
        if 'e' in grammar['S']:
            return [], True
        else:
            return [], False
    else:

        # Create a 2D list table to store intermediate parsing results
        T = [[set() for _ in range(n)] for _ in range(n)]

        # The table is filled starting from substrings of length 1, gradually moving to longer substrings
        for i in range(n):
        # loops over the characters of the input string
            for lhs, rhs in grammar.items():
            # loops over the items in the grammar dictionary--
            # lhs:a non-terminal symbol; rhs: the set of terminal symbols (production rules) associated with the non-terminal.
                if string[i] in rhs:
                # if the ith character of the input string is part of the production rule set (rhs), 
                # the non-terminal symbol (lhs) can be used to derive this specific character according to the grammar rules.
                    T[i][i].add(lhs)
                    # if the above is true, then non-terminal symbol (lhs) is added to the set at position [i][i] in the 2D list T.
                    print(f"{string[i]} found in {lhs, rhs}. Adding {lhs} to T[{i}][{i}]")
                    # show character from the string was found in the grammar rule 
                    # and which non-terminal symbol was added to the table.
                    print_table(T)
                    # update the table visualization for each iteration

        # Fill in the table for substrings of length 2 to n
        for l in range(2, n + 1):
        # loops over the possible lengths of substrings, starting from 2 up to the length of the input string
            for i in range(n - l + 1):
            #starting from 0 to 
                j = i + l - 1
                # calculates the ending index (j) of the substring
                for k in range(i, j):
                # loops over the substring
                    for lhs, rhs in grammar.items():
                    # loops over the items in the grammar dictionary--
                    # lhs:a non-terminal symbol; rhs: the set of terminal symbols (production rules) associated with the non-terminal.
                        for prod in rhs:
                        # iterates over each production rule "prod" in the set rhs.
                            if len(prod) == 2 and prod[0] in T[i][k] and prod[1] in T[k + 1][j]:
                            # if these 3 conditions are met:
                            # 1. the production rule prod is a binary
                            # 2. the first symbol of prod can generate the substring from i to k
                            # 3. the second symbol of prod can generate the substring from k + 1 to j
                                print(f"{prod[0]} found in T[{i}][{k}] and {prod[1]} found in T[{k+1}][{j}]. {lhs} : {prod[0]}{prod[1]} is valid. Adding {lhs} to T[{i}][{j}]")
                                T[i][j].add(lhs)
                                # then add the non-terminal lhs, since can generate the substring from i to j
                                print_table(T)
                                # update the table visualization for each iteration


        # After the table is filled, the function checks if the start symbol ('S') is in the top-right cell of the table.
        print(f"Table filled. Checking if {T[0][n-1]} (T[0][{n-1}]) contains S")
        return T, 'S' in T[0][n - 1] 
        # the string can be derived from the start symbol according to the grammar if S (start) is an option in the top right corner

def print_table(table):
    """
    Prints the parsing table.

    Args:
    table (list of list of sets): A 2D list representing a table where each cell contains a set of symbols.
                                  this is usually the parsing table generated from algorithms like CYK.

    Returns:
    - None: This function does not return values -- it solely prints and visualizes the table
    """
    print("Parsing table:")
    for row in table:
        print(row)

# Example grammar in CNF
# rules
grammar = {
    'S': {'AB'}, #S: start sym
    'A': {'BB', 'a'},
    'B': {'AB', 'b'}
}

# Example strings (TRUE)
string = "aabbb"
string1 = "ab"
string2 = "babbbb"
string3 = "abbbbaabbab"

# Example strings (FALSE)
string4 = ""
string5 = "b"
string6 = "abababababaa"


# Parse the string
table, result = CYK_parse(grammar, string)

# Print the result
print("Can the string be derived?", result)
# print_table(table)

grammar_anbn = {
    'S': {'AB', 'AR', 'e'}, #S: start sym
    'T': {'AB', 'AR'},
    'R': {'TB'},
    'A': {'a'},
    'B': {'b'}
}

# Example strings (TRUE)
string_anbn = "aabb"
string0_abnb = ""
string1_anbn = "ab"

# Example strings (FALSE)
string2_anbn = "abbb"
string3_anbn = "b"
string4_anbn = "abab"

table, result = CYK_parse(grammar_anbn, string0_abnb)
print("Can the string be derived?", result)