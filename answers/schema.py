from . import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class WeatherSchema(ma.Schema):
    class Meta:
        fields = ("Date", "Max_Temp", "Min_temp", "PPT", "Station_ID", "Year")


class WeatherStatSchema(ma.Schema):
    class Meta:
        fields = ("Year", "Station_ID", "Avg_Max_Temp", "Avg_Min_Temp", "AccPPT")
