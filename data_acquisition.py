# Awais Akram, Zhenxiang Chen, Michele Sallaku, Mattia Zani - AstroPi 2018-2019
# Enviroment data acquisition

import csv
import subprocess
from time import gmtime, strftime
import ephem
# from sense_hat import SenseHat

class data_acq:
    text_speed = 0.1
    # Init sensehat
    def __init__(self, sense_hat):
        self.sense = sense_hat
    
    def read_temp(self, show_data):
        cputemp = subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True)
        cputemp = float(cputemp) / 1000
        temp = self.sense.get_temperature_from_pressure() + self.sense.get_temperature_from_humidity() + self.sense.get_temperature()
        temp = temp / 3
        goodtemp = temp - ((cputemp - temp) / 1.65)
        goodtemp = round(goodtemp, 1)
        # print (time.strftime('%x %X'))
        # print (goodtemp)
        if show_data == True:
            strtemp = str(goodtemp)
            if goodtemp >= 25:
                self.sense.show_message(strtemp + "'c", text_colour=(155,50,50), scroll_speed=self.text_speed)
            elif goodtemp < 20:
                self.sense.show_message(strtemp + "'c", text_colour=(0,100,255), scroll_speed=self.text_speed)
            else :
                self.sense.show_message(strtemp + "'c", text_colour=(155,155,155), scroll_speed=self.text_speed)
        return goodtemp
    
    def read_humidity(self, show_data):
        humidity = self.sense.get_humidity()
        humidity = round(humidity, 1)
        # print (humidity)
        if show_data == True:
            strhumidity = "Humidity" + str(humidity) + "%"
            if humidity < 65:
                self.sense.show_message(strhumidity, text_colour=(150,255,255), scroll_speed=self.text_speed)
            else:
                self.sense.show_message(strhumidity, text_colour=(0,50,255), scroll_speed=self.text_speed)
        return humidity
    
    def read_pressure(self, show_data):
        pressure = self.sense.get_pressure()
        pressure = round(pressure, 0)
        # print (pressure)
        if show_data == True:
            strpressure = str(pressure)
            self.sense.show_message(strpressure + "mbar", text_colour=(255,183,50), scroll_speed=self.text_speed)
        return pressure

    def read_position(self):
        name = "ISS (ZARYA)"
        line1 = "1 25544U 98067A   19024.69130787  .00000289  00000-0  11946-4 0  9991"
        line2 = "2 25544  51.6429 354.9058 0004630 308.2748  50.7575 15.53168972152956"
        iss = ephem.readtle(name, line1, line2)
        iss.compute()
        iss_lat = str(iss.sublat)
        iss_long = str(iss.sublong)
        return iss_lat, iss_long

    def write_data(self, out_file, show_data):
        lat, long = self.read_position()
        temp = self.read_temp(show_data)
        humidity = self.read_humidity(show_data)
        pressure = self.read_pressure(show_data)
        p_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        data_array = [lat, long, p_time, temp, humidity, pressure]
        print(data_array)
        with out_file:
            writer = csv.writer(out_file)
            writer.writerow(data_array)
#        out_file.close()

'''
sense = SenseHat()
read = data_acq(sense)
while True:
    data = open('dati.csv', 'a')
    read.write_data(data)
'''