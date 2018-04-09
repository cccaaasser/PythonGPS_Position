import serial
import logging

gps = serial.Serial("/dev/ttyUSB1", baudrate = 9600)
format_time = '%(asctime)s %(message)s'
logging.basicConfig(filename='gps_logging.log', level=logging.INFO,format=format_time, datefmt='%m/%d/%Y %I:%M:%S %p')

while True:
    line = gps.readline()
    data = line.split(",")
    if data[0] == "$GPRMC":
        if data[2] == "A":

            latgps = float(data[3])
            if data[4] == "S":
                latgps = -latgps

            latdeg = int(latgps/100)
            latmin = latgps - latdeg*100
            lat = latdeg+(latmin/60)

            longps = float(data[5])
            if data[6] == "W":
                longps = -longps

            londeg = int(longps/100)
            lonmin = longps - londeg*100
            lon = londeg+(lonmin/60)
            
            logging.info(">> Latitude: %s" % lat)
            logging.info(">> Longitude: %s" % lon)

    if data[0] == "$GPVTG":
        if data[8] == 'K':
	    speed = float(data[7])

	logging.info(">> Speed: %s" % speed + " Km/h")
