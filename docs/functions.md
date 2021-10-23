# Bult-in functions

## `BubiUser(phoneNumber, pin)`

- `info()` - returns information in JSON (not dictionary) format -> if you want it in dictionary format, `import json`, and use `json.loads(info())`
- `getScreenName()` - grabs the screen name from `info()`, and returns it
- `getLoginKey()` - grabs the login key from `info()`, and returns it
- `callOtherEndpoint(relativeURL, data)` (*relativeURL needs to be a string, and data needs to be a dictionary*) - calls the specified `endpoint` with the specified `data` (plus `loginkey`, `domain`, `apikey`, `show_errors`), and returns the output. (*you can find endpoints [here](https://github.com/h0chi/nextbike-api-reverse-engineering)*)
- `rentBike(bikeNumber)` (*bikeNumber needs to be a string*) - rents a bike, and returns the output
- `getRentals()` - returns information about the user's rentals
- `getClosedRentals()` - returns closed rentals from `getRentals()`
- `getActiveRentals()` - returns active rentals
- `getPaymentLinks()` - returns information about payment links
- `getSubscriptionInfo()` - returns the end of the subscription, and the type of the subscription
- `getSubScriptionType()` - returns the type of the subscription based on `getSubscriptionInfo()` (monthly, or annual)
- `getEndOfSubscription()` - returns the end of the subscription based on `getSubscriptionInfo()` (date)
- `moreInfo()` - returns a LOT of information about the user
- `getRentalDetails()` - returns information about the current rental
- `register()` - *Work in progress...*

## `BubiMap()`

- `listAllStations()` - returns a JSON object containing all stations
- `listAllBikes()` - returns a JSON object containing all bikes
- `listAllBikesFormatted()` - returns a JSON object containing all bikes (without the unnecessary parts)
- `listAllStationsFormatted()` - returns a JSON object containing all stations (without the unnecessary parts)
- `getNearestStation(lat, lon)` - (*lat, and lon needs to be a string*) returns the nearest station's name by latitude, and longitude (Using the Pythagorean theorem)
- `getNearestStationByAddress(address)` - returns the nearest station's name by address (using `getNearestStation()`, and OpenStreetMap API)
- `listAllBikesOnStations(stationName)` - returns all the bikes on a station (and the number of these bikes, and information about these bikes)
- `countBikesOnStation(stationName)` - counts all the bikes on a station (using `listAllBikesOnStation()`), and returns the counter
- `getCoordinateOfStation(stationName)` - returns the coordinates of a station (latitude, longitude)
