import datetime
import hashlib

import pymysql

import xmltodict
import json
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import xmltodict
import json
import requests
import chromedriver_autoinstaller


def database_creation():
    global db_name
    db_name = 'FLight_Source_Destination'

    global table
    table = 'flightsmaster'

    db = pymysql.connect(host="localhost", user="root", password="xbyte")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(f'''CREATE DATABASE IF NOT EXISTS {db_name}''')
        print("Database Created Successfully")
    except Exception as Database_Creation:
        print(Database_Creation)
    conn = pymysql.connect(host="localhost", user="root", password="xbyte", database=db_name)
    curr = conn.cursor()
    try:
        curr.execute(f'''CREATE TABLE IF NOT EXISTS {table}(
                                    `Id` int(11) NOT NULL AUTO_INCREMENT,
                                     `Source` longtext,
                                     `Destination` longtext,
                                     `Platform` longtext,
                                     `Dates` longtext,
                                     `TotalFare` longtext,
                                      PRIMARY KEY (`Id`))DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_general_ci''')
        print("Table Created Successfully")

    except Exception as Table_Creation:
        print(Table_Creation)


def login_site():
    session = requests.Session()

    url = "https://www.makevoyage.com/dispatch.jsp?nonce=84.44047970198821"

    payload = "userid=9382207002&password=Sumit%4012356&opid=AU001&usertype=GenericClient&agencycode="
    headers = {
        'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '86',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.makevoyage.com',
        'Referer': 'https://www.makevoyage.com/indexpage.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    session.post(url=url, headers=headers, data=payload)
    jsessionid = session.cookies.get_dict()['JSESSIONID']

    return jsessionid
    # try:
    #     username = "9382207002"
    #     password = "Sumit@12356"
    #
    #     options = Options()
    #     options.add_argument('--headless')
    #
    #     driver = webdriver.Chrome(chromedriver_autoinstaller.install(), options=options)
    #     # driver = webdriver.Chrome('C:\Chromedriver_path\chromedriver.exe', options=options)
    #
    #     # head to github login page
    #     driver.get("https://www.makevoyage.com/indexpage.jsp")
    #     # find username/email field and send the username itself to the input field
    #     driver.find_element_by_id("username").send_keys(username)
    #
    #     # comment: find password input field and insert password as well
    #     driver.find_element_by_id("password").send_keys(password)
    #
    #     driver.find_element_by_id("loginbutton").click()
    #     jsessionid = driver.get_cookies()[0]['value']
    #     print(jsessionid)
    #
    #
    #     WebDriverWait(driver=driver, timeout=10).until(
    #         lambda x: x.execute_script("return document.readyState === 'complete'"))
    #     error_message = "Incorrect username or password."
    #
    #     errors = driver.find_elements_by_class_name("flash-error")
    #
    #     if any(error_message in e.text for e in errors):
    #         print("Login failed")
    #     else:
    #         print("Login successful")
    #
    #     driver.close()
    #     return jsessionid
    # except Exception as e:
    #     print("Error in login :", e)
    #     jsessionid = ''
    #     return jsessionid


def db_makevoyage():
    current_date = datetime.date.today().strftime('%Y-%m-%d')
    current_date = datetime.datetime.strptime(current_date, '%Y-%m-%d')

    db_name = 'Radharani'
    table = f'flightsmaster'
    conn = pymysql.connect(host="dev.xbytedev.co", user="root", password="Xbyte@123", db=f"{db_name}")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(f"Delete from {table} where PlatForm ='Makevoyage' ")
    conn.commit()

    url = "https://www.makevoyage.com/dispatch.jsp?nonce=0.30312992328242494"

    jsessionid = login_site()
    payload = "opid=MQ000&actioncode=GETDISTINCTCOUPONSECTORS"
    headers = {
        'accept': 'text/html, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'connection': 'keep-alive',
        # 'content-length': '46',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': f'JSESSIONID={jsessionid}',
        'host': 'www.makevoyage.com',
        'origin': 'https://www.makevoyage.com',
        # 'referer': 'https://www.makevoyage.com/series-fare-search.jsp?org=JAI&des=GOI',
        # 'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"Windows"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    a = response.text
    print()

    # print(response.text)

    my_xml = response.text
    dict_data = xmltodict.parse(my_xml)

    json_data = json.dumps(dict_data)
    json_data = json.loads(json_data)
    print()

    # db_name = database_creation()
    # table = database_creation()
    # db_name = "FLight_Source_Destination"
    # table = "FlightMaster"

    for flight_Data in json_data['Root']['Result']['DistinctCouponSectorS']['DistinctCouponSector']:
        # item = {}

        Origin = flight_Data['Origin']
        OriginFullname = flight_Data['OriginFullname']
        Destination = flight_Data['Destination']
        DestinationFullname = flight_Data['DestinationFullname']

        url1 = "https://www.makevoyage.com/dispatch.jsp?nonce=0.243262532656227"

        payload = f"opid=MQ000&actioncode=GETCOUPONFARECALENDAR&origin={Origin}&destination={Destination}"
        headers = {
            'accept': 'text/html, */*; q=0.01',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'connection': 'keep-alive',
            # 'content-length': '70',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': f'JSESSIONID={jsessionid}',
            'host': 'www.makevoyage.com',
            'origin': 'https://www.makevoyage.com',
            # 'referer': 'https://www.makevoyage.com/series-fare-search.jsp?org=MAA&des=GAU',
            # 'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-platform': '"Windows"',
            # 'sec-fetch-dest': 'empty',
            # 'sec-fetch-mode': 'cors',
            # 'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        response1 = requests.request("POST", url1, headers=headers, data=payload)

        # print(response1.text)

        my_xml1 = response1.text
        dict_data1 = xmltodict.parse(my_xml1)

        json_data1 = json.dumps(dict_data1)
        json_data1 = json.loads(json_data1)

        # print(json_data1)
        print()

        # print(type(json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']))

        if json_data1['Root']['Result']['CouponFareCalendarList'] == "None":
            # Root.Result.CouponFareCalendarList
            break

        if type(json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']) == dict:

            if json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']['AvailSeats'] != '0':

                item = {}
                Origin_ = json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']['Origin']
                Destination_ = json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar'][
                    'Destination']
                DepDate_ = str(json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']['DepDate'])

                DepDate_ = datetime.datetime.strptime(DepDate_, '%Y-%m-%d')


                # DepDate_ = DepDate_[:2] + ":" + DepDate_[2:]
                # print(DepDate_)
                TotalFare = json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar'][
                    'TotalFare']
                # AvailSeats = json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']['AvailSeats']

                item['Source'] = Origin_
                item['Destination'] = Destination_
                item['Dates'] = DepDate_

                item['PlatForm'] = "Makevoyage"
                # item['TotalFare'] = TotalFare

                hash_utf8 = (f"{item['Source']}{item['Destination']}{item['Dates']}{item['PlatForm']}").encode(
                    'utf8')
                Hash_id = int(hashlib.md5(hash_utf8).hexdigest(), 16) % (10 ** 16)
                item['hashid'] = Hash_id

                if DepDate_ >= current_date:
                    print(item)

                    try:
                        field_list = []
                        value_list = []
                        for field in item:
                            field_list.append(str(field))
                            value_list.append(str(item[field]).replace("'", "’"))
                        fields = ','.join(field_list)
                        values = "','".join(value_list)
                        values = values.replace('\n', '').replace('\t', '').replace('\r', '')
                        insert_db = "insert into " + table + "( " + fields + " ) values ( '" + values + "' )"
                        cur.execute(insert_db)
                        conn.commit()
                        print("Data Inserted Successfully.")
                    except Exception as e:
                        print(e)

        # break
        if type(json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']) == list:
            # Root.Result.CouponFareCalendarList.CouponFareCalendar[0].CouponId
            for info in json_data1['Root']['Result']['CouponFareCalendarList']['CouponFareCalendar']:

                if info['AvailSeats'] != '0':
                    item = {}
                    Origin_ = info['Origin']
                    Destination_ = info['Destination']
                    DepDate_ = info['DepDate']
                    DepDate_ = datetime.datetime.strptime(DepDate_, '%Y-%m-%d')

                    # TotalFare = info['TotalFare']
                    # AvailSeats = info['AvailSeats']

                    item['Source'] = Origin_
                    item['Destination'] = Destination_
                    item['Dates'] = DepDate_
                    item['PlatForm'] = "Makevoyage"

                    hash_utf8 = (
                        f"{item['Source']}{item['Destination']}{item['Dates']}{item['PlatForm']}").encode(
                        'utf8')
                    Hash_id = int(hashlib.md5(hash_utf8).hexdigest(), 16) % (10 ** 16)
                    item['hashid'] = Hash_id

                    # item['TotalFare'] = TotalFare
                    # item['TotalFare'] = TotalFare
                    # item['AvailSeats'] = AvailSeats
                    if DepDate_ >= current_date:
                        print(item)

                        try:
                            field_list = []
                            value_list = []
                            for field in item:
                                field_list.append(str(field))
                                value_list.append(str(item[field]).replace("'", "’"))
                            fields = ','.join(field_list)
                            values = "','".join(value_list)
                            values = values.replace('\n', '').replace('\t', '').replace('\r', '')
                            insert_db = "insert into " + table + "( " + fields + " ) values ( '" + values + "' )"
                            cur.execute(insert_db)
                            conn.commit()
                            print("Data Inserted Successfully.")
                        except Exception as e:
                            print(e)

        # Root.Result.DistinctCouponSectorS.DistinctCouponSector


if __name__ == '__main__':
    db_makevoyage()
    # database_creation()
