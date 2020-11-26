import requests, json


def cocktail():
    drinkname = input("Which cocktail would you like today? ")
    #base link
    link = ('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkname)
    response = requests.get(link)
    info = json.loads(response.text)
    def web():
        if response.status_code == 200:
            print("\n", "Drink Found!", "\n")
            drinkinfo()
        else:
            print("Drink not found. Try another drink.")
    def drinkinfo():
        for i in (info['drinks']):
            #drink name
            print("Drink name:", i['strDrink'], '\n')
            #drink instructions
            print("Instructions:", i['strInstructions'], '\n')
            print("Ingredients:","\n")
            #drink ingredients 
            x = 1
            while x < 17:
                Ingredient = ("strIngredient" + str(x))
                Measure = ("strMeasure" + str(x))
                if i[Ingredient] is None:
                    print('\n'+'Enjoy your drink!')
                    x+=17
                else:
                    print(i[Ingredient], "-", i[Measure])
                    x+=1
    web()
cocktail()