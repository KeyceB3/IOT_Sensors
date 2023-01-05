# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, json
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

def bddInfluxDB():
    client = InfluxDBClient(host='localhost', port=8086, username='keyce', password='keycekeyce',
                            database='keyce')

def SendBdd(name, value):
    bucket = "keyce"
    org = "keyce"
    token = "aIYwHMeAdK6auxP5rB1yxhzpD0mNsaDY3GTDg7ZMCAbWJVwX-yyaEtK3srjFdLhCActEn-Qea1ThxfVCVLqWRQ=="
    # Store the URL of your InfluxDB instance
    url = "http://localhost:8086"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    # Write script
    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = influxdb_client.Point("Sensors").tag("Sensor", name).field("Value", value)
    write_api.write(bucket=bucket, org=org, record=p)


# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
# Code Use for Humidity
@app.route('/api/humidity', methods=['POST'])
def humidity():
    data = json.loads(request.data)
    value = data['data']
    first_two_digits = value[0:2]
    last_four_digits = value[2:6]
    last_eight_digits = value[6:10]
    decimal_value_1 = int(first_two_digits, 16)
    decimal_value_2 = int(last_four_digits, 16)
    if decimal_value_1 == 10:
        decimal_value_3 = int(last_eight_digits, 16)
        print("Code:", decimal_value_1, "Humidité:", decimal_value_2/10, "Seuil:", decimal_value_3/10)
    if decimal_value_1 == 20:
        print("Code:", decimal_value_1, "Humidité:", decimal_value_2/10)
    SendBdd("Humidity", decimal_value_2/10)
    return jsonify({"data" : (decimal_value_1, decimal_value_2)})


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
# Code Use for Temperature
@app.route('/api/temperature', methods=['POST'])
def temperature():
    data = json.loads(request.data)
    value = data['data']
    first_two_digits = value[0:2]
    last_four_digits = value[2:6]
    last_eight_digits = value[6:10]
    decimal_value_1 = int(first_two_digits, 16)
    decimal_value_2 = int(last_four_digits, 16)
    if decimal_value_1 == 30:
        decimal_value_3 = int(last_eight_digits, 16)
        print("Code:", decimal_value_1, "Température:", decimal_value_2/10, "Seuil:", decimal_value_3/10)
    if decimal_value_1 == 40:
        print("Code:", decimal_value_1, "Température:", decimal_value_2/10)
    SendBdd("Degree", decimal_value_2 / 10)
    return jsonify({"data" : (decimal_value_1, decimal_value_2)})

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10


# driver function
if __name__ == '__main__':
    app.run(debug=True)
