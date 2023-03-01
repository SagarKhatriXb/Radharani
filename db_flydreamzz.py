import datetime
import hashlib
import json

import pymysql
import requests



# db_name = 'flight_source_destination'
db_name = 'Radharani'
db_name2 = 'flight_source_destination'

table = f'flightsmaster'
# conn = pymysql.connect(host="localhost", user="root", password="xbyte", db=f"{db_name}")
conn = pymysql.connect(host="dev.xbytedev.co", user="root", password="Xbyte@123", db=f"{db_name}")
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute(f"delete from {table} where PlatForm = 'Flydreamzz' ")
conn.commit()

conn2 = pymysql.connect(host="localhost", user="root", password="xbyte", db=f"{db_name2}")
cur2 = conn2.cursor(pymysql.cursors.DictCursor)

url = "https://api.flydreamzz.in/getDashboard/"

payload = "{\"filters\":{},\"username\":\"agent.sneha14\"}"
headers = {
  'Accept':'application/json, text/plain, */*',
  'Accept-Language':'en-US,en;q=0.9,de;q=0.8',
  'Content-Type':'application/json',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

a = response.text
print()

json_Data = json.loads(response.text)
print()
for data in json_Data['data']:
  # data[0].bookingtype
  if data['bookingtype'] == 'online':
    item = dict()
    Source = data['destination'].split(" ")[0]
    Destination = data['destination'].split(" ")[2]
    PlatForm = 'Flydreamzz'
    Dates = data['traveldate']

    item['Source'] = Source
    item['Destination'] = Destination
    item['PlatForm'] = PlatForm
    item['Dates'] = Dates

    hash_utf8 = (
      f"{item['Source']}{item['Destination']}{item['Dates']}{item['PlatForm']}").encode(
      'utf8')
    Hash_id = int(hashlib.md5(hash_utf8).hexdigest(), 16) % (10 ** 16)
    item['hashid'] = Hash_id

    try:
      field_list = []
      value_list = []
      for field in item:
        field_list.append(str(field))
        value_list.append(str(item[field]).replace("'", "’"))
      fields = ','.join(field_list)
      values = "','".join(value_list)
      values = values.replace('\n', '').replace('\t', '').replace('\r', '')
      try:
        insert_db = "insert into " + table + "( " + fields + " ) values ( '" + values + "' )"
        cur.execute(insert_db)
        conn.commit()
      except Exception as E:
        print(E)

      print("Data Inserted Successfully.")

      try:
        cur2.execute(insert_db)
      except Exception as E:
        print(E)
        conn2.commit()
    except Exception as e:
      print(e)