import datetime
import requests
import json


def flydreamzz_json(param_json, hash_id):
    origin = param_json['origin']
    destination = param_json['destination']
    depart_date = param_json['depart_date']

    ls1 = {"results": dict()}


    flight_code_json = [{"places": "Agartala", "airport_code": "IXA"}, {"places": "Ahmedabad", "airport_code": "AMD"},
                        {"places": "Aizawl", "airport_code": "AJL"}, {"places": "Aurangabad", "airport_code": "IXU"},
                        {"places": "Amritsar", "airport_code": "ATQ"}, {"places": "Bagdogra", "airport_code": "IXB"},
                        {"places": "Bengaluru", "airport_code": "BLR"},
                        {"places": "Bhubaneswar", "airport_code": "BBI"}, {"places": "Bhopal", "airport_code": "BHO"},
                        {"places": "Chandigarh", "airport_code": "IXC"}, {"places": "Chennai", "airport_code": "MAA"},
                        {"places": "Coimbatore", "airport_code": "CJB"}, {"places": "Dehradun", "airport_code": "DED"},
                        {"places": "Delhi", "airport_code": "DEL"}, {"places": "Dibrugarh", "airport_code": "DIB"},
                        {"places": "Dimapur", "airport_code": "DMU"}, {"places": "Durgapur", "airport_code": "RDP"},
                        {"places": "Gaya", "airport_code": "GAY"}, {"places": "Goa", "airport_code": "GOI"},
                        {"places": "Gorakhpur", "airport_code": "GOP"}, {"places": "Guwahati", "airport_code": "GAU"},
                        {"places": "Hubli", "airport_code": "HBX"}, {"places": "Hyderabad", "airport_code": "HYD"},
                        {"places": "Imphal", "airport_code": "IMF"}, {"places": "Indore", "airport_code": "IDR"},
                        {"places": "Jabalpur", "airport_code": "JLR"}, {"places": "Jaipur", "airport_code": "JAI"},
                        {"places": "Jammu", "airport_code": "IXJ"}, {"places": "Jodhpur", "airport_code": "JDH"},
                        {"places": "Jorhat", "airport_code": "JRH"}, {"places": "Kannur", "airport_code": "CNN"},
                        {"places": "Kurnool", "airport_code": "KJB"}, {"places": "Kochi", "airport_code": "COK"},
                        {"places": "Kolhapur", "airport_code": "KLH"}, {"places": "Kolkata", "airport_code": "CCU"},
                        {"places": "Kozhikode", "airport_code": "CCJ"}, {"places": "Lucknow", "airport_code": "LKO"},
                        {"places": "Madurai", "airport_code": "IXM"}, {"places": "Mangaluru", "airport_code": "IXE"},
                        {"places": "Mumbai", "airport_code": "BOM"}, {"places": "Mysuru", "airport_code": "MYQ"},
                        {"places": "Nagpur", "airport_code": "NAG"}, {"places": "Patna", "airport_code": "PAT"},
                        {"places": "Prayagraj", "airport_code": "IXD"}, {"places": "Pune", "airport_code": "PNQ"},
                        {"places": "Portblair", "airport_code": "IXZ"}, {"places": "Raipur", "airport_code": "RPR"},
                        {"places": "Rajahmundry", "airport_code": "RJA"}, {"places": "Ranchi", "airport_code": "IXR"},
                        {"places": "Shillong", "airport_code": "SHL"}, {"places": "Shirdi", "airport_code": "SAG"},
                        {"places": "Silchar", "airport_code": "IXS"}, {"places": "Srinagar", "airport_code": "SXR"},
                        {"places": "Surat", "airport_code": "STV"},
                        {"places": "Thiruvananthapuram", "airport_code": "TRV"},
                        {"places": "Tiruchirappalli", "airport_code": "TRZ"},
                        {"places": "Tirupati", "airport_code": "TIR"}, {"places": "Tuticorin", "airport_code": "TCR"},
                        {"places": "Udaipur", "airport_code": "UDR"}, {"places": "Vadodara", "airport_code": "BDQ"},
                        {"places": "Varanasi", "airport_code": "VNS"}, {"places": "Vijayawada", "airport_code": "VGA"},
                        {"places": "Visakhapatnam", "airport_code": "VTZ"}, {"places": "Kannur", "airport_code": "CNN"},
                        {"places": "Agartala", "airport_code": "IXA"}, {"places": "Ahmedabad", "airport_code": "AMD"},
                        {"places": "Amritsar", "airport_code": "ATQ"}, {"places": "Bagdogra", "airport_code": "IXB"},
                        {"places": "Bengaluru", "airport_code": "BLR"},
                        {"places": "Bhubaneswar", "airport_code": "BBI"}, {"places": "Bhopal", "airport_code": "BHO"},
                        {"places": "Chandigarh", "airport_code": "IXC"}, {"places": "Chennai", "airport_code": "MAA"},
                        {"places": "Coimbatore", "airport_code": "CJB"}, {"places": "Dehradun", "airport_code": "DED"},
                        {"places": "Delhi", "airport_code": "DEL"}, {"places": "Dimapur", "airport_code": "DMU"},
                        {"places": "Goa", "airport_code": "GOI"}, {"places": "Gorakhpur", "airport_code": "GOP"},
                        {"places": "Guwahati", "airport_code": "GAU"}, {"places": "Hubli", "airport_code": "HBX"},
                        {"places": "Hyderabad", "airport_code": "HYD"}, {"places": "Imphal", "airport_code": "IMF"},
                        {"places": "Indore", "airport_code": "IDR"}, {"places": "Jabalpur", "airport_code": "JLR"},
                        {"places": "Jaipur", "airport_code": "JAI"}, {"places": "Jammu", "airport_code": "IXJ"},
                        {"places": "Kolkata", "airport_code": "CCU"}, {"places": "Kozhikode", "airport_code": "CCJ"},
                        {"places": "Lucknow", "airport_code": "LKO"}, {"places": "Madurai", "airport_code": "IXM"},
                        {"places": "Mangaluru", "airport_code": "IXE"}, {"places": "Mumbai", "airport_code": "BOM"},
                        {"places": "Nagpur", "airport_code": "NAG"}, {"places": "Patna", "airport_code": "PAT"},
                        {"places": "Pune", "airport_code": "PNQ"}, {"places": "Raipur", "airport_code": "RPR"},
                        {"places": "Rajahmundry", "airport_code": "RJA"}, {"places": "Ranchi", "airport_code": "IXR"},
                        {"places": "Srinagar", "airport_code": "SXR"}, {"places": "Surat", "airport_code": "STV"},
                        {"places": "Thiruvananthapuram", "airport_code": "TRV"},
                        {"places": "Tiruchirappalli", "airport_code": "TRZ"},
                        {"places": "Tuticorin", "airport_code": "TCR"}, {"places": "Udaipur", "airport_code": "UDR"},
                        {"places": "Vadodara", "airport_code": "BDQ"}, {"places": "Varanasi", "airport_code": "VNS"},
                        {"places": "Vijayawada", "airport_code": "VGA"},
                        {"places": "Visakhapatnam", "airport_code": "VTZ"}, {"places": "Gaya", "airport_code": "GAY"},
                        {"places": "Jodhpur", "airport_code": "JDH"}, {"places": "Silchar", "airport_code": "IXS"},
                        {"places": "Belagavi", "airport_code": "IXG"}]

    url = "https://api.flydreamzz.in/getDashboard/"

    payload = "{\"filters\":{\"traveldate__contains\":\""+depart_date+"\",\"airportfrom__name\":\""+origin+"\",\"airportto__name\":\""+destination+"\"},\"username\":\"agent.sneha14\"}"
    # payload = "{\"filters\":{\"traveldate__contains\":\""+depart_date+"\",\"airportfrom__name\":\""+origin+"\",\"airportto__name\":\""+destination+"\"},\"username\":\"agent.sneha14\"}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
        # 'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4MTQyMjg2LCJqdGkiOiI1ODViZTRlNTgzNzQ0MjNkYWQ3ZDllMjQ4NjE4OTY4OSIsInVzZXJfaWQiOjQyNH0.dlaba4GNp4-qfj6o5fMJrHHGEKPF3pnsaTZwuAQKVWQ',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.flydreamzz.in',
        'Referer': 'https://www.flydreamzz.in/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    a = response.text
    print()

    json_data = json.loads(response.text)
    res_json = dict()

    if json_data['data'] == []:
        res_json['result'] = {"status": 200, "HasResults": False, "data": []}
        return res_json


    for data in json_data['data']:
        if len(json_data['data']) == 1:

            if data['bookingtype'] == 'online':
                # data[0].bookingtype
                result = {"Departure_Sector": None, "Arrival_Sector": None,
                          "Airlines": None, "Flight_number": None,
                          "No_of_stops": None, "Departure_Date_&_time": None,
                          "Arrival_Date_&_time": None,"No_of_available_seats": None,
                          "Price_per_seat": {'adult':None,'child':None,'infant':None}, "Domain": {}}

                result["Departure_Sector"] = data['destination'].split(" ")[0]
                # print(result["Departure_Sector"])

                for i in flight_code_json:

                    if i['airport_code'] == result["Departure_Sector"]:
                        result["Departure_Sector"] = i['places']


                result['Arrival_Sector'] = data['destination'].split(" ")[2]

                for j in flight_code_json:

                    if j['airport_code'] == result['Arrival_Sector']:
                        result['Arrival_Sector'] = j['places']

                try:
                    result['Airlines'] = data['airlines']
                except:
                    result['Airlines'] = data = None
                try:
                    result['Flight_number'] = data['flightno']
                except:
                    result['Flight_number'] = data = None

                try:
                    Departure_Time = str(data['departure'])[0:5]

                    Departure_Time = datetime.datetime.strptime(Departure_Time, "%H:%M").strftime("%I:%M %p")
                except:
                    Departure_Time = None
                print()
                travel_Date = str(data['traveldate']).split("-")
                travel_Date.reverse()
                travel_Date = str("-".join(travel_Date))

                try:
                    result['Departure_Date_&_time'] = travel_Date + " " + Departure_Time
                except:
                    result['Departure_Date_&_time'] = None

                try:
                    Arrival_Time = str(data['arrival'])[0:5]
                    Arrival_Time = datetime.datetime.strptime(Arrival_Time, "%H:%M").strftime("%I:%M %p")
                except:
                    Arrival_Time = None

                try:
                    result['Arrival_Date_&_time'] = travel_Date + " " + Arrival_Time
                except:
                    result['Arrival_Date_&_time'] = None
                result['No_of_stops'] = ''
                try:
                    result['No_of_available_seats'] = data['availableseats']
                except:
                    result['No_of_available_seats'] = None
                try:
                    result['Price_per_seat']['adult'] = data['deal']
                except:
                    result['Price_per_seat']['adult'] = None
                try:
                    result['Price_per_seat']['child'] = data['deal']
                except:
                    result['Price_per_seat']['child'] = None
                try:
                    result['Price_per_seat']['infant'] = data['deal']
                except:
                    result['Price_per_seat']['infant'] = None
                result['Domain'] = 'flydreamzz.in'

                res_json['results'] = {"status": 200, "HasResults": True, "data": [result]}
                return res_json
            else:
                result = []
                res_json['results'] = {"status": 200, "HasResults": True, "data": [result]}
                return res_json['results']
        else:
            ls = []
            if data['bookingtype'] == 'online':
                # data[0].bookingtype
                result = {"Departure_Sector": None, "Arrival_Sector": None,
                          "Airlines": None, "Flight_number": None,
                          "No_of_stops": None, "Departure_Date_&_time": None,
                          "Arrival_Date_&_time": None, "No_of_available_seats": None,
                          "Price_per_seat": {'adult': None, 'child': None, 'infant': None}, "Domain": {}}

                result["Departure_Sector"] = data['destination'].split(" ")[0]
                print(result["Departure_Sector"])

                for i in flight_code_json:

                    if i['airport_code'] == result["Departure_Sector"]:
                        result["Departure_Sector"] = i['places']

                result['Arrival_Sector'] = data['destination'].split(" ")[2]

                for j in flight_code_json:

                    if j['airport_code'] == result['Arrival_Sector']:
                        result['Arrival_Sector'] = j['places']

                try:
                    result['Airlines'] = data['airlines']
                except:
                    result['Airlines'] = data = None
                try:
                    result['Flight_number'] = data['flightno']
                except:
                    result['Flight_number'] = data = None

                try:
                    Departure_Time = str(data['departure'])[0:5]

                    Departure_Time = datetime.datetime.strptime(Departure_Time, "%H:%M").strftime("%I:%M %p")
                except:
                    Departure_Time = None

                travel_Date = str(data['traveldate']).split("-")
                travel_Date.reverse()
                travel_Date = str("-".join(travel_Date))

                try:
                    result['Departure_Date_&_time'] = travel_Date + " " + Departure_Time
                except:
                    result['Departure_Date_&_time'] = None

                try:
                    Arrival_Time = str(data['arrival'])[0:5]
                    Arrival_Time = datetime.datetime.strptime(Arrival_Time, "%H:%M").strftime("%I:%M %p")
                except:
                    Arrival_Time = None

                try:
                    result['Arrival_Date_&_time'] = travel_Date + " " + Arrival_Time
                except:
                    result['Arrival_Date_&_time'] = None
                result['No_of_stops'] = ''
                try:
                    result['No_of_available_seats'] = data['availableseats']
                except:
                    result['No_of_available_seats'] = None
                try:
                    result['Price_per_seat']['adult'] = data['deal']
                except:
                    result['Price_per_seat']['adult'] = None
                try:
                    result['Price_per_seat']['child'] = data['deal']
                except:
                    result['Price_per_seat']['child'] = None
                try:
                    result['Price_per_seat']['infant'] = data['deal']
                except:
                    result['Price_per_seat']['infant'] = None
                result['Domain'] = 'flydreamzz.in'

                ls.append(result)

            res_json['results'] = {"status": 200, "HasResults": True, "data": ls}
            return res_json

if __name__ == '__main__':
    # data = get_json("AMD", "DXB", "yes", "economy", "2022-09-03", "2022-09-23", 1, 1, 1, 12345)
    param_json = {
        "origin": "BLR",
        "destination": "CCU",
        "is_return": '',
        "flight_class": "",
        "depart_date": "2023-01-01",  # "01-09-2022"
        "return_date": "",
        "adult": "1",
        "child": "0",
        "infant": "0",
        "domain": "flydreamzz",
        "key": "test-xbyte"
    }
    data = flydreamzz_json(param_json, 12345)
    print(json.dumps(data))
# IXB to CCU"