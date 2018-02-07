from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/')
def index():
    session['scene'] = map.START.urlname
    session['count_empty_user_inputs'] = 1
    return redirect(url_for('game_get'))

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        thescene.count = 1
        return render_template('show_scene.html', scene=thescene)
    else:
        # My code enters into a new -> "no-session" scene
        return render_template('you_died.html', scene=map.SCENES["no_session"])

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if not userinput:
            # Weird, a POST request to /game with no user input... what should your code do?
            ## !!!
            # for some reason this condition is never TRUE. Even when no input is entered.
            # ...otherwise my code would run the following code:
            # return render_template('show_scene.html', scene=map.SCENES[session['scene']])
            #             return render_template('you_died.html')
            session['count_empty_user_inputs'] = session['count_empty_user_inputs'] + 1
            currentscene = map.SCENES[session['scene']]
            currentscene.count = session['count_empty_user_inputs']
            return render_template('show_scene.html', scene=currentscene)
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # There's no transition for that user input.
                # what should your code do in response?
                return render_template('you_died.html', scene =currentscene)
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')


app.secret_key = '555'

if __name__ == "__main__":
    app.run()
