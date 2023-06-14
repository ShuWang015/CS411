from __future__ import annotations

import flask
from model import ConcentrationModel
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

model = ConcentrationModel()


@app.route('/health', methods=['GET'])
def health() -> flask.Response:
    """Health check.

    """
    data = {
        'message': 'OK'
    }
    return flask.make_response(data, 200)


@app.route('/reset', methods=['POST'])
def reset() -> flask.Response:
    """Reset game.

    """
    # Specify global scope if going to change the value of a global variable.
    global model

    model = ConcentrationModel()

    global guesses

    guesses = 0

    data = {
        'message': 'OK'
    }
    return flask.make_response(data, 200)


@app.route('/card/<int:index>', methods=['GET'])
def card(index: int) -> flask.Response:
    """Get card info.

    Parameter
    ---------
    index : int
        The card's index

    """
    # TODO: Implement. See Part 2: Card information.
    data = {
        "card": model.cards[index],
        "match": model.matched[index],
        "state": model.state[index]
    }

    return flask.make_response(data, 200)


@app.route('/select/<int:index>', methods=['POST'])
def select(index: int) -> flask.Response:
    """Select a card.

    """
    # Specify global scope if going to change the value of a global variable.
    global model
    # Edge cases: Selecting a matched card or selected card.
    # TODO: Implement. See Part 3: Card selection.
    
    second_index = []
    for i in range(52):
        if model.state[i] == "up" and (model.matched[i] == False):
            second_index = second_index + [i]
    if len(second_index) >= 2:
        for i in second_index:
            model.state[i] = "down"
            model.matched[i] = False
            
    if model.matched[index] is True:
        data = {
            'message': 'Card already matched. Try again.'
        }
        return flask.make_response(data, 200)
    if model.state[index] == 'up':
        data = {
            'message': 'Card already selected. Try again.'
        }
        return flask.make_response(data, 200)

    if len(second_index) == 0 :
        model.state[index] = "up"
        model.matched[index] == False
    elif len(second_index) == 1:
        two = second_index[0]
        global guesses
    
        guesses = guesses + 1
        if model.cards[index][0] == model.cards[two][0]:
            model.state[index] = "up"
            model.matched[index] = True
            model.state[two] = "up"
            model.matched[two] = True
        else:
            model.state[index] = "up"
            model.matched[index] = False
            model.state[two] = "up"
            model.matched[two] = False

    data = {
        'message': 'OK'
    }
    return flask.make_response(data, 200)


@app.route('/guesses', methods=['GET'])
def get_guesses() -> flask.Response:
    """Get number of guesses.
    """
    # TODO: Implement. See Part 4: Guesses counter.
    global guesses

    data = {
        "guesses": guesses
    }

    return flask.make_response(data, 200)


if __name__ == '__main__':
    app.run(debug=True)
