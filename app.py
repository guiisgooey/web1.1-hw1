# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

from random import randint

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    """Displays a message saying penguins are cute"""
    return "Penguins are cute!"

@app.route('/frogs')
def frogs():
    """Displays a message saying frogs are cute"""
    return "Frogs are cute!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal}s are my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'Wow, {users_dessert} is my favorite dessert, too!'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a madlib to the user that changes based on the adjective and noun input."""
    return f'I am a {adjective} {noun}!'

@app.route('/multiply/<n1>/<n2>')
def multiply(n1, n2):
    """Display the product of multiplication to the user that changes based on the numbers input. 
    If input is not numbers returns an error asking for the user to only input numbers"""
    if n1.isdigit() == True and n2.isdigit() == True:
        x = int(n1)*int(n2)
        return f'{n1} * {n2} = {x}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Display a word printed n times to the user that changes based on the users input. 
    If n is not numbers returns an error asking for the user to only input numbers"""
    if n.isdigit() == True:
        return int(n)*(word + ' ')
    else:
        return 'Invalid inputs. Please try again by entering a number for n!'

@app.route('/reverse/<word>')
def reverse(word):
    """Displays a word printed in reverse that changes based on the users input"""
    #reversed = word [::-1] #the easier way of doing things
    #return reversed
    reversed = "" 
    for i in word: 
        reversed = i + reversed
    return reversed

@app.route('/strangecaps/<word>')
def strangecaps(word):
    """Displays a word with even letters uppercased and odd letters lowercased that changes based on user input"""
    strangecapped = ""
    n = 1
    for i in word:
        if n%2 == 0:
            strangecapped += i.upper()
        else:
            strangecapped += i.lower()
        n+=1
    return strangecapped

@app.route('/dicegame')    
def dicegame():
    """Displays a random number from 1-6, if it is a 6 it displays that the user has one, if not it displays that the user has lost"""
    x = randint(1,6)
    if x == 6:
        return f'You rolled a {x}, you won!'
    else:
        return f'You rolled a {x}, you lost!'

if __name__ == '__main__':
    app.run(debug=True)