import openbubi
import json # for converting the command-line output to dictionary
import os # for running termux-location
import urllib.parse # for parsing urls

Budapest = openbubi.BubiMap()

currentLocation = os.popen("termux-location").read() # read the current location

currentLocationDict = json.loads(currentLocation) # convert it to a dictionary

lat = currentLocationDict["latitude"]; lon = currentLocationDict["longitude"] # parse it

nearestStation = Budapest.getNearestStation(lat, lon) # call getNearestStation(), and provide lat, lon
# this will return the nearest station's name

nearestStationInfo = {
  "name": nearestStation,
  "bikesOnStation": Budapest.countBikesOnStation(nearestStation), # count the bikes on that station
  "coordinates": json.loads(Budapest.getCoordinateOfStation(nearestStation)) # get the coordinates of that station, and convert it to a dictionary
}

startingPoint = urllib.parse.quote(f"{lat},{lon}")
# make a starting point in a url-friendly format (based on the current coordinates)
destinationPoint = urllib.parse.quote(f"{nearestStationInfo['coordinates']['lat']},{nearestStationInfo['coordinates']['lon']}")
# make an ending point in a url-friendly format (based on the station's coordinates)
googlemapsurl = f"https://www.google.com/maps?f=d&saddr={startingPoint}&daddr={destinationPoint}&dirflg=d"
# generate the Google Maps URL

# ^
# |
# calculate a Google Maps route to the station

print(
 f"""
 Station found...

 Informations:

 - Station name: {nearestStationInfo["name"]}
 - Bikes on station: {nearestStationInfo["bikesOnStation"]}
 - Coordinates of station: {nearestStationInfo["coordinates"]}
 - Google Maps route to the station: {googlemapsurl}
 """
)
# printing out
