"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
                <html>Hi! This is the home page.<br><br>
                <a href="http://localhost:5000/hello"> Click here to say hello!</a><br>
                <a href="http://localhost:5000/diss"> Click here to read a message!</a>
                </html>
                """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name and a compliment."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br><br>
          Pick a compliment:
          <select name="awesome-compliment">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="lovely">Lovely</option>
            <option value="ducky">Ducky</option>
          </select><br><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def insults_user():
    """Say hello and prompt for user's name and an insult."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br><br>
          Pick an insult:
          <select name="awesome-insult">
            <option value="stinky">Stinky</option>
            <option value="ugly">Ugly</option>
            <option value="annoying">Annoying</option>
            <option value="dumb">Dumb</option>
          </select><br><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet') #save it as a variable so if/else works?? 
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("awesome-compliment")
    insult = request.args.get("awesome-insult")

    if route('/hello'):

        return """
        <!doctype html>
        <html>
          <head>
            <title>A Nice Message</title>
          </head>
          <body>
            Hi, {player}! I think you're {compliment}!
          </body>
        </html>
        """.format(player=player, compliment=compliment)

    else:

        return """
        <!doctype html>
        <html>
          <head>
            <title>A Nice Message</title>
          </head>
          <body>
            Hi, {player}! I think you're {insult}!
          </body>
        </html>
        """.format(player=player, insult=insult)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
