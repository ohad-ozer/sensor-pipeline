#include "Sensor.h"
#include <iostream>
#include <fstream>
#include <chrono>
#include <thread>
#include <iomanip>

int main()
{
	std::ofstream file("sensor_data.csv");

	if (!file) {
		std::cout << "Failed to open file\n";
		return 1;
	}

	file << "timestamp, sensor_name, temperature, humidity" << "\n";
	jb::Sensor s1{ "sensor_1" };

	for (int i = 1;i <= 20;++i)
	{
		std::this_thread::sleep_for(std::chrono::seconds(1));
		double humidity = s1.randomHumidityReading();
		double temperature = s1.randomTemperatureReading();

		std::cout << i;
		std::cout << ',' << s1.getName();
		std::cout << ',' << std::fixed << std::setprecision(2) << temperature;
		std::cout << ',' << std::fixed << std::setprecision(2) << humidity << std::endl;

		file << i;
		file << ',' << s1.getName();
		file << ',' << std::fixed << std::setprecision(2) << temperature;
		file << ',' << std::fixed << std::setprecision(2) << humidity << "\n";
	}

	file.close();

	return 0;
}
