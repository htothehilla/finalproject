# install dependent libraries
# you will have to pip install requests when creating a new enviroments via the terminal
# documentation api https://developer.edamam.com/edamam-docs-recipe-api
import requests

#to use please request an api

api_id = "request yah own"
api_key = "request yah own via ednam"

#asking user how much time they have
time = input("how much time in minutes do you have to cook ?")

# define a function that calls the api with
def recipe_search(ingredient):
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=0&to=10&health=vegan&time={}'.format(
        ingredient, api_id, api_key,time)
    response = requests.get(url)
    recipe = response.json()
    return recipe['hits']

# define a function that asks a user what ingredient they would like

def run():
    question = input('What ingredient do you have to cook with ? : ')
    recipe_response = recipe_search(question)

    # save results to a file

    with open('results.txt', 'w+') as recipe_file:
        for recipe in recipe_response:
            recipe_file.write(recipe['recipe']['label'] + '\n')
            recipe_file.write(recipe['recipe']['url'] + '\n')
            recipe_file.write(str(recipe['recipe']['healthLabels']) + '\n')
            recipe_file.write(str(recipe['recipe']['totalTime']) + '\n')
            recipe_file.write('\n')

run()

