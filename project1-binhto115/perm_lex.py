from __future__ import annotations


def perm_gen_lex(string: str) -> list[str]:
    """This function takes in a list of strings and
    return its permutations
    """
    list_of_perm = []
    if string == "":
        return [""]
    for char in string:
        simpler_string = string.replace(char, "")
        for perm in perm_gen_lex(simpler_string):
            add_it = char + perm
            list_of_perm.append(add_it)
    return list_of_perm
