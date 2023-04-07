# Code Challenge Template
# Weather API

This API provides access to weather and yield data for different locations and years. You can filter the data by date and location, and it also provides statistical information on weather data.

## Features
The API enables you to:
- Fetch weather information for a particular date and location
- Get statistical details about the weather data, such as the highest, lowest, and total rainfall for a       specific date and location.

# Installation
>create virtual environment:
```bash
cd answers
python -m venv venv
source ./venv/bin/activate
```

>Install the required packages:
```bash
pip3 install -r requirements.txt
```

## Usage

- Run the following command to create the database and populate it with data:

```bash
python3 -m flask create
```

- Run the following command to create the database and populate it with data:

- Start the API server
```bash
 python3 -m flask run
```
- The API can now be accessed at `http://localhost:5000`

---

### Endpoints

#### Swagger <br>
 `http://localhost:5000/apidocs/`

#### Weather data
```
GET /weather
```
This endpoint returns a paginated list of weather records. You can filter the results by date and Station_ID using query parameters:
```
GET /weather?date=19850103&Station_ID=USC00257715
```

##### Weather Stats data
```
GET /weather/stats

```
This endpoint returns statistical information about the weather data. You can filter the results by date and station using query parameters, in the same way as the /weather/ endpoint.

### Example Request

``` bash
 curl -X GET "http://127.0.0.1:5000/weather?page=1&per_page=100&date=19850211&Station_ID=USC00257715" -H "accept: application/json"
```

# Testing

## Run the tests
-Run 
```bash
python3 -m flask create
```
before 

```bash
pytest -W ignore::DeprecationWarning
```
# Deployment

One possible solution for deploying the Flask API, database, and scheduled data ingestion code on AWS is to use Amazon ECS for deployment, Amazon RDS for the database, Amazon S3 for data storage, AWS Glue for data ingestion and job scheduling, AWS CloudWatch for monitoring and logging, AWS Elastic Container Registry (ECR) for container image storage, and Application Load Balancer for traffic routing. This approach offers a fully managed, scalable, and durable solution for deploying these components on AWS.







