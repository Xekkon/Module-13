from flask import Flask, jsonify
app = Flask(__name__)


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    response = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
