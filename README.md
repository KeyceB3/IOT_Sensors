# IOT_Sensors
IOT Sensors for TP in B3 at Keyce

README:

Introduction:
This is a Python API that communicates with an InfluxDB database and a Grafana dashboard. The API receives data from sensors in the form of a hexadecimal string and processes it to extract the relevant information. The processed data is then stored in the InfluxDB database and displayed on the Grafana dashboard.

Prerequisites:
- Python 3
- Flask
- InfluxDB
- Grafana
 
Installation:

Clone the repository: git clone https://github.com/<your-username>/api-influxdb-grafana.git
Install the required libraries: pip install flask influxdb_client
In the bddInfluxDB function, replace host, port, username, password, and database with your InfluxDB credentials.
In the SendBdd function, replace bucket, org, and token with your InfluxDB details. Replace url with the URL of your InfluxDB instance.
  
Usage:
  
Run the API: python api.py
The API will now be running at http://127.0.0.1:5000/.
To send data to the API, make a POST request to the appropriate endpoint: /api/humidity or /api/temperature. Include the sensor data in the request body as a JSON object with the key data.
The processed data will be stored in the InfluxDB database and displayed on the Grafana dashboard.
  
Notes:
  
The humidity and temperature routes handle data from sensors with codes 10 and 20 (humidity) and 30 and 40 (temperature).
The data received from the sensors is in the form of a hexadecimal string. The API converts this string to decimal and processes it to extract the relevant information (sensor code, sensor value, and threshold value if applicable).
The SendBdd function stores the processed data in the InfluxDB database.
  
License:
  
This project is licensed under the MIT License - see the LICENSE file for details.
