import json
import time

import requests


def get_json(Origin, Destination, isreturn, FlightClass, DepartDate, ReturnDate, Adult, Child, Infant, hashId):
    ls = []
    api_response = []
    if isreturn.lower() == "yes":
        if FlightClass.lower() == "economy":
            FlightClass = "Y"
        elif FlightClass.lower() == "business":
            FlightClass = "C"
        elif FlightClass.lower() == "firstclass":
            FlightClass = "F"
        elif FlightClass.lower() == "premium economy":
            FlightClass = "W"

        isreturn = "RoundTrip"
        url = "https://www.makevoyage.com/dispatch.jsp?opid=FS000&actioncode=FSAPI&agentid=MV24858"

        payload = f"xmlorjson=%3Cflightsearchrequest%3E%3Ccredentials%3E%3Cusername%3EAPIUSER%3C%2Fusername%3E%3Cpassword%3EAPIUSER%3C%2Fpassword%3E%3Cofficeid%3ESUPER%3C%2Fofficeid%3E%3C%2Fcredentials%3E%3Corigin%3E{Origin}%3C%2Forigin%3E%3Cdestination%3E{Destination}%3C%2Fdestination%3E%3Conwarddate%3E{DepartDate}%3C%2Fonwarddate%3E%3Creturndate%3E{ReturnDate}%3C%2Freturndate%3E%3Cnumadults%3E{Adult}%3C%2Fnumadults%3E%3Cnumchildren%3E{Child}%3C%2Fnumchildren%3E%3Cnuminfants%3E{Infant}%3C%2Fnuminfants%3E%3Cjourneytype%3E{isreturn}%3C%2Fjourneytype%3E%3Cprefclass%3E{FlightClass}%3C%2Fprefclass%3E%3Crequestformat%3EJSON%3C%2Frequestformat%3E%3Cresultformat%3EJSON%3C%2Fresultformat%3E%3Csearchtype%3Enormal%3C%2Fsearchtype%3E%3Csortkey%3Ecf409041-7d12-4af5-8636-a8247248db1d%3C%2Fsortkey%3E%3Cissbt%3Efalse%3C%2Fissbt%3E%3Cprofileid%3E%3C%2Fprofileid%3E%3Cnumresults%3E100%3C%2Fnumresults%3E%3Cactionname%3EFLIGHTSEARCH%3C%2Factionname%3E%3Cpreddeptimewindow%3Enull%3C%2Fpreddeptimewindow%3E%3Cprefarrtimewindow%3Enull%3C%2Fprefarrtimewindow%3E%3Cprefcarrier%3E6E%3C%2Fprefcarrier%3E%3Cexcludecarriers%2F%3E%3Crefundtype%3EAll%3C%2Frefundtype%3E%3Clayovertime%3E%3C%2Flayovertime%3E%3C%2Fflightsearchrequest%3E"
        headers = {
            'accept': 'text/html, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'connection': 'keep-alive',
            'content-length': '1146',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'JSESSIONID=D55315A521606D3AC4F9ABA2FCB66CA1',
            'host': 'www.makevoyage.com',
            'origin': 'https://www.makevoyage.com',
            'referer': f'https://www.makevoyage.com/flight_roundTrip_search_new.jsp?fromFlight={Origin}&toFlight={Destination}&departureDateFlight={DepartDate}&arrivalDateFlight={ReturnDate}&adultFlight={Adult}&childFlight={Child}&infantFlight={Infant}&journyType={isreturn}&lat1=undefined&longi1=undefined&lat2=undefined&longi2=undefined&prefairline=All&pclass={FlightClass}&searchtype=domestic&lg=English&refundtype=All&layovertime=&apa=&directflights=false&defenceflight=false&studentflight=false&personalbooking=no',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        json_data = json.loads(response.text)

        if json_data['flightsearchresponse']['totalresults'] == 0:
            url = "https://www.makevoyage.com/dispatch.jsp?opid=FS000&actioncode=FSAPI&agentid=MV24858"

            payload = f"xmlorjson=%3Cflightsearchrequest%3E%3Ccredentials%3E%3Cusername%3EAPIUSER%3C%2Fusername%3E%3Cpassword%3EAPIUSER%3C%2Fpassword%3E%3Cofficeid%3ESUPER%3C%2Fofficeid%3E%3C%2Fcredentials%3E%3Corigin%3E{Origin}%3C%2Forigin%3E%3Cdestination%3E{Destination}%3C%2Fdestination%3E%3Conwarddate%3E{DepartDate}%3C%2Fonwarddate%3E%3Creturndate%3E{ReturnDate}%3C%2Freturndate%3E%3Cnumadults%3E{Adult}%3C%2Fnumadults%3E%3Cnumchildren%3E{Child}%3C%2Fnumchildren%3E%3Cnuminfants%3E{Infant}%3C%2Fnuminfants%3E%3Cjourneytype%3E{isreturn}%3C%2Fjourneytype%3E%3Cprefclass%3E{FlightClass}%3C%2Fprefclass%3E%3Crequestformat%3EJSON%3C%2Frequestformat%3E%3Cresultformat%3EJSON%3C%2Fresultformat%3E%3Csearchtype%3Enormal%3C%2Fsearchtype%3E%3Csortkey%3E23315592-1e29-419e-806c-02834521ef6e%3C%2Fsortkey%3E%3Cissbt%3Efalse%3C%2Fissbt%3E%3Cprofileid%3E%3C%2Fprofileid%3E%3Cnumresults%3E100%3C%2Fnumresults%3E%3Cactionname%3EFLIGHTSEARCH%3C%2Factionname%3E%3Cpreddeptimewindow%3Enull%3C%2Fpreddeptimewindow%3E%3Cprefarrtimewindow%3Enull%3C%2Fprefarrtimewindow%3E%3Cprefcarrier%3EAll%3C%2Fprefcarrier%3E%3Cexcludecarriers%2F%3E%3Crefundtype%3EAll%3C%2Frefundtype%3E%3Clayovertime%3E%3C%2Flayovertime%3E%3C%2Fflightsearchrequest%3E"
            headers = {
                'accept': 'text/html, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9,de;q=0.8',
                'connection': 'keep-alive',
                'content-length': '1147',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'JSESSIONID=D55315A521606D3AC4F9ABA2FCB66CA1',
                'host': 'www.makevoyage.com',
                'origin': 'https://www.makevoyage.com',
                'referer': f'https://www.makevoyage.com/flight_roundTrip_search_new.jsp?fromFlight={Origin}&toFlight={Destination}&departureDateFlight={DepartDate}&arrivalDateFlight={ReturnDate}&adultFlight={Adult}&childFlight={Child}&infantFlight={Infant}&journyType={isreturn}&lat1=undefined&longi1=undefined&lat2=undefined&longi2=undefined&prefairline=All&pclass={FlightClass}&searchtype=international&lg=English&refundtype=All&layovertime=&apa=&directflights=false&defenceflight=false&studentflight=false&personalbooking=no',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            json_data = json.loads(response.text)

            for data in json_data['flightsearchresponse']['flightjourneys']:
                for info in data['flightoptions']:
                    for details in info['recommendedflight']:
                        result = {"result": [{"Price_per_seat": {}, "flight_data": {}, "Domain": {}}]}

                        result['result'][0]['Price_per_seat']['adult'] = details['flightfare']['adultbasefare']
                        result['result'][0]['Price_per_seat']['child'] = details['flightfare']['childbasefare']
                        result['result'][0]['Price_per_seat']['infant'] = details['flightfare']['infantbasefare']
                        result['result'][0]['Domain'] = "travelsansaar"

                        for main_data in details['flightlegs']:

                            try:
                                result['result'][0]['flight_data']['Departure_Sector'] = main_data['origin_name']
                            except:
                                result['result'][0]['flight_data']['Departure_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Sector'] = main_data['destination_name']
                            except:
                                result['result'][0]['flight_data']['Arrival_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Airlines'] = main_data['carriername']
                            except:
                                result['result'][0]['flight_data']['Airlines'] = ''
                            try:
                                result['result'][0]['flight_data']['Flight_number'] = main_data['flightnumber']
                            except:
                                result['result'][0]['flight_data']['Flight_number'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_stops'] = main_data['stopover']
                            except:
                                result['result'][0]['flight_data']['No_of_stops'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Date'] = main_data['depdate']
                            except:
                                result['result'][0]['flight_data']['Departure_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Time'] = main_data['deptime']
                            except:
                                result['result'][0]['flight_data']['Departure_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Date'] = main_data['arrdate']
                            except:
                                result['result'][0]['flight_data']['Arrival_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Time'] = main_data['arrtime']
                            except:
                                result['result'][0]['flight_data']['Arrival_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_available_seats'] = main_data[
                                    'numseatsavailable']
                            except:
                                result['result'][0]['flight_data']['No_of_available_seats'] = ''

                            api_response.append(result)

                        for i in api_response:
                            if i in ls:
                                continue
                            else:
                                ls.append(result)
            return ls





        # flightsearchresponse.flightjourneys[0].flightoptions[9].recommendedflight[0].flightlegs
        else:
            for data in json_data['flightsearchresponse']['flightjourneys']:
                for info in data['flightoptions']:
                    for details in info['recommendedflight']:
                        result = {"result": [{"Price_per_seat": {}, "flight_data": {}, "Domain": {}}]}

                        result['result'][0]['Price_per_seat']['adult'] = details['flightfare']['adultbasefare']
                        result['result'][0]['Price_per_seat']['child'] = details['flightfare']['childbasefare']
                        result['result'][0]['Price_per_seat']['infant'] = details['flightfare']['infantbasefare']
                        result['result'][0]['Domain'] = "travelsansaar"

                        for main_data in details['flightlegs']:

                            try:
                                result['result'][0]['flight_data']['Departure_Sector'] = main_data['origin_name']
                            except:
                                result['result'][0]['flight_data']['Departure_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Sector'] = main_data['destination_name']
                            except:
                                result['result'][0]['flight_data']['Arrival_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Airlines'] = main_data['carriername']
                            except:
                                result['result'][0]['flight_data']['Airlines'] = ''
                            try:
                                result['result'][0]['flight_data']['Flight_number'] = main_data['flightnumber']
                            except:
                                result['result'][0]['flight_data']['Flight_number'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_stops'] = main_data['stopover']
                            except:
                                result['result'][0]['flight_data']['No_of_stops'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Date'] = main_data['depdate']
                            except:
                                result['result'][0]['flight_data']['Departure_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Time'] = main_data['deptime']
                            except:
                                result['result'][0]['flight_data']['Departure_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Date'] = main_data['arrdate']
                            except:
                                result['result'][0]['flight_data']['Arrival_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Time'] = main_data['arrtime']
                            except:
                                result['result'][0]['flight_data']['Arrival_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_available_seats'] = main_data[
                                    'numseatsavailable']
                            except:
                                result['result'][0]['flight_data']['No_of_available_seats'] = ''

                                api_response.append(result)
                        for i in api_response:
                            if i in ls:
                                continue
                            else:
                                ls.append(result)
            return ls



    elif isreturn.lower() == "no":
        isreturn = "OneWay"
        if FlightClass.lower() == "economy":
            FlightClass = "Y"
        elif FlightClass.lower() == "business":
            FlightClass = "C"
        elif FlightClass.lower() == "firstclass":
            FlightClass = "F"
        elif FlightClass.lower() == "premium economy":
            FlightClass = "W"

        url = "https://www.makevoyage.com/dispatch.jsp?opid=FS000&actioncode=FSAPI&agentid=MV24858"

        payload = f"xmlorjson=%3Cflightsearchrequest%3E%3Ccredentials%3E%3Cusername%3EAPIUSER%3C%2Fusername%3E%3Cpassword%3EAPIUSER%3C%2Fpassword%3E%3Cofficeid%3ESUPER%3C%2Fofficeid%3E%3C%2Fcredentials%3E%3Corigin%3E{Origin}%3C%2Forigin%3E%3Cdestination%3E{Destination}%3C%2Fdestination%3E%3Conwarddate%3E{DepartDate}%3C%2Fonwarddate%3E%3Creturndate%3E%3C%2Freturndate%3E%3Cnumadults%3E{Adult}%3C%2Fnumadults%3E%3Cnumchildren%3E{Child}%3C%2Fnumchildren%3E%3Cnuminfants%3E{Infant}%3C%2Fnuminfants%3E%3Cjourneytype%3E{isreturn}%3C%2Fjourneytype%3E%3Cprefclass%3E{FlightClass}%3C%2Fprefclass%3E%3Crequestformat%3EJSON%3C%2Frequestformat%3E%3Cresultformat%3EJSON%3C%2Fresultformat%3E%3Csearchtype%3Enormal%3C%2Fsearchtype%3E%3Csortkey%3E80a27e50-4ea9-4a34-9b7f-5ffb86d7786e%3C%2Fsortkey%3E%3Cissbt%3Efalse%3C%2Fissbt%3E%3Cprofileid%3E%3C%2Fprofileid%3E%3Cnumresults%3E100%3C%2Fnumresults%3E%3Cactionname%3EFLIGHTSEARCH%3C%2Factionname%3E%3Cpreddeptimewindow%3Enull%3C%2Fpreddeptimewindow%3E%3Cprefarrtimewindow%3Enull%3C%2Fprefarrtimewindow%3E%3Cprefcarrier%3EAll%3C%2Fprefcarrier%3E%3Cexcludecarriers%2F%3E%3Crefundtype%3EAll%3C%2Frefundtype%3E%3Clayovertime%3E%3C%2Flayovertime%3E%3C%2Fflightsearchrequest%3E"
        headers = {
            'accept': 'text/html, */*; q=0.01',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'connection': 'keep-alive',
            'content-length': '1134',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'JSESSIONID=1C09455FEADCDCEA14F6E5BFE7280191',
            'host': 'www.makevoyage.com',
            'origin': 'https://www.makevoyage.com',
            'referer': f'https://www.makevoyage.com/flight_result_new.jsp?fromFlight={Origin}&toFlight={Destination}&departureDateFlight={DepartDate}&arrivalDateFlight={ReturnDate}&adultFlight={Adult}&childFlight={Child}&infantFlight={Infant}&journyType={isreturn}&lat1=undefined&longi1=undefined&lat2=undefined&longi2=undefined&prefairline=All&pclass={FlightClass}&searchtype=international&lg=English&refundtype=All&layovertime=&apa=&storelogs=false&directflights=false&defenceflight=false&studentflight=false&personalbooking=no',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        json_data = json.loads(response.text)

        if json_data['flightsearchresponse']['totalresults'] == 0:
            url = "https://www.makevoyage.com/dispatch.jsp?opid=FS000&actioncode=FSAPI&agentid=MV24858"

            payload = f"xmlorjson=%3Cflightsearchrequest%3E%3Ccredentials%3E%3Cusername%3EAPIUSER%3C%2Fusername%3E%3Cpassword%3EAPIUSER%3C%2Fpassword%3E%3Cofficeid%3ESUPER%3C%2Fofficeid%3E%3C%2Fcredentials%3E%3Corigin%3E{Origin}%3C%2Forigin%3E%3Cdestination%3E{Destination}%3C%2Fdestination%3E%3Conwarddate%3E{DepartDate}%3C%2Fonwarddate%3E%3Creturndate%3E%3C%2Freturndate%3E%3Cnumadults%3E{Adult}%3C%2Fnumadults%3E%3Cnumchildren%3E{Child}%3C%2Fnumchildren%3E%3Cnuminfants%3E{Infant}%3C%2Fnuminfants%3E%3Cjourneytype%3E{isreturn}%3C%2Fjourneytype%3E%3Cprefclass%3E{FlightClass}%3C%2Fprefclass%3E%3Crequestformat%3EJSON%3C%2Frequestformat%3E%3Cresultformat%3EJSON%3C%2Fresultformat%3E%3Csearchtype%3Enormal%3C%2Fsearchtype%3E%3Csortkey%3E60c32e36-8dcf-435e-bd1b-ce37ceda1d51%3C%2Fsortkey%3E%3Cissbt%3Efalse%3C%2Fissbt%3E%3Cprofileid%3E%3C%2Fprofileid%3E%3Cnumresults%3E100%3C%2Fnumresults%3E%3Cactionname%3EFLIGHTSEARCH%3C%2Factionname%3E%3Cpreddeptimewindow%3Enull%3C%2Fpreddeptimewindow%3E%3Cprefarrtimewindow%3Enull%3C%2Fprefarrtimewindow%3E%3Cprefcarrier%3E6E%3C%2Fprefcarrier%3E%3Cexcludecarriers%2F%3E%3Crefundtype%3EAll%3C%2Frefundtype%3E%3Clayovertime%3E%3C%2Flayovertime%3E%3C%2Fflightsearchrequest%3E"
            headers = {
                'accept': 'text/html, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9,de;q=0.8',
                'connection': 'keep-alive',
                'content-length': '1133',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'JSESSIONID=1C09455FEADCDCEA14F6E5BFE7280191',
                'host': 'www.makevoyage.com',
                'origin': 'https://www.makevoyage.com',
                'referer': f'https://www.makevoyage.com/flight_result_new.jsp?fromFlight={Origin}&toFlight={Destination}&departureDateFlight={DepartDate}&arrivalDateFlight={ReturnDate}&adultFlight={Adult}&childFlight={Child}&infantFlight={Infant}&journyType={isreturn}&lat1=undefined&longi1=undefined&lat2=undefined&longi2=undefined&prefairline=All&pclass={FlightClass}&searchtype=domestic&lg=English&refundtype=All&layovertime=&apa=&storelogs=false&directflights=false&defenceflight=false&studentflight=false&personalbooking=no',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            json_data = json.loads(response.text)

            for data in json_data['flightsearchresponse']['flightjourneys']:
                for info in data['flightoptions']:
                    for details in info['recommendedflight']:

                        result = {"result": [{"Price_per_seat": {}, "flight_data": {}, "Domain": {}}]}

                        result['result'][0]['Price_per_seat']['adult'] = details['flightfare']['adultbasefare']
                        result['result'][0]['Price_per_seat']['child'] = details['flightfare']['childbasefare']
                        result['result'][0]['Price_per_seat']['infant'] = details['flightfare']['infantbasefare']
                        result['result'][0]['Domain'] = "travelsansaar"

                        for main_data in details['flightlegs']:

                            try:
                                result['result'][0]['flight_data']['Departure_Sector'] = main_data['origin_name']
                            except:
                                result['result'][0]['flight_data']['Departure_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Sector'] = main_data['destination_name']
                            except:
                                result['result'][0]['flight_data']['Arrival_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Airlines'] = main_data['carriername']
                            except:
                                result['result'][0]['flight_data']['Airlines'] = ''
                            try:
                                result['result'][0]['flight_data']['Flight_number'] = main_data['flightnumber']
                            except:
                                result['result'][0]['flight_data']['Flight_number'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_stops'] = main_data['stopover']
                            except:
                                result['result'][0]['flight_data']['No_of_stops'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Date'] = main_data['depdate']
                            except:
                                result['result'][0]['flight_data']['Departure_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Time'] = main_data['deptime']
                            except:
                                result['result'][0]['flight_data']['Departure_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Date'] = main_data['arrdate']
                            except:
                                result['result'][0]['flight_data']['Arrival_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Time'] = main_data['arrtime']
                            except:
                                result['result'][0]['flight_data']['Arrival_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_available_seats'] = main_data[
                                    'numseatsavailable']
                            except:
                                result['result'][0]['flight_data']['No_of_available_seats'] = ''

                                api_response.append(result)

                                for i in api_response:
                                    if i in ls:
                                        continue
                                    else:
                                        ls.append(result)
                    return ls


        else:
            for data in json_data['flightsearchresponse']['flightjourneys']:
                for info in data['flightoptions']:
                    for details in info['recommendedflight']:
                        result = {"result": [{"Price_per_seat": {}, "flight_data": {}, "Domain": {}}]}

                        # result[0].Price_per_seat

                        result['result'][0]['Price_per_seat']['adult'] = details['flightfare']['adultbasefare']
                        result['result'][0]['Price_per_seat']['child'] = details['flightfare']['childbasefare']
                        result['result'][0]['Price_per_seat']['infant'] = details['flightfare']['infantbasefare']
                        result['result'][0]['Domain'] = "travelsansaar"

                        for main_data in details['flightlegs']:

                            try:
                                result['result'][0]['flight_data']['Departure_Sector'] = main_data['origin_name']
                            except:
                                result['result'][0]['flight_data']['Departure_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Sector'] = main_data['destination_name']
                            except:
                                result['result'][0]['flight_data']['Arrival_Sector'] = ''
                            try:
                                result['result'][0]['flight_data']['Airlines'] = main_data['carriername']
                            except:
                                result['result'][0]['flight_data']['Airlines'] = ''
                            try:
                                result['result'][0]['flight_data']['Flight_number'] = main_data['flightnumber']
                            except:
                                result['result'][0]['flight_data']['Flight_number'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_stops'] = main_data['stopover']
                            except:
                                result['result'][0]['flight_data']['No_of_stops'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Date'] = main_data['depdate']
                            except:
                                result['result'][0]['flight_data']['Departure_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Departure_Time'] = main_data['deptime']
                            except:
                                result['result'][0]['flight_data']['Departure_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Date'] = main_data['arrdate']
                            except:
                                result['result'][0]['flight_data']['Arrival_Date'] = ''
                            try:
                                result['result'][0]['flight_data']['Arrival_Time'] = main_data['arrtime']
                            except:
                                result['result'][0]['flight_data']['Arrival_Time'] = ''
                            try:
                                result['result'][0]['flight_data']['No_of_available_seats'] = main_data[
                                    'numseatsavailable']
                            except:
                                result['result'][0]['flight_data']['No_of_available_seats'] = ''

                            api_response.append(result)

                            for i in api_response:
                                if i in ls:
                                    continue
                                else:
                                    ls.append(result)
                return ls


if __name__ == '__main__':
    data = get_json("AMD", "DXB", "no", "economy", "2022-09-03", "2022-09-03", 1, 1, 1, 12345)
    print(json.dumps(data))
