from dataclasses import dataclass
from pathlib import Path

@dataclass
class SensorReading:
    timestamp: int
    sensor_name: str
    temperature: float
    humidity: float

    @classmethod
    def from_string(cls, row:str):
        row = row.strip()
        timestamp, sensor_name, temperature, humidity=row.split(',')
        return cls(int(timestamp), sensor_name, float(temperature), float(humidity))


class SensorData:
    def __init__(self):
        self.rows = []
        path = Path(__file__).parent.parent / "sensor-simulator" / "sensor_data.csv"
        with open(path, 'r') as file:
            lines = file.readlines()
        for i in range(1,len(lines)):
            self.rows.append(SensorReading.from_string(lines[i]))

    def average_temperature(self) -> float :
        avg=0
        for row in self.rows:
            avg += row.temperature
        avg /= len(self.rows)
        return avg
    
    def min_max_temperature(self) -> list[float] :
        min_temperature = self.rows[0].temperature
        max_temperature = self.rows[0].temperature
        for row in self.rows:
            max_temperature = max(max_temperature,row.temperature) 
            min_temperature = min(min_temperature,row.temperature) 
        return [min_temperature,max_temperature]
    
    def average_humidity(self) -> float :
        avg=0
        for row in self.rows:
            avg += row.humidity
        avg /= len(self.rows)
        return avg
    
    def min_max_humidity(self) -> list[float] :
        min_humidity = self.rows[0].humidity
        max_humidity = self.rows[0].humidity
        for row in self.rows:
            max_humidity = max(max_humidity,row.humidity) 
            min_humidity = min(min_humidity,row.humidity) 
        return [min_humidity,max_humidity]
    
    def alert_system(self) -> None :
        for row in self.rows:
            if row.temperature >35.0:
                print(f"⚠ Reading {row.timestamp}: temperature {row.temperature} exceeds threshold!")



def sensor_report(sd:SensorData) -> None :
    print("=== Sensor Report ===")
    print(f"Sensor: {sd.rows[0].sensor_name}")
    print(f"Readings: {len(sd.rows)}\n")

    print("Temperature:")
    print(f"  Average : {sd.average_temperature():.2f}")
    min_max_temp = sd.min_max_temperature()
    print(f"  Min     : {min_max_temp[0]}")
    print(f"  Max     : {min_max_temp[1]}\n")

    print("Humidity:")
    print(f"  Average : {sd.average_humidity():.2f}")
    min_max_temp = sd.min_max_humidity()
    print(f"  Min     : {min_max_temp[0]}")
    print(f"  Max     : {min_max_temp[1]}\n")
    
    print("Alerts:")
    sd.alert_system()





if __name__ == "__main__":
    sd = SensorData()
    sensor_report(sd)