<h1>README:</h1>

<h2>Introduction:</h2>
This is a Python API that communicates with an InfluxDB database and a Grafana dashboard. The API receives data from sensors in the form of a hexadecimal string and processes it to extract the relevant information. The processed data is then stored in the InfluxDB database and displayed on the Grafana dashboard.

<h2>Prerequisites:</h2>
 - Python 3 <br>
 - Flask <br>
 - InfluxDB <br>
 - Grafana <br>
 
<h2>Installation:</h2>

Install the required libraries: <br> 
- pip install flask
- pip install influxdb_client <br>

In the SendBdd function replace with your InfluxDB details:
- bucket
- org
- token<br>

Replace url with the URL of your InfluxDB instance. <br>
  
<h2>Usage:</h2>
  
Run the API: python api.py <br>
The API will now be running at http://127.0.0.1:5000/. <br>
To send data to the API, make a POST request to the appropriate endpoint: /api/humidity or /api/temperature. Include the sensor data in the request body as a JSON object with the key data. <br>
The processed data will be stored in the InfluxDB database and displayed on the Grafana dashboard. <br>
  
<h2>Notes:</h2>
  
The humidity and temperature routes handle data from sensors with codes 10 and 20 (humidity) and 30 and 40 (temperature). <br>
The data received from the sensors is in the form of a hexadecimal string. The API converts this string to decimal and processes it to extract the relevant information (sensor code, sensor value, and threshold value if applicable). <br>
The SendBdd function stores the processed data in the InfluxDB database. <br>
  
<h2>License:</h2>
  
This project is licensed under the MIT License - see the LICENSE file for details.
