def not_enough_params(min_num: int):
    return NameError(f'Not enough variables specified: please specify at least {min_num}')

def cannot_divide_vectors():
    return NameError("Invalid terms - Cannot divide vectors")