import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("YesIntentEasy")
def next_round_easy():
    numbers = [randint(0, 9) for _ in range(3)]
    round_msg = render_template('round', numbers=numbers)
    session.attributes['numbers'] = numbers[::-1]  # reverse
    return question(round_msg)

@ask.intent("YesIntentMedium")
def next_round_medium():
    numbers = [randint(0, 9) for _ in range(5)]
    round_msg = render_template('round', numbers=numbers)
    session.attributes['numbers'] = numbers[::-1]  # reverse
    return question(round_msg)

@ask.intent("YesIntentHard")
def next_round_hard():
    numbers = [randint(0, 9) for _ in range(10)]
    round_msg = render_template('round', numbers=numbers)
    session.attributes['numbers'] = numbers[::-1]  # reverse
    return question(round_msg)


@ask.intent("AnswerIntentEasy", convert={'first': int, 'second': int, 'third': int})
def answer(first, second, third):
    winning_numbers = session.attributes['numbers']
    if [first, second, third] == winning_numbers:
        msg = render_template('win')
    else:
        msg = render_template('lose')
    return statement(msg)

@ask.intent("AnswerIntentMedium", convert={'first': int, 'second': int, 'third': int, 'fourth': int, 'fifth':int})
def answer(first, second, third, fourth, fifth):
    winning_numbers = session.attributes['numbers']
    if [first, second, third, fourth, fifth] == winning_numbers:
        msg = render_template('win')
    else:
        msg = render_template('lose')
    return statement(msg)

@ask.intent("AnswerIntentHard", convert={'first': int, 'second': int, 'third': int, 'fourth': int, 'fifth':int, 'sixth':int, 'seventh':int, 'eigth':int, 'ninth':int, 'tenth':int})
def answer(first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth):
    winning_numbers = session.attributes['numbers']
    if [first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth] == winning_numbers:
        msg = render_template('win')
    else:
        msg = render_template('lose')
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)