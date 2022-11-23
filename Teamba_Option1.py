
"""
    Functions
    1. Route Type
    2. Gas Price for (PH) 
    3. Has Ferry
    4. Bounding Box 
    5. Use Traffic
    SS
    Future Enhancements
    1. Route Type User Input (Display correct directions)
    2. Enhance the UI further
"""
import urllib.parse
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rKYdRUvO2kk0NiNjlQnZ5r9Hm0dALE3f"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if orig == "quit" or orig == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Calculating Directions...")

        if json_data["route"]["options"]["useTraffic"] == False:
            print("**********************************************")
            print("Not accurate traffic info.")
            print("**********************************************\n")
        else:
            print("**********************************************")
            print("Accurate traffic info.")
            print("**********************************************\n")

        print(Fore.YELLOW + "=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))
        """
        print("Fuel Used (Ltr): " +
              str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78)))
        print("Diesel total price: " +
              str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78 * 71.700)) + "php")
        """
        print("Longitude & Latitude of Starting Point: " +
              str(json_data["route"]["boundingBox"]["ul"]).strip("{}"))
        print("Longitude & Latitude of Destination Point: " +
              str(json_data["route"]["boundingBox"]["lr"]).strip("{}"))
        print("=============================================")
        print('\033[39m')

        print(Fore.CYAN +"=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"]) * 1.61) + " km)"))
        print("=============================================")
        print('\033[39m')

        print("Route type: " + json_data['route']['options']['routeType'])
        print("=============================================")
        print("Need Ferry: " + str(json_data['route']['hasFerry']))
        print("=============================================")
        print("END OF ANALYSIS\n")

    elif json_status == 402:
        print(Fore.RED + "**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
        print('\033[39m')

    elif json_status == 611:
        print(Fore.RED + "**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
        print('\033[39m')

    else:
        print(Fore.RED + "************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
        print('\033[39m')