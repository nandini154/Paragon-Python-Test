from flasgger import Swagger
from . import app
from .models import Weather, WeatherStats
from .schema import WeatherSchema, WeatherStatSchema
from flask import request, jsonify

swagger = Swagger(app)

weather_schema = WeatherSchema(many=True)
weather_stat_schema = WeatherStatSchema(many=True)


@app.route("/weather", methods=["GET"])
def get_weather():
    """
    This endpoint returns a paginated list of weather data for a given date and station id,
    or for all weather data if no date or station id is specified.
    ---
    parameters:
        - name: page
          in: query
          type: integer
          default: 1
          description: The page number to return.
        - name: per_page
          in: query
          type: integer
          default: 100
          description: The number of results per page.
        - name: date
          in: query
          type: integer
          description: The date for which to return weather data (in YYYYMMDD format).
        - name: Station_ID
          in: query
          type: string
          description: The station id for which to return weather data.

    responses:
        200:
            description: OK
    """
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=100, type=int)
    date = request.args.get("date", type=int)
    Station_ID = request.args.get("Station_ID")
    if date and Station_ID:
        all_items = Weather.query.filter(
            Weather.Date == date, Weather.Station_ID == Station_ID
        ).paginate(page=page, per_page=per_page, error_out=False)
        result = weather_schema.dump(all_items)
        return jsonify(result)
    if date:
        all_items = Weather.query.filter(Weather.Date == date).paginate(
            page=page, per_page=per_page, error_out=False
        )
        result = weather_schema.dump(all_items)
        return jsonify(result)
    if Station_ID:
        all_items = Weather.query.filter(Weather.Station_ID == Station_ID).paginate(
            page=page, per_page=per_page, error_out=False
        )
        result = weather_schema.dump(all_items)
        return jsonify(result)
    all_items = Weather.query.paginate(page=page, per_page=per_page, error_out=False)
    result = weather_schema.dump(all_items)
    return jsonify(result)


@app.route("/weather/stats", methods=["GET"])
def get_stats():
    """
    This endpoint retrieves weather statistics based on the given parameters.
    ---
    parameters:
        - name: page
          in: query
          type: integer
          default: 1
          required: false
          description: The page number to return
        - name: per_page
          in: query
          type: integer
          default: 100
          required: false
          description: The number of items to return per page
        - name: year
          in: query
          type: integer
          required: false
          description: The year to filter by
        - name: Station_ID
          in: query
          type: string
          description: The station id for which to return weather data.
    responses:
        200:
            description: OK
    """
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=100, type=int)
    year = request.args.get("year", type=int)
    Station_ID = request.args.get("Station_ID")
    if year and Station_ID:
        all_items = WeatherStats.query.filter(
            WeatherStats.Year == year, WeatherStats.Station_ID == Station_ID
        ).paginate(page=page, per_page=per_page, error_out=False)
        result = weather_stat_schema.dump(all_items)
        return jsonify(result)
    if year:
        all_items = WeatherStats.query.filter(WeatherStats.Year == year).paginate(
            page=page, per_page=per_page, error_out=False
        )
        result = weather_stat_schema.dump(all_items)
        return jsonify(result)
    if Station_ID:
        all_items = WeatherStats.query.filter(
            WeatherStats.Station_ID == Station_ID
        ).paginate(page=page, per_page=per_page, error_out=False)
        result = weather_stat_schema.dump(all_items)
        return jsonify(result)
    all_items = WeatherStats.query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    result = weather_stat_schema.dump(all_items)
    return jsonify(result)
