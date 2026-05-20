#include "Sensor.h"
#include <random>

namespace jb
{

Sensor::Sensor(std::string name)
	: m_name(name) 
{ }

double Sensor::randomTemperatureReading() 
{
    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_real_distribution<double> dist(15.0, 40.0);

    return dist(gen);
}

double Sensor::randomHumidityReading() 
{
    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_real_distribution<double> dist(30.0, 90.0);

    return dist(gen);
}


}//jb