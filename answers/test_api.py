import unittest
from .app import app


class TestWeatherAPI(unittest.TestCase):
    def test_get_weather_all(self):
        with app.test_client() as client:
            response = client.get("/weather")
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)

    def test_get_weather_by_date(self):
        with app.test_client() as client:
            response = client.get("/weather?date=19850111")
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)

    def test_get_weather_by_stationid(self):
        with app.test_client() as client:
            response = client.get("/weather?Station_ID=USC00338534")
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)

    def test_get_weather_by_date_and_stationid(self):
        with app.test_client() as client:
            response = client.get("/weather?date=19850111&Station_ID=USC00338534")
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)
            self.assertEqual(response.status_code, 200)

    def test_get_stats_all(self):
        with app.test_client() as client:
            response = client.get("/weather/stats")
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)
            self.assertEqual(response.status_code, 200)

    def test_get_stats_by_year(self):
        with app.test_client() as client:
            response = client.get("/weather/stats?year=1985")
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)
            self.assertEqual(response.status_code, 200)

    def test_get_stats_by_stationid(self):
        with app.test_client() as client:
            response = client.get("/weather/stats?Station_ID=USC00338534")
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)

    def test_get_stats_by_year_and_stationid(self):
        with app.test_client() as client:
            response = client.get("/weather/stats?year=1985&Station_ID=USC00338534")
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertTrue(isinstance(data, list))
            self.assertTrue(len(data) > 0)


if __name__ == "__main__":
    unittest.main()
