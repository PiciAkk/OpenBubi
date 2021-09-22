import os
import requests
import json
import math
from geopy.geocoders import Nominatim

class BubiUser:
	def __init__(self, mobile, pin):
		self.mobile = mobile
		self.pin = pin
	def info(self):
		return requests.post(
			'https://api-budapest.nextbike.net/api/login.json',
			data={
				'mobile': self.mobile,
				'pin': self.pin,
				'apikey': 'Bbx3nGP291xEtDmq',
				'show_errors': '1',
				'domain': 'bh'
			}
		).text
	def getScreenName(self):
		return json.loads(BubiUser(self.mobile, self.pin).info())["user"]["screen_name"]
	def getLoginKey(self):
		return json.loads(BubiUser(self.mobile, self.pin).info())["user"]["loginkey"]
	def rentBike(self, bikeNumber):
		return "Coming soon..."
		requests.post(
			'https://api-budapest.nextbike.net/api/rent.json',
			data={
				'bike': bikeNumber,
				'loginkey': getLoginKey(),
				'apikey': 'Bbx3nGP291xEtDmq',
				'show_errors': '1',
				'domain': 'bh'
			}
		).text
class BubiMap:
	def listAllStations(self):
		return requests.get("https://futar.bkk.hu/api/query/v1/ws/otp/api/where/bicycle-rental.json?key=bkk-web&version=4").text
	def listAllBikes(self):
		return requests.get("https://api-budapest.nextbike.net/maps/nextbike-live.json?domains=bh").text
	def listAllBikesFormatted(self):
		return json.dumps(json.loads(BubiMap().listAllBikes())['countries'][0]['cities'][0]['places'])
	def listAllStationsFormatted(self):
		return json.dumps(json.loads(BubiMap().listAllStations())['data']['list'])
	def getNearestStation(self, lat, lon):
		stations = json.loads(BubiMap().listAllStationsFormatted())
		differences = {}
		for i in range(len(stations)):
			currentStation = stations[i]
			difference = math.sqrt(abs(currentStation["lat"] - lat)**2 + abs(currentStation["lon"] - lon)**2)
			differences.update({currentStation["name"]: difference})
		sortedDifferences = dict(sorted(differences.items(), key=lambda item: item[1]))
		return next(iter(sortedDifferences))
	def getNearestStationByAddress(self, address):
		location = Nominatim(user_agent="OpenBubi").geocode(address)
		return BubiMap().getNearestStation(location.latitude, location.longitude)
	def listAllBikesOnStation(self, stationName):
		stations = json.loads(BubiMap().listAllBikesFormatted())
		for i in range(len(stations)):
			currentStation = stations[i]
			print(stationName)
			print(currentStation)
			if currentStation["name"] == stationName:
				try:
					return currentStation["bike_list"]
				except:
					return "No bikes in station"
