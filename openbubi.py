import os
import requests
import json
import math
from geopy.geocoders import Nominatim

def needsToBeString(variable):
	if type(variable).__name__ != "str":
		raise Exception(f"Provided parameter ({variable}) isn't a string")
def needsToBeList(variable):
	if type(variable).__name__ != "list":
		raise Exception(f"Provided parameter ({variable}) isn't a list")
def needsToBeInteger(variable):
	if type(variable).__name__ != "int":
		raise Exception(f"Provided parameter ({variable}) isn't an integer")
def needsToBeDictionary(variable):
	if type(variable).__name__ != "dict":
		raise Exception(f"Provided parameter ({variable}) isn't a dictionary")
def needsToBeFloat(variable):
	if type(variable).__name__ != "float":
		raise Exception(f"Provided parameter ({variable}) isn't a float")

class BubiUser:
	def __init__(self, mobile, pin):
		needsToBeString(mobile)
		needsToBeString(pin)
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
		return json.loads(self.info())["user"]["screen_name"]
	def getLoginKey(self):
		return json.loads(self.info())["user"]["loginkey"]
	def callOtherEndpoint(self, endpoint, userData):
		needsToBeString(endpoint)
		needsToBeDictionary(userData)
		dataToPost = userData
		dataToPost.update({"apikey": "Bbx3nGP291xEtDmq"})
		dataToPost.update({"loginkey": self.getLoginKey()})
		dataToPost.update({"show_errors": "1"})
		dataToPost.update({"domain": "bh"})
		return requests.post(
			f'https://api-budapest.nextbike.net{endpoint}',
			data = dataToPost
		).text
	def rentBike(self, bikeNumber):
		needsToBeInteger(bikeNumber)
		return self.callOtherEndpoint('/api/rent.json', {"bike": str(bikeNumber)})
	def getRentals(self):
		return self.callOtherEndpoint('/api/rentals.json', {})
	def getClosedRentals(self):
		return json.dumps(json.loads(self.getRentals())["closed_rentals"])
	def getActiveRentals(self):
		return self.callOtherEndpoint('/api/getOpenRentals.json', {})
	def getPaymentLinks(self):
		return self.callOtherEndpoint('/api/getPaymentLinks.json', {})
	def getSubscriptionInfo(self):
		linkUrl = json.loads(self.getPaymentLinks())["paymentlinks"][0]["link_url"]
		contents = requests.get(linkUrl).text
		for i in contents.splitlines():
			if "Érvényeség" in i:
				endOfSubscription = i.strip()
				endOfSubscription = endOfSubscription.replace("Érvényeség vége: ", "")
		subscriptionInfo = {}
		if "havi" in contents:
			subscriptionInfo.update({"subscription_type": "monthly"})
		elif "éves" in contents:
			subscriptionInfo.update({"subscription_type": "annual"})
		else:
			subscriptionInfo.update({"subscription_type": None})
		subscriptionInfo.update({"subscription_end": endOfSubscription})
		return json.dumps(subscriptionInfo)
	def getSubscriptionType(self):
		return json.loads(self.getSubscriptionInfo())["subscription_type"]
	def getEndOfSubscription(self):
		return json.loads(self.getSubscriptionInfo())["subscription_end"]
	def moreInfo(self):
		return self.callOtherEndpoint("/api/getUserDetails.json", {})
	def getRentalDetails(self):
		return self.callOtherEndpoint("/api/getRentalDetails.json", {})
class BubiMap:
	def listAllStations(self):
		return requests.get("https://futar.bkk.hu/api/query/v1/ws/otp/api/where/bicycle-rental.json?key=bkk-web&version=4").text
	def listAllBikes(self):
		return requests.get("https://api-budapest.nextbike.net/maps/nextbike-live.json?domains=bh").text
	def listAllBikesFormatted(self):
		return json.dumps(json.loads(self.listAllBikes())['countries'][0]['cities'][0]['places'])
	def listAllStationsFormatted(self):
		return json.dumps(json.loads(self.listAllStations())['data']['list'])
	def getNearestStations(self, lat, lon):
		needsToBeFloat(lat)
		needsToBeFloat(lon)
		stations = json.loads(self.listAllStationsFormatted())
		differences = {}
		for i in range(len(stations)):
			currentStation = stations[i]
			difference = math.sqrt(abs(currentStation["lat"] - lat)**2 + abs(currentStation["lon"] - lon)**2)
			differences.update({currentStation["name"]: difference})
		sortedDifferences = dict(sorted(differences.items(), key=lambda item: item[1]))
		return json.dumps(sortedDifferences)
	def getNearestStation(self, lat, lon):
		needsToBeFloat(lat)
		needsToBeFloat(lon)
		return next(iter(json.loads(self.getNearestStations(lat, lon))))
	def getNearestStationByAddress(self, address):
		needsToBeString(address)
		location = Nominatim(user_agent="OpenBubi").geocode(address)
		return self.getNearestStation(location.latitude, location.longitude)
	def listAllBikesOnStation(self, stationName):
		needsToBeString(stationName)
		stations = json.loads(self.listAllBikesFormatted())
		for i in range(len(stations)):
			currentStation = stations[i]
			currentStationName = currentStation["name"][5:]
			if currentStationName == stationName:
				try:
					return json.dumps(currentStation["bike_list"])
				except:
					return "No bikes in station"
	def countBikesOnStation(self, stationName):
		needsToBeString(stationName)
		return len(json.loads(self.listAllBikesOnStation(stationName)))
	def getCoordinatesOfStation(self, stationName):
		needsToBeString(stationName)
		stations = json.loads(self.listAllStationsFormatted())
		for i in range(len(stations)):
			currentStation = stations[i]
			currentStationName = currentStation["name"]
			if currentStationName == stationName:
				coordinates = {}
				coordinates.update({"lat": currentStation["lat"]})
				coordinates.update({"lon": currentStation["lon"]})
				return json.dumps(coordinates)

class BubiHelpers:
	def register(self):
		return "Coming soon..."
	def pinReset(self, mobile):
		needsToBeString(mobile)
		return "Coming soon..."
	def getNews(self):
		return requests.post(
			"https://api-budapest.nextbike.net/api/getNews.json",
			data = {
				"fallback_domain": "bh",
				"language": "hu",
				"apikey": "Bbx3nGP291xEtDmq",
				"show_errors": "1",
				"domain": "bh"
			}
		).text
