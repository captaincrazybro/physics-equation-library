def not_enough_params(min_num: int):
    return NameError(f'Not enough variables specified: please specify at least {min_num} parameters')

def cannot_divide_vectors():
    return NameError("Invalid terms - Cannot divide vectors")

def not_enough_or_invalid(min_num: int):
    return NameError(f'Not enough parameters or invalid combination of parameters: please specify at least {min_num} parameters')

def invalid_param_combination():
    return NameError("Invalid combination of parameters")