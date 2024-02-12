# flask app to display even and odd number

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/even', methods=['GET'])
def even():
    num = request.args.get('num')
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            return jsonify({"result": "Even"})
        else:
            return jsonify({"result": "Odd"})
    else:
        return jsonify({"error": "Please enter a valid number"})

if __name__ == '__main__':
    app.run(debug=True, host='', port=5000)