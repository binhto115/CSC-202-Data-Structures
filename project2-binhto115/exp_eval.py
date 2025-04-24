
from __future__ import annotations

from array_stack import empty_stack, is_empty, peek, pop, push


def postfix_eval(input_string: str) -> float:
    array_stack = empty_stack()
    if input_string == "":
        raise ValueError("empty input")
    else:
        split_string = input_string.split(" ")
        for string in split_string:
            try:
                new = float(string)
                push(array_stack, new)
            except ValueError:
                value = string
                if value == "+":
                    try:
                        pop_1 = pop(array_stack)
                        pop_2 = pop(array_stack)
                        addition = pop_2 + pop_1
                        push(array_stack, addition)
                    except IndexError:
                        raise ValueError("insufficient operands")
                elif value == "-":
                    try:
                        pop_1 = pop(array_stack)
                        pop_2 = pop(array_stack)
                        subtration = pop_2 - pop_1
                        push(array_stack, subtration)
                    except IndexError:
                        raise ValueError("insufficient operands")
                elif value == "*":
                    try:
                        pop_1 = pop(array_stack)
                        pop_2 = pop(array_stack)
                        multiplication = pop_2 * pop_1
                        push(array_stack, multiplication)
                    except IndexError:
                        raise ValueError("insufficient operands")
                elif value == "/":
                    try:
                        pop_1 = pop(array_stack)
                        pop_2 = pop(array_stack)
                        if pop_1 == 0:
                            raise ZeroDivisionError
                        else:
                            division = pop_2 / pop_1
                            push(array_stack, division)
                    except IndexError:
                        raise ValueError("insufficient operands")
                elif value == "//":
                    try:
                        pop_1 = pop(array_stack)
                        pop_2 = pop(array_stack)
                        if pop_1 == 0:
                            raise (ZeroDivisionError)
                        else:
                            division = pop_2 // pop_1
                            push(array_stack, division)
                    except IndexError:
                        raise ValueError("insufficient operands")
                elif value == "^":
                    try:
                        pop_1 = pop(array_stack)
                        pop_2 = pop(array_stack)
                        exponentiation = pop_2 ** pop_1
                        push(array_stack, exponentiation)
                    except IndexError:
                        raise ValueError("insufficient operands")
                else:
                    raise ValueError("invalid token")
    if array_stack.size > 1:
        raise ValueError("too many operands")
    return float(array_stack.array[0])


def operations_order(string: str) -> int:
    if string == "+" or string == "-":
        return 1
    elif string == "*" or string == "/" or string == "//":
        return 2
    elif string == "^":
        return 3
    return 0


def infix_to_postfix(input_string: str) -> str:
    rpn_stack = empty_stack()
    rpn_string = []
    array_stack = empty_stack()
    if input_string == "":
        raise ValueError("empty input")
    else:
        split_string = input_string.split(" ")
        for element in split_string:
            try:
                new_int = int(element)
                push(rpn_stack, new_int)
            except ValueError:
                value = element
                if value == "(":
                    push(array_stack, value)
                elif value == ")":
                    while array_stack.array[array_stack.size - 1] != "(":
                        new_pop = pop(array_stack)
                        push(rpn_stack, new_pop)
                    pop(array_stack)
                elif value == "^":
                    push(array_stack, value)
                elif (value == "+" or value == "-" or value == "*"
                      or value == "/" or value == "//"):
                    while (not is_empty(array_stack) and
                           operations_order(peek(array_stack)) >=
                           operations_order(value)):
                        new_pop = pop(array_stack)
                        push(rpn_stack, new_pop)
                    push(array_stack, value)
                else:
                    new_int = float(element)
                    push(rpn_stack, new_int)
    for i in range(array_stack.size - 1, -1, -1):
        if array_stack.array[i] is not empty_stack():
            new_pop = pop(array_stack)
            push(rpn_stack, new_pop)
    for i in range(0, rpn_stack.size):
        if type(rpn_stack.array[i]) == int:
            convert_int_to_str = str(rpn_stack.array[i])
            rpn_string.append(convert_int_to_str)
        elif type(rpn_stack.array[i]) == float:
            convert_int_to_str = str(rpn_stack.array[i])
            rpn_string.append(convert_int_to_str)
        else:
            rpn_string.append(rpn_stack.array[i])
    join_string = " ".join(rpn_string)
    return (join_string)
print(infix_to_postfix("2 ^ 3 ^ 2"))