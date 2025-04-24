from __future__ import annotations


def bears(n: int) -> bool:
    """
    This function takes in an integer and return whether we can
    win the bear game by reaching 42 bears.
    """
    if n == 42:
        return True
    elif n < 42:
        return False
    else:
        if n % 5 == 0 and bears(n - 42):
            return True
        elif (n % 2 == 0) and bears(n / 2):
            return True
        elif (n % 3 == 0) or (n % 4 == 0):
            string_it = str(int(n))
            lst = [num for num in string_it]
            last_num = int(lst[-1])
            second_last_num = int((lst[-2]))
            new_n = (n - (last_num * second_last_num))
            if new_n == n:
                return False
            return bears(new_n)
        else:
            return False
