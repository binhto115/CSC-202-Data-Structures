from __future__ import annotations


def convert(num: int, base: int) -> str:
    """
    This function takes in a number and a base to return a single
    string of remainders representing the number in the given
    base
    """
    remainder_rep = "0123456789ABCDEF"
    div = num // base
    mod = num % base
    if div == 0:
        if mod >= 10:
            post_mod_var = remainder_rep[mod]
            return str(post_mod_var)
        else:
            return str(mod)
    else:
        if mod >= 10:
            post_mod_var = remainder_rep[mod]
            return convert(div, base) + str(post_mod_var)
        else:
            return convert(div, base) + str(mod)
