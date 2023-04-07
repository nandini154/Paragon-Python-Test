from . import app, db
from sqlalchemy import Column, String, Float, Integer
from datetime import datetime
from .ingestor import IngestInputs, WeatherMetrics
import click


class Weather(db.Model):
    __tablename__ = "Weather"
    Date = Column(String, primary_key=True)
    Max_Temp = Column(Float)
    Min_Temp = Column(Float)
    PPT = Column(Float)
    Station_ID = Column(String, primary_key=True)
    Year = Column(Integer)

    def __init__(self, Date, Max_Temp, Min_Temp, PPT, Station_ID, Year):
        self.Date = Date
        self.Max_Temp = Max_Temp
        self.Min_Temp = Min_Temp
        self.PPT = PPT
        self.Station_ID = Station_ID
        self.Year = Year


class WeatherStats(db.Model):
    __tablename__ = "weatherstats"
    Year = Column(Integer, primary_key=True)
    Station_ID = Column(String, primary_key=True)
    Avg_Max_Temp = Column(Float)
    Avg_Min_Temp = Column(Float)
    AccPPT = Column(Integer)

    def __init__(self, Year, Station_ID, Avg_Max_Temp, Avg_Min_Temp, AccPPT):
        self.Year = Year
        self.Station_ID = Station_ID
        self.Avg_Max_Temp = Avg_Max_Temp
        self.Avg_Min_Temp = Avg_Min_Temp
        self.AccPPT = AccPPT


@click.command(name="create")
def create():
    with app.app_context():
        db.create_all()
        print(f"Ingestion started at {datetime.now()}")
        data = IngestInputs("./wx_data")
        result = WeatherMetrics(data)
        data.to_sql("Weather", con=db.engine, if_exists="replace", index=False)
        result.to_sql("weatherstats", con=db.engine, if_exists="replace", index=False)
        print(f"Ingestion finished at {datetime.now()}")


app.cli.add_command(create)
