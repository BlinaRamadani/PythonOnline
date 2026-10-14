def add(x, y):
    return x + y

print(add(1, 3))

def concatenate(x, y):
    return str(x) + str(y)

print(concatenate(1, 2))

def operate(operation, x, y):
    """
    Performs a specified operation on two operands

    :param operation:  The operation function to be performed
    :param x: The first operand
    :param y: The second operand
    :return: The result of the operation

    """

    result_sum = operation(add, 3, 5)
    result_concatenate = operate(concatenate, "Hello", "World")
