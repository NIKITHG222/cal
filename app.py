from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json.get('expression', '')
    try:
        # Warning: eval can be dangerous, so we'll restrict built-ins
        result = eval(expression, {"__builtins__":None}, {})
    except Exception:
        return jsonify({'result': 'Error'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

