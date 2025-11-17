##exercise 8-15 printing models
#put the functions for the example printing_models.py in a seperate file called
#printing_functions.py
#write an import statement on the top of printing_models.py, and modify the  file
#to use the imported functions

from printing_models_exercise_req import print_models, show_completed_models

unprinted_design = ['phone case','doll']
completed_models = []

print_models(unprinted_design,completed_models)
show_completed_models(completed_models)




