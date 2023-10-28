from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample riddles for demonstration
riddles = [
    {"riddle": "What has keys but can't open locks?", "answer": "piano"},
    {"riddle": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"}
]

current_riddle = riddles[0]

@app.route('/')
def index():
    return render_template('index.html', riddle=current_riddle["riddle"])

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('answer')
    if user_answer == current_riddle["answer"]:
        return jsonify({"result": "correct"})
    else:
        return jsonify({"result": "incorrect"})

if __name__ == "__main__":
    app.run(debug=True)
