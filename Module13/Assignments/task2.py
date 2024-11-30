from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_airport_info(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="flight_game"
    )
    cursor = connection.cursor()


    query = "select * from airport where ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return {
            "ICAO": icao_code,
            "Name": result[0],
            "Location": result[1]
        }
    else:
        return {"error": "Airport not found"}

@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport(icao_code):
    airport_info = get_airport_info(icao_code)
    return jsonify(airport_info)

if __name__ == '__main__':
    app.run(debug=True)
