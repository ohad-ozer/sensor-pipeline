#ifndef __Sensor_h__
#define __Sensor_h__

#include <string>

namespace jb
{

class Sensor
{
public:
	Sensor(std::string name);
	std::string getName() { return m_name; }
	double randomTemperatureReading();
	double randomHumidityReading();

private:
	std::string m_name;

};

}//jb

#endif
