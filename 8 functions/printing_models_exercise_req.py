def print_models(unprinted_designs, completed_models):
    """simulate printing design until none are left
    move each designt o completed models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """show all the models that are printed"""
    for completed_model in completed_models:
        print(completed_model)