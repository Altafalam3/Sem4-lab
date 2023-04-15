from flask import Flask, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the exam!"


@app.route('/result/<int:marks>')
def result(marks):
    if marks < 40:
        return redirect('/failed')
    else:
        return redirect('/passed')

@app.route('/failed')
def failed():
    result = {
        'message': 'Sorry, you have failed the exam.'
    }
    return jsonify(result)

@app.route('/passed')
def passed():
    result = {
        'message': 'Congratulations, you have passed the exam!'
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
