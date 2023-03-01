import xmltodict
import json
import requests
import datetime
proxy_host = "zproxy.luminati.io"
proxy_port = "22225"

proxy_auth = 'brd-customer-c_11e7173f-zone-shopee_foram_ecom:qws2756tfhbc'
proxies_uk = {
    "https": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/",
    "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/"
    }


airline = [{'I5S': 'Air Asia Series'}, {'UK1': 'Vistara Special'}, {'6EH': 'Indigo Handbaggage'}, {'H1': 'Hahn Airways'}, {'6EF': 'Indigo Family'}, {'PC': 'Pegasus Airlines'}, {'G84': 'GoAir Preferred '}, {'SGF': 'Spicejet Family'}, {'SG7': 'Spicejet Coupon'}, {'YB1': 'Borajet'}, {'TZ': 'Air Tanzania'}, {'PK': 'Pakistan Airlines'}, {'PK1': 'Pakistan Airlines'}, {'TK1': 'Turkish Airlines'}, {'RQS': 'Kamair Series'}, {'FZS': 'Flydubai Series'}, {'SGS': 'Spicejet Special'}, {'4QS': 'Safi Airways Series'}, {'AI1': 'Air India'}, {'G86': 'GoAir Business'}, {'6E6': 'Indigo Preferred'}, {'SG6': 'SpiceJet Handbaggage only Fare'}, {'SG5': 'SpiceJet Family'}, {'EA': 'European Air Express'}, {'SG9': 'SpiceJet Preferred'}, {'SG8': 'SpiceJet Retail'}, {'EB': 'Pullmantur Air'}, {'EC': 'Openskies'}, {'DT': 'TAAG Angola Airlines'}, {'E7': 'Fly European'}, {'DV': 'Air Company SCAT'}, {'DW': 'Aero-Charter'}, {'DX': 'Danish Air Transport'}, {'DY': 'Norwegian Air Shuttle'}, {'DM': 'Sterling Blue'}, {'DL': 'Delta Air Lines'}, {'DN': 'Air Deccan'}, {'DQ': 'Costal Air Transport'}, {'DP': 'First Choice Airways'}, {'E4': 'Aero Asia International'}, {'DR': 'Air Link Pty Ltd'}, {'DE': 'Condor Flugdienst'}, {'DD': 'NOK Airlines'}, {'DG': 'South East Asian Airlines'}, {'DF': 'Aebal'}, {'DH': 'Independence AIr'}, {'DJ': 'Virgin Blue'}, {'FD': 'Thai AirAsia'}, {'FE': 'Primaris Airlines'}, {'FB': 'Bulgaria Air'}, {'FC': 'Finnish Commuter Airlines'}, {'F8': 'Freedom Airlines'}, {'EW': 'Eurowings AG'}, {'F9': 'Frontier Airlines'}, {'EX': 'Air Santo Domingo'}, {'EU': 'Ecuatoriana'}, {'EV': 'Atlantic Southeast Airlines'}, {'Z2': 'Zest Airways'}, {'FZ': 'Fly Dubai'}, {'F7': 'Flybaboo'}, {'EY': 'Etihad Airways'}, {'EY1': 'Etihad Airways'}, {'EZ': 'Sun Air of Scandinavia'}, {'EP': 'Iran Assemam Airlines'}, {'EO': 'Hewa Bora Airways'}, {'EN': 'Air Dolomiti S P A'}, {'EM': 'Aero Benin'}, {'ET': 'Ethiopian Air Lines'}, {'ET1': 'Ethiopian Air Lines'}, {'ES': 'DHL International'}, {'F3': 'Fly Excellent'}, {'EH': 'Air Nippon Network'}, {'EF': 'Far Eastern Air Transport'}, {'EE': 'Aero Airlines'}, {'EK': 'Emirates Airlines'}, {'EK1': 'Emirates'}, {'4Q1': 'Safi Airways'}, {'EJ': 'New England Airlines'}, {'EI': 'Aer Lingus P.L.C.'}, {'GE': 'TransAsia Airways'}, {'GF': 'Gulf Airlines'}, {'GF1': 'Gulf Airlines'}, {'GF1': 'Gulf Air Company'}, {'GA': 'Garuda Indonesian'}, {'FZ1': 'Fly Dubai'}, {'FZ2': 'Fly Dubai'}, {'XY': 'Flynas'}, {'FV': 'Rossiya- Russian Airlines'}, {'FW': 'IBEX Airlines'}, {'G81': 'GoAir Preferred'}, {'G82': 'GoAir Flexi'}, {'G85': 'GoAir Special'}, {'G83': 'GoAir Business'}, {'G8': 'GoAir Smart'}, {'G9': 'Air Arabia'}, {'FY': 'Firefly'}, {'G4': 'Allegiant Air'}, {'FS': 'Itali Airlines'}, {'G3': 'Gol Transportes Aereos'}, {'FR': 'RyanAir (Ireland)'}, {'G6': 'Angkor Airways Corporation'}, {'FT': 'Siem Reap Airways International'}, {'G5': 'China Express Airlines'}, {'FN': 'Regional Air Lines  (Morocco)'}, {'FQ': 'Brindabella Airlines'}, {'FP': 'Freedom Air (Guam)'}, {'FK': 'Keewatin Air'}, {'FJ': 'Air Pacific Limited'}, {'FM': 'Shanghai Airlines'}, {'FL': 'Airtran Airways Inc'}, {'FG': 'Ariana Afghan Airlines'}, {'FI': 'Icelandair'}, {'FH': 'Futura International Airways'}, {'HG': 'Niki Luftfahrt'}, {'HD': 'Hokkaido International Airlines'}, {'HE': 'LGW'}, {'HB': 'Homer Air'}, {'HA': 'Hawaiian Airlines'}, {'GY': 'Gabon Airlines'}, {'GZ': 'Air Rarotonga'}, {'GW': 'Kuban Airline'}, {'GX': 'JetX'}, {'H9': 'Pegasus Airlines'}, {'GV': 'Grant Aviation'}, {'H7': 'Eagle Aviation Uganda'}, {'H6': 'Hageland Aviation Services'}, {'GU': 'Aviateca'}, {'GT': 'GB Airways'}, {'H4': 'Heli Securite'}, {'GS': 'Grand China Express'}, {'GR': 'Aurigny Air Services'}, {'H2': 'Sky Airline'}, {'GP': 'Gadair'}, {'GM': 'Air Slovakia'}, {'GL': 'Air Greenland'}, {'GI': 'Itek Air'}, {'A4': 'Southern Winds S.A.'}, {'A3': 'Aegean Air'}, {'A6': 'Air Alps'}, {'A5': 'Airlinair'}, {'A8': 'Benin Golf Air'}, {'A9': 'Georgian Airways'}, {'A0': 'L Avion Elysair'}, {'AT': 'Royal Air Maroc'}, {'AS': 'Alaska Airlines'}, {'AR': 'Aerolineas Argentinas'}, {'B2': 'Belavia'}, {'AX': 'American Connection'}, {'B8': 'Eritrean Airlines'}, {'AV': 'Avianca'}, {'B7': 'Uni Airways Corporate.'}, {'AU': 'Austral Lineas Aerea'}, {'B6': 'JetBlue Airways'}, {'AZ': 'Alitalia'}, {'AY': 'Finnair'}, {'BA': 'British Airways'}, {'AC': 'Air Canada'}, {'AA': 'American Airlines'}, {'AB': 'Air Berlin'}, {'AH': 'Air Algerie'}, {'AF': 'Air France'}, {'AF1': 'Air France'}, {'AK': 'AirAsia'}, {'AL': 'Skyway Airlines'}, {'AI': 'Air India'}, {'AJ': 'Aerocontractors'}, {'AP': 'Air One'}, {'AM': 'Aeromexico'}, {'BW': 'Caribbean Airlines'}, {'C8': 'NAC Air LP'}, {'BV': 'Blue Panorama Airlines'}, {'BY': 'Thomsonfly'}, {'C9': 'Cirrus Airlines'}, {'BS': 'British International'}, {'BR': 'EVA Airways Corporation'}, {'C3': 'Contact Air'}, {'C6': 'Canjet Airlines'}, {'BU': 'SAS Norway'}, {'BT': 'Air Baltic'}, {'C5': 'CommutAir'}, {'CB': 'ScotAirways'}, {'CA': 'Air China'}, {'BZ': 'KEYSTONE AIR SERVICE LTD'}, {'BF': 'Vincent Aviation'}, {'BG': 'Biman Bangladesh'}, {'BH': 'BH Airlines (Air Bosna)'}, {'BI': 'Royal Brunei Air'}, {'BB': 'Seaborne Airlines'}, {'BD': 'Bmi British Midland'}, {'BE': 'Flybe'}, {'C0': 'Centralwings'}, {'BP': 'Air Botswana'}, {'C2': 'CEIBA Intercontinental'}, {'BQ': 'Aeromar Airlines'}, {'BJ': 'Nouvelair Tunisie'}, {'BL': 'Jetstar Pacific'}, {'BL1': 'Jetstar Pacific'}, {'BM': 'Airbee'}, {'CZ': 'China Southern Airlines'}, {'CY': 'Cyprus Airways'}, {'CX': 'Cathay Pacific Airways'}, {'D8': 'Djibouti Airlines'}, {'D7': 'AirAsia X'}, {'CV': 'Air Chatham'}, {'D6': 'Interair South Africa'}, {'CU': 'Cubana Airlines'}, {'D5': 'Dauair'}, {'D4': 'Alidaunia'}, {'CS': 'Continental Micronesia'}, {'DC': 'Golden Air Commuter'}, {'DB': 'Brit Air'}, {'CI': 'China Airlines'}, {'CJ': 'BA City Flyer'}, {'CG': 'Airlines of Papua New Guinea'}, {'CH': 'Bemidji Airlines'}, {'CE': 'Nationwide Air'}, {'CF': 'City Airline'}, {'YIN': 'Yining Arpt'}, {'CD': 'Alliance Air (India)'}, {'D2': 'Severstal Aircompany'}, {'CQ': 'Sunshine Express Airline'}, {'D3': 'Daallo Airlines'}, {'CO': 'Continental Airlines'}, {'CP': 'Compass Airlines'}, {'CM': 'Copa Airlines'}, {'CN': 'Grand China Air'}, {'CL': 'Lufthansa CityLine'}, {'LW': 'Pacific Wings'}, {'LV': 'Albanian Airlines'}, {'M7': 'Marsland Aviation'}, {'LU': 'Lan Express'}, {'M5': 'Kenmore Air'}, {'LZ': 'Belle Air'}, {'LY': 'El Al Israel Airlines'}, {'LX': 'SWISS'}, {'M9': 'Motor Sich JSC'}, {'LO': 'LOT Polish Airlines'}, {'M0': 'Aero Mongolia'}, {'LN': 'Libyan Airlines'}, {'M4': 'AVIOMPEX'}, {'LS': 'Jet2.com'}, {'LR': 'LACSA'}, {'M3': 'North Flying'}, {'M2': 'Mahfooz Aviation (Gambia) Ltd.'}, {'LQ': 'Air Guinea Cargo'}, {'LP': 'Lan Peru S.A.'}, {'MH': 'Malaysia Airline'}, {'ME': 'Middle East Airlines'}, {'ME1': 'Middle East Airlines'}, {'MF': 'Xiamen Airlines'}, {'MK': 'Air Mauritius'}, {'ML': 'African Transport'}, {'MI': 'SilkAir'}, {'MJ': 'Mihin Lanka'}, {'MD': 'Air Madagascar'}, {'MA': 'Malev Hungarian Airlines'}, {'MV': 'Armenian International Airways'}, {'N7': 'Lagun Air'}, {'MU': 'China Eastern Airlines'}, {'N6': 'Nuevo Continente S.A.'}, {'N9': 'Niger Air Continental'}, {'MW': 'Mokulele Airlines'}, {'MN': 'Kulula air'}, {'MM': 'Sociedad Aeronautica Medellin'}, {'MP': 'Martinair Holland'}, {'MO': 'Calm Air International'}, {'N3': 'Omskavia Airlines'}, {'N2': 'Dagestan Airlines'}, {'MQ': 'American Eagle Airlines'}, {'MT': 'Thomas Cook Airlines'}, {'MS': 'Egyptair'}, {'MS1': 'Egyptair'}, {'N4': 'Trans Air Benin'}, {'NF': 'Air Vanuatu Limited'}, {'NG': 'Lauda Air Luftfahrt'}, {'NH': 'All Nippon Airways'}, {'NK': 'Spirit Airlines'}, {'NL': 'Shaheen Air International'}, {'NM': 'Manx2'}, {'NB': 'Sterling'}, {'NZ': 'Air New Zealand'}, {'NY': 'Air Iceland'}, {'NX': 'Air Macau Company Limited'}, {'NW': 'Northwest Airlines Inc'}, {'O8': 'Oasis Hong Kong Airlines'}, {'NV': 'Air Central'}, {'O7': 'OzJet Airlines'}, {'NU': 'Japan Trans Ocean Air'}, {'NT': 'Binter Canarias'}, {'NS': 'Northeastern Airlines'}, {'O4': 'Antrak Air Ltd'}, {'NR': 'Pamir Air'}, {'NQ': 'Air Japan'}, {'O2': 'Jet Air'}, {'NO': 'Neos'}, {'NN': 'VIM Airlines'}, {'OM': 'MIAT - Mongolian Airlines'}, {'ON': 'Our Airline'}, {'OK': 'Czech Airlines'}, {'OL': 'OLT Ostfriesische Luftransport'}, {'OJ': 'Overland Airways'}, {'OH': 'Comair Inc.'}, {'OF': 'Air Finland'}, {'OC': 'Omni'}, {'OA': 'Olympic Air'}, {'OX': 'Orient Thai Airlines'}, {'P9': 'Perm Airlines'}, {'OW': 'Executive Airlines'}, {'P8': 'P.L.A.S. S/A'}, {'OZ': 'Asiana Airlines'}, {'OY': 'Andes Lineas Aeras'}, {'OT': 'Aeropelican'}, {'P5': 'AeroRepublica'}, {'OS': 'Austrian Airlines'}, {'P4': 'Aero Lineas Sosa'}, {'OV': 'Salam Air'}, {'P6': 'Pascan Aviation'}, {'OU': 'Croatia Airlines'}, {'OO': 'Skywest Airlines (Utah)'}, {'P0': 'ProflightCommuter Services'}, {'OR': 'Tui Airlines Nederland'}, {'P2': 'AirKenya Express'}, {'OQ': 'Chongqing Airlines'}, {'PL': 'Southern Air Charter'}, {'PN': 'China West Air'}, {'Q0': 'Quebecair Express'}, {'PO': 'Polar Air Cargo'}, {'PH': 'Polynesian Airlines'}, {'PJ': 'Air Saint-Pierre'}, {'PD': 'Porter Airlines'}, {'PF': 'Primera Air Scandinavia'}, {'PG': 'Bangkok Airways'}, {'PB': 'Provincial Airlines'}, {'HK': 'Yangon Airways'}, {'HH': 'Islandsflug HF'}, {'HI': 'Papillon Airways Inc'}, {'HN': 'Heavylift Cargo Airlines'}, {'HO': 'Juneyao Airlines'}, {'HM': 'Air Seychelles'}, {'HR': 'Hahn Air Businessline'}, {'I3': 'Ivoirienne de Transport'}, {'HS': 'Svenska Direktflyg'}, {'HQ': 'Harmony Airways'}, {'HV': 'Transavia Airlines'}, {'I7': 'Paramount Airways'}, {'I8': 'Aboriginal Air Services'}, {'HW': 'North-Wright Air Ltd'}, {'I5': 'Air Asia India'}, {'I51': 'Air Asia'}, {'HU': 'Hainan Airlines'}, {'HZ': 'Sakhalinskie Aviatrassy'}, {'HY': 'Uzbekistan Airways'}, {'I9': 'Air Italy'}, {'HX': 'Hong Kong Airlines'}, {'IC': 'Indian Airlines'}, {'IB': 'Iberia'}, {'IA': 'Iraqi Airways'}, {'IH': 'Falcon Air'}, {'IG': 'Air Italy'}, {'IF': 'Islas Airways'}, {'IE': 'Solomon Airlines'}, {'IJ': 'GREAT WALL AIRLINES CO LTD'}, {'IO': 'Intercontinental Pacific Airways'}, {'J0': 'Jetlink Express'}, {'IP': 'Atyrau Airways'}, {'J2': 'Azerbaijan Airlines'}, {'IQ': 'Augsburg Airways'}, {'J3': 'Northwestern Air'}, {'IR': 'Iran Air'}, {'IS': 'Island Airlines of Nantucket'}, {'J5': 'Alaska Seaplane'}, {'IT': 'Kingfisher Airlines'}, {'J6': "Larry's Flying Service"}, {'J7': 'Centre-Avia Airlines'}, {'IV': 'Wind Jet'}, {'J8': 'Berjaya Air'}, {'IW': 'Wings Air'}, {'J9': 'Jazeera Airways'}, {'IX': 'Air India Express'}, {'IZ': 'Arkia Israeli Airlines'}, {'IY': 'Yemenia Yemen Airways'}, {'JA': 'B &amp; H Airlines'}, {'JC': 'JAL Express'}, {'JE': 'Mango'}, {'JD': 'Deer Air Co'}, {'JF': 'L A B Flying Service'}, {'JI': 'San Juan Aviation'}, {'JH': 'Nordeste-Linhas Aereas Regionals'}, {'JP': 'Adria Airways'}, {'K2': 'Eurolot S. A.'}, {'JQ': 'Jetstar Airways'}, {'JN': 'Excel Airways'}, {'JO': 'JALways'}, {'JL': 'Japan Airlines International'}, {'JM': 'Air Jamaica'}, {'JJ': 'TAM Linhas Aereas'}, {'JK': 'Spanair'}, {'K9': 'Esen Air'}, {'JY': 'Air Turks &amp; Caicos'}, {'JV': 'Bearskin Airlines'}, {'K5': 'Wings of Alaska'}, {'JT': 'Lion Air'}, {'JU': 'JAT Airways'}, {'K3': 'Taquan Air Service'}, {'JR': 'Aero California'}, {'K4': 'Kronflyg'}, {'JS': 'Air Koryo'}, {'KB': 'Druk Air'}, {'KA': 'Hong Kong Dragon Airlines'}, {'JZ': 'Skyways AB'}, {'KG': 'Aerogaviota'}, {'KF': 'Blue1'}, {'KE': 'Korean Air'}, {'KC': 'Air Astana'}, {'KC1': 'Air Astana'}, {'KO': 'Alaska Central Express'}, {'KP': 'Kiwi International'}, {'KQ': 'Kenya Airways'}, {'KQ1': 'Kenya Airways'}, {'KR': 'Comores Aviation'}, {'KK': 'Atlas Jet International Airways'}, {'KL': 'KLM Royal Dutch Airlines'}, {'KL1': 'KLM Royal Dutch Airlines'}, {'KM': 'Air Malta Company'}, {'KW': 'Wataniya Airlines'}, {'KX': 'Cayman Airways'}, {'L9': 'Teamline Air Luftfahrt'}, {'L4': 'Air Liaison'}, {'KS': 'Peninsula Airways'}, {'L5': 'Helikopter Service'}, {'KT': 'Katmai Air'}, {'L6': 'Tbilaviamsheni'}, {'KU': 'Kuwait Airways'}, {'LA': 'Lan Airlines S.A.'}, {'LB': 'Lloyd Aereo Boliviano'}, {'LI': 'Liat Ltd'}, {'LH': 'Lufthansa'}, {'LJ': 'Jin Air'}, {'LE': 'Lugansk Airlines'}, {'LG': 'Luxair'}, {'LF': 'FlyNordic'}, {'VT': 'Air Tahiti'}, {'W5': 'Mahan Air'}, {'W6': 'Wizz Air Hungary'}, {'VU': 'Air Ivoire'}, {'W3': 'Arik Air'}, {'VR': 'Transportes Aereos de Cabo Verde'}, {'VS': 'Virgin Atlantic Airways Ltd.'}, {'VS1': 'Virgin Atlantic Airways Ltd.'}, {'VQ': 'Vintage Props &amp; Jets Inc'}, {'VN': 'Vietnam Airlines'}, {'VO': 'Tyrolean Airways'}, {'VJ': 'Jatayu Airlines'}, {'VK': 'Virgin Nigeria Airways'}, {'VH': 'Aeropostal Alas De Venezuela'}, {'VI': 'Vieques Air Link'}, {'VF': 'Valuair LTD'}, {'VG': 'VLM Trading As Cityjet'}, {'VE': 'Volare Spa'}, {'VC': 'Ocean Airlines SPA'}, {'VA': 'V-Australia'}, {'UZ': 'Buraq Air'}, {'V9': 'Bashkir Airlines'}, {'UX': 'Air Europa'}, {'UW': 'Universal Airlines Inc'}, {'V8': 'Iliamna Air Taxi'}, {'V6': 'VIP S.A'}, {'UU': 'Air Austral'}, {'V3': 'Carpatair'}, {'US': 'US Airways'}, {'UT': 'UTAir Aviation JSC'}, {'V5': 'DANUBE WINGS'}, {'UM': 'Air Zimbabwe'}, {'UN': 'Transaero Airlines'}, {'UO': 'Hong Kong Express Airways'}, {'UP': 'Bahamasair'}, {'UI': 'Eurocypria Airlines'}, {'UJ': 'Montair Aviation'}, {'UL': 'SriLankan Airlines'}, {'UE': 'Nasair'}, {'UF': 'Ukrainian Mediterranean'}, {'UG': 'Sevenair'}, {'UA': 'United Airlines Inc'}, {'UD': 'Hex Air'}, {'UC': 'Lan Chile Cargo'}, {'TY': 'Air Caledonie'}, {'TX': 'Air Caraibes'}, {'U9': 'Tatarstan Airlines'}, {'TU': 'Tunis Air'}, {'U6': 'Ural Airlines'}, {'TT': 'Tiger Airways'}, {'U5': 'USA 3000 Airlines'}, {'U8': 'Armavia Airline'}, {'U7': 'Air Uganda'}, {'Y3': 'Driessen Services'}, {'XR': 'Skywest Airlines (Australia)'}, {'Y4': 'Volaris'}, {'XP': 'Casino Express Airlines'}, {'XQ': 'SunExpress'}, {'XV': 'MR Lines'}, {'XW': 'Sky Express'}, {'Y8': 'Yakutia'}, {'Y5': 'Pace Airlines'}, {'XT': 'Skystar Airways'}, {'XU': 'African Express Airways'}, {'XJ': 'Mesaba Aviation'}, {'XK': 'CCM Airlines'}, {'XN': 'Air Nepal International'}, {'Y0': 'Yellow Air Taxi'}, {'XO': 'LTE International Airways'}, {'XL': 'Lan Ecuador Aerolane SA'}, {'XM': 'Alitalia Express'}, {'XG': 'Clickair'}, {'XF': 'Vladivostok Air'}, {'XE': 'Express Jet Airlines'}, {'WY': 'Oman Aviation'}, {'WY1': 'Oman Aviation'}, {'WX': 'City Jet'}, {'WW': 'Bmibaby'}, {'X8': 'Icaro'}, {'WO': 'World Airways'}, {'WP': 'Island Air'}, {'WR': 'Aviaprad'}, {'X3': 'Tuifly'}, {'WS': 'WestJet'}, {'X4': 'Vanair Limited'}, {'WT': 'Wasaya Airways'}, {'X5': 'Afrique Airlines'}, {'WU': 'Wizz Air Ukraine'}, {'X7': 'Air Service'}, {'WG': 'Sunwing Airlines'}, {'WI': 'Tradewinds Airlines'}, {'WJ': 'Labrador Airways Limited'}, {'WK': 'Edelweiss Air'}, {'WM': 'Windward Island Airways'}, {'WN': 'Southwest Airlines'}, {'WB': 'Rwandair Express'}, {'WA': 'KLM Cityhopper B V'}, {'WC': 'Islena Airlines'}, {'WF': 'Wideroes Flyveselskap'}, {'VW': 'Aeromar Airlines'}, {'VV': 'Aerosvit Airlines'}, {'VY': 'Vueling Airlines'}, {'VX': 'Virgin America'}, {'VZ': 'My TravelLite'}, {'RI': 'PT. Mandella Airlines'}, {'RH': 'Robin Hood Aviation'}, {'RF': 'Florida West International Airways'}, {'RE': 'Aer Arann Express'}, {'RB': 'Syrian Arab Airlines'}, {'S2': 'Jet Lite'}, {'RQ': 'Kam Air'}, {'RP': 'Chautauqua Airlines'}, {'S0': 'Slok Air International'}, {'RO': 'Tarom-Romanian Air Transport'}, {'RM': 'Regional Air'}, {'RJ': 'Royal Jordanian'}, {'RJ1': 'Royal Jordanian'}, {'QW': 'Blue Wings'}, {'QX': 'Horizon Air - Seattle'}, {'R9': 'Camai Air'}, {'R6': 'DOT LT'}, {'QV': 'Lao Aviation'}, {'R7': 'Aserca Airlines'}, {'QS': 'Smartwings'}, {'R4': 'Tulpar Avia Service'}, {'QT': 'Regional Pacific Airlines'}, {'R5': 'Malta Air Charter Company Limited'}, {'QQ': 'Alliance Airlines'}, {'R2': 'Orenair'}, {'QR': 'Qatar Airways'}, {'QR1': 'Qatar Airways'}, {'RA': 'Royal Nepal Airlines'}, {'QY': 'EUROPEAN AIR'}, {'QZ': 'Indonesia AirAsia'}, {'QF': 'Qantas Airways'}, {'QF1': 'Qantas Airways'}, {'QE': 'Crossair Europe'}, {'QH': 'Kyrgystan'}, {'QG': 'Qualiflyer Group'}, {'QA': 'Aero Caribe'}, {'QC': 'Air Corridor'}, {'QM': 'Air Malawi'}, {'QO': 'Origin Pacific Airways'}, {'QJ': 'Latpass Airlines'}, {'QI': 'Cimber Sterling'}, {'QL': 'Laser Airlines'}, {'QK': 'Air Canada Jazz'}, {'Q5': 'Forty Mile Air'}, {'PU': 'Pluna'}, {'PV': 'Saint Barth Commuter'}, {'PW': 'Precisionair'}, {'Q8': 'Trans Air Congo'}, {'PA': 'AirBlue Airways'}, {'PP': 'Jet Aviation Business Jets'}, {'PQ': 'Panafrican Airways'}, {'PR': 'Philippine Airlines'}, {'PS': 'Ukraine International Airline'}, {'Q4': 'Swazi Express Airways'}, {'PX': 'Air Niugini'}, {'PY': 'Surinam Airways'}, {'PZ': 'Transportes Aereso del Mercosur'}, {'TG': 'Thai Airways Intl'}, {'TF': 'Malmo Aviation'}, {'TD': 'Atlantis European Airways'}, {'TK': 'Turkish Airlines'}, {'TH': 'British Airways Citiexpress'}, {'TN': 'Air Tahiti Nui'}, {'TM': 'LAM Lineas Aereas de Mocambique'}, {'TL': 'Air North Regional'}, {'TS': 'Air Transat A.T. Inc.'}, {'U4': 'PMT Air'}, {'TR': 'Tiger Airways'}, {'U3': 'Avies LTD'}, {'TQ': 'Tandem Aero'}, {'U2': 'Easy jet'}, {'TP': 'TAP Air Portugal'}, {'SU': 'Aeroflot Russian Airlines'}, {'SU1': 'Aeroflot Russian Airlines'}, {'SV': 'Saudi Arabian Airlines'}, {'T7': 'Twin Jet'}, {'SS': 'Corsair International'}, {'T5': 'Turkmenistan Airlines'}, {'SY': 'Sun Country Airlines'}, {'SZ': 'Air Southwest'}, {'T8': 'STA Trans African Airlines'}, {'SW': 'Air Namibia'}, {'T9': 'Trans Meridian Airlines'}, {'TB': 'Tui Airlines Belgium'}, {'TC': 'Air Tanzania'}, {'TA': 'Taca International Airlines'}, {'SD': 'Sudan Airways'}, {'SC': 'Shandong Airlines'}, {'SF': 'Tassili Airlines'}, {'SE': 'XL Airways France'}, {'SG1': 'SpiceJet Special'}, {'SG2': 'Spice Jet Preferred'}, {'SG3': ' Spice Jet Preferred'}, {'SG': 'SpiceJet Web'}, {'SGH': 'Hand Baggage Only Fare  No Free checkin Baggage is Allowed'}, {'SJ': 'Sriwijaya Air'}, {'SI': 'Skynet Airlines'}, {'SL': 'Rio Sul'}, {'SK': 'SAS Scandinavian Airlines'}, {'SN': 'Brussels Airlines'}, {'SM': 'Swedline'}, {'SP': 'SATA Air Acores'}, {'T3': 'Eastern Airways Ltd'}, {'SQ': 'Singapore Airlines'}, {'T2': 'Nakina Air Service'}, {'RR': 'Royal Air Force-38 Transport Group'}, {'S3': 'Santa Barbara Airlines C.A.'}, {'S4': 'SATA International'}, {'RT': 'RAK Airways'}, {'S5': 'Shuttle America'}, {'S6': 'Salmon Air'}, {'S7': 'Siberian Airlines'}, {'RV': 'Caspian Airlines'}, {'RW': 'RAS Fluggesellschaft'}, {'RY': 'Royal Wings'}, {'SA': 'South African Airways'}, {'SB': 'Air Calin'}, {'/KL': 'One Ticket to the World'}, {'ZA': 'Astair'}, {'ZG': 'Viva Macau'}, {'ZH': 'Shenzhen Airlines'}, {'ZI': 'Aigle Azur'}, {'ZN': 'Naysa'}, {'ZP': 'Air St Thomas'}, {'ZK': 'Great Lakes Airlines'}, {'ZJ': 'Zambezi Airlines'}, {'ZL': 'Regional Express'}, {'ZW': 'Air Wisconsin'}, {'ZV': 'Air Midwest'}, {'ZY': 'Ada Air'}, {'ZX': 'Zoom Airlines UK'}, {'ZR': 'Alexandria Airlines'}, {'ZU': 'Helios Airways'}, {'XZ': 'South African Express'}, {'Y9': 'Kish Airlines'}, {'YH': 'West Caribbean Airways'}, {'YE': 'Eram Airlines'}, {'YC': 'Yamal Airlines'}, {'YD': 'Mauritania Airways'}, {'YB': 'South African Express'}, {'YO': 'Heli-Air Monaco'}, {'YN': 'Air Creebec'}, {'YM': 'Montenergo Airlines'}, {'YL': 'Air Bissau International'}, {'YJ': 'AMC Airlines'}, {'YI': 'Air Sunshine'}, {'YW': 'Air Nostrum'}, {'YV': 'Mesa Airlines Inc'}, {'Z6': 'Dnieproavia State Aviation'}, {'YT': 'Air Togo'}, {'Z5': 'GMG Airlines'}, {'YS': 'Regional CAE'}, {'Z4': 'Zoom Airlines'}, {'YR': 'Scenic Airlines'}, {'Z3': 'PM Air LLC'}, {'YQ': 'Aircompany Polet'}, {'3A': 'Alliance Airlines (Chicago)'}, {'3B': 'Job Air Central Connect'}, {'2U': "Sun d'OR Int'l Airlines"}, {'2X': 'XEROX'}, {'2Y': 'Air Andaman'}, {'2W': 'Welcome Air'}, {'3M': 'Gulfstream Intl'}, {'3L': 'Intersky'}, {'3K': 'Jetstar Asia Airways'}, {'3R': 'Gromov Air'}, {'3Q': 'Carib Aviation'}, {'3O': 'Peau Vava U'}, {'3F': 'Pacific Airways'}, {'3E': 'Air Choice One'}, {'3D': 'Denim Air'}, {'3C': 'Corporate Express Airlines'}, {'3H': 'Air Inuit Ltd.'}, {'1T': '1Time Airlines'}, {'1X': 'Branson Air Express'}, {'2K': 'Aerogal Aerolinas Galapagos'}, {'2J': 'Air Burkina'}, {'2M': 'Moldavian Airlines'}, {'2L': 'Helvetic Airways'}, {'2O': 'Island Air Service'}, {'2Q': 'Avitrans Nordi'}, {'2B': 'Bahrain Air'}, {'2E': 'Smokey Bay Air'}, {'2G': 'Northwest Seaplanes'}, {'2F': 'Frontier Flying Service'}, {'2I': 'Star Up'}, {'0Y': 'FlyYeti'}, {'0D': 'Darwin Airlines'}, {'6Y': 'Latcharter Airlines Ltd'}, {'7B': 'Atlant-Soyuz Airlines'}, {'7A': 'Air Next'}, {'7F': 'First Air'}, {'7E': 'Panagra Airways Inc.'}, {'7D': 'Donbassaero Airlines'}, {'7I': 'Insel Air International'}, {'7J': 'Tajikair'}, {'7H': 'Era Aviation Inc'}, {'7N': 'Inland Aviation Services'}, {'7Q': 'Tibesti AirLibya'}, {'7R': 'Red Sea Air'}, {'7P': 'APA International Air SA'}, {'7V': 'Pelican Air'}, {'7S': 'Artic Transportation Services'}, {'7T': 'Trans North Aviation'}, {'5V': 'Lviv Airlines'}, {'5U': 'Challenge Aero'}, {'5W': 'Astraeus'}, {'5Z': 'Bismillah Airlines'}, {'6C': 'Cape Smythe Air'}, {'VA': 'Ventura AirConnect'}, {'LB': 'Air Costa'}, {'LB1': 'Air Costa EconomyPlus'}, {'6E5': 'Indigo Preferred'}, {'6E1': 'Indigo Star'}, {'6E2': 'Indigo Special'}, {'6E3': 'Indigo TBF'}, {'6E8': 'Indigo Preferred'}, {'6E9': 'Indigo Preferred'}, {'6E': 'Indigo Web'}, {'6E4': 'Indigo Family'}, {'6G': 'Gulfstream Connection'}, {'6H': 'Israir'}, {'6I': 'AeroSyncro Aviation'}, {'6J': 'Jubba Airways'}, {'6K': 'Asian Spirit'}, {'6L': 'Aklak Air Ltd'}, {'6N': 'Nordic Regional'}, {'6P': 'Clubair Sixgo'}, {'6Q': 'Slovak Airlines'}, {'6T': 'Air Mandalay Ltd.'}, {'4Y': 'Yute Air Alaska Inc.'}, {'4W': 'Warbelows Air Ventures'}, {'4V': 'Birdy Airlinesce'}, {'4U': 'Germanwings'}, {'4T': 'Belair'}, {'5D': 'Aeromexico Connect'}, {'5C': 'Nature Air'}, {'5B': 'Euro- Asia Air International'}, {'5K': 'Odessa Airlines'}, {'5L': 'Aerosur'}, {'5J': 'Cebu Pacific Air'}, {'5G': 'Skyservice Airlines'}, {'5H': 'Five Fourty Aviation'}, {'5E': 'Nok Mini'}, {'5F': 'Arctic Circle Air'}, {'5S': 'Servicios Aereos Profesionales'}, {'5T': 'Canadian North'}, {'5Q': 'Best Air'}, {'5O': 'Europe Airpost'}, {'5P': 'SkyEurope Airlines Hungary'}, {'5N': 'Nordavia Regional Airline'}, {'3X': 'JAPAN AIR COMMUTER CO'}, {'3Z': 'Everts Air'}, {'3Y': 'UNIWAYS'}, {'3S': 'Air Guyane'}, {'3U': 'Sichuan Airlines'}, {'4A': 'Royal Bengal Airlines'}, {'4C': 'Aires'}, {'4B': 'Perimeter Aviation'}, {'4H': 'United Airways Bangladesh'}, {'4I': 'IHY Izmir Havayollari'}, {'4J': 'Somon Air'}, {'4K': 'Kenn Borek Air Ltd'}, {'4D': 'Air Sinai'}, {'4F': 'Air City'}, {'4G': 'Gazpromavia'}, {'4P': 'Viking Airlines'}, {'4Q': 'Safi Airways'}, {'4R': 'Hamburg International'}, {'4L': 'Georgian International Airline LLC'}, {'4M': 'Lan Argentina'}, {'4N': 'Air North'}, {'4O': 'Interjet'}, {'9V': 'Avior Airlines'}, {'9U': 'Air Moldova'}, {'9X': 'New Axis Airways'}, {'9W': 'Jet Airways'}, {'9W1': 'Jet Airways Special'}, {'9W2': 'Jet Airways Corporate'}, {'9Q': 'PB Air Company'}, {'9T': 'Travelspan'}, {'9N': 'SATENA'}, {'9M': 'Central Mountain Air'}, {'9P': 'Palau National Airlines'}, {'9J': 'Pacific Island Aviation'}, {'9L': 'Colgan Air'}, {'9K': 'Cape Air'}, {'9E': 'Nortwest Airlink'}, {'9H': 'Dutch Antilles Express'}, {'9C': 'Wimbi Dira Airways'}, {'9D': 'Toumai Air Tchad'}, {'8Z': 'Wizz Air Bulgaria'}, {'8W': 'Private Wings'}, {'8V': 'Wright Air Service Inc.'}, {'8U': 'Afriqiyah Airways'}, {'8T': 'Air Tindi Ltd.'}, {'8P': 'Pacific Coastal Airlines'}, {'8N': 'Nordkalottflyg'}, {'8M': 'Myanmar Airways Intl'}, {'8J': 'Jet4You'}, {'8H': 'Highland Airways'}, {'8F': 'STP Airways'}, {'8D': 'Servant Air'}, {'8E': 'Bering Air Inc.'}, {'8A': 'Atlas Blue'}, {'7Y': 'Flying Carpet Air Transport'}, {'7Z': 'Halcyon Air'}, {'7W': 'Wind Rose Aviation'}, {'6ES': 'Indigo Special'}, {'G8S': 'Go Air Series'}, {'9WS': 'Jetairways Series'}, {'S2S': 'Jetlite Series'}, {'AIS': 'Air India Series'}, {'6E-S': 'Indigo Series'}, {'SG-S': 'Spicejet Series'}, {'G8-S': 'Go Air Series'}, {'9W-S': 'Jetairways Series'}, {'S2-S': 'Jetlite Series'}, {'AI-S': 'Air India Series'}, {'6E-SP': 'Indigo Corporate'}, {'SG-SP': 'Spicejet Corporate'}, {'G8-SP': 'Go Air Corporate'}, {'9W-SP': 'Jetairways Specil'}, {'S2-SP': 'Jetlite Corporate'}, {'AI-SP': 'Air India Corporate'}, {'6EL': 'Indigo Hand Baggage Fares'}, {'SGL': 'Last Minute Deal'}, {'G8L': 'Last Minute Deal'}, {'9WL': 'Last Minute Deal'}, {'S2L': 'Last Minute Deal'}, {'AIL': 'Last Minute Deal'}, {'OD': 'Malindo Air'}, {'UK': 'Vistara'}, {'OP': 'Air Pegasus'}, {'ZM': 'Air Manas'}, {'YK': 'Avia Traffic Company'}, {'GK': 'Jetstar Japan'}, {'K6': 'Cambodia Angkor Air'}, {'2T': 'TruJet'}, {'AO': 'Air Odisha'}, {'9W_corpgds': 'Jet Airways Corporate'}, {'AI_corpgds': 'Air India Corporate'}, {'UK_corpgds': 'Vistara Corporate'}, {'6E7': 'Indigo SME Fare'}, {'G91': 'Air Arabia Baggage'}, {'G92': 'Air Arabia Baggage'}, {'6ET': 'Indigo Special fare'}, {'WE': 'Thai Smile'}, {'UK2': 'Vistara TBF'}, {'G8S': 'GoAir Series'}, {'UKS': 'Vistara Series'}, {'S9S': 'Flybig Series'}]
flight_code_json = [{"places": "Agartala", "airport_code": "IXA"}, {"places": "Ahmedabad", "airport_code": "AMD"},
                    {"places": "Aizawl", "airport_code": "AJL"}, {"places": "Aurangabad", "airport_code": "IXU"},
                    {"places": "Amritsar", "airport_code": "ATQ"}, {"places": "Bagdogra", "airport_code": "IXB"},
                    {"places": "Bengaluru", "airport_code": "BLR"}, {"places": "Bhubaneswar", "airport_code": "BBI"},
                    {"places": "Bhopal", "airport_code": "BHO"}, {"places": "Chandigarh", "airport_code": "IXC"},
                    {"places": "Chennai", "airport_code": "MAA"}, {"places": "Coimbatore", "airport_code": "CJB"},
                    {"places": "Dehradun", "airport_code": "DED"}, {"places": "Delhi", "airport_code": "DEL"},
                    {"places": "Dibrugarh", "airport_code": "DIB"}, {"places": "Dimapur", "airport_code": "DMU"},
                    {"places": "Durgapur", "airport_code": "RDP"}, {"places": "Gaya", "airport_code": "GAY"},
                    {"places": "Goa", "airport_code": "GOI"}, {"places": "Gorakhpur", "airport_code": "GOP"},
                    {"places": "Guwahati", "airport_code": "GAU"}, {"places": "Hubli", "airport_code": "HBX"},
                    {"places": "Hyderabad", "airport_code": "HYD"}, {"places": "Imphal", "airport_code": "IMF"},
                    {"places": "Indore", "airport_code": "IDR"}, {"places": "Jabalpur", "airport_code": "JLR"},
                    {"places": "Jaipur", "airport_code": "JAI"}, {"places": "Jammu", "airport_code": "IXJ"},
                    {"places": "Jodhpur", "airport_code": "JDH"}, {"places": "Jorhat", "airport_code": "JRH"},
                    {"places": "Kannur", "airport_code": "CNN"}, {"places": "Kurnool", "airport_code": "KJB"},
                    {"places": "Kochi", "airport_code": "COK"}, {"places": "Kolhapur", "airport_code": "KLH"},
                    {"places": "Kolkata", "airport_code": "CCU"}, {"places": "Kozhikode", "airport_code": "CCJ"},
                    {"places": "Lucknow", "airport_code": "LKO"}, {"places": "Madurai", "airport_code": "IXM"},
                    {"places": "Mangaluru", "airport_code": "IXE"}, {"places": "Mumbai", "airport_code": "BOM"},
                    {"places": "Mysuru", "airport_code": "MYQ"}, {"places": "Nagpur", "airport_code": "NAG"},
                    {"places": "Patna", "airport_code": "PAT"}, {"places": "Prayagraj", "airport_code": "IXD"},
                    {"places": "Pune", "airport_code": "PNQ"}, {"places": "Portblair", "airport_code": "IXZ"},
                    {"places": "Raipur", "airport_code": "RPR"}, {"places": "Rajahmundry", "airport_code": "RJA"},
                    {"places": "Ranchi", "airport_code": "IXR"}, {"places": "Shillong", "airport_code": "SHL"},
                    {"places": "Shirdi", "airport_code": "SAG"}, {"places": "Silchar", "airport_code": "IXS"},
                    {"places": "Srinagar", "airport_code": "SXR"}, {"places": "Surat", "airport_code": "STV"},
                    {"places": "Thiruvananthapuram", "airport_code": "TRV"},
                    {"places": "Tiruchirappalli", "airport_code": "TRZ"}, {"places": "Tirupati", "airport_code": "TIR"},
                    {"places": "Tuticorin", "airport_code": "TCR"}, {"places": "Udaipur", "airport_code": "UDR"},
                    {"places": "Vadodara", "airport_code": "BDQ"}, {"places": "Varanasi", "airport_code": "VNS"},
                    {"places": "Vijayawada", "airport_code": "VGA"}, {"places": "Visakhapatnam", "airport_code": "VTZ"},
                    {"places": "Kannur", "airport_code": "CNN"}, {"places": "Agartala", "airport_code": "IXA"},
                    {"places": "Ahmedabad", "airport_code": "AMD"}, {"places": "Amritsar", "airport_code": "ATQ"},
                    {"places": "Bagdogra", "airport_code": "IXB"}, {"places": "Bengaluru", "airport_code": "BLR"},
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
                    {"places": "Vijayawada", "airport_code": "VGA"}, {"places": "Visakhapatnam", "airport_code": "VTZ"},
                    {"places": "Gaya", "airport_code": "GAY"}, {"places": "Jodhpur", "airport_code": "JDH"},
                    {"places": "Silchar", "airport_code": "IXS"}, {"places": "Belagavi", "airport_code": "IXG"}, {"places": "Puducherry", "airport_code": "PNY"},{"places": "Rupsi", "airport_code": "RUP"},{"places": "Pasighat", "airport_code": "IXT"},{"places": "Ahmedabad", "airport_code": "AMD"},{"places": "Teju", "airport_code": "TEI"},{"places": "Imphal", "airport_code": "IMF"}]


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
    session.proxies.update(proxies_uk)
    try:
        a = session.post(url=url, headers=headers, data=payload, verify=False)
    except Exception as e:
        print(e)
    jsessionid = session.cookies.get_dict()['JSESSIONID']

    return jsessionid

    # comment: With selenium ==> below code
    # try:
    #     username = "9382207002"
    #     password = "Sumit@12356"
    #
    #     options = Options()
    #     options.add_argument('--headless')
    #
    #     driver = webdriver.Chrome(chromedriver_autoinstaller.install(), options=options)
    #     # driver = webdriver.Chrome("D:\X-Byte(Projects)\chromedriver.exe", options=options)
    #     # driver = webdriver.Chrome('C:\Chromedriver_path\chromedriver.exe', options=options)
    #
    #     # head to github login page
    #     driver.get("https://www.makevoyage.com/indexpage.jsp")
    #     # find username/email field and send the username itself to the input field
    #     driver.find_element_by_id("username").send_keys(username)
    #     # find password input field and insert password as well
    #     driver.find_element_by_id("password").send_keys(password)
    #     # click login button
    #     driver.find_element_by_id("loginbutton").click()
    #     jsessionid = driver.get_cookies()[0]['value']
    #     print(jsessionid)
    #
    #     # wait the ready state to be complete
    #     WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    #     error_message = "Incorrect username or password."
    #     # get the errors (if there are)
    #     errors = driver.find_elements_by_class_name("flash-error")
    #     # print the errors optionally
    #     # for e in errors:
    #     #     print(e.text)
    #     # if we find that error message within errors, then login is failed
    #     if any(error_message in e.text for e in errors):
    #         print("Login failed")
    #     else:
    #         print("Login successful")
    #
    #     driver.close()
    #     return jsessionid
    # except Exception as e:
    #     print("Error in login :",e)
    #     jsessionid = ''
    #     return jsessionid


def makevoyage_json(param_json, hashId):
    ls1 = {"results": dict()}

    list_ori_des = []
    for data in flight_code_json:
        list_ori_des.append(data['airport_code'])
    # print(list_ori_des)

    jsessionid = login_site()
    Origin = str(param_json['origin'])
    # print(Origin)

    Destination = str(param_json['destination'])
    # print(Destination)

    if Origin not in list_ori_des:
        # ls1['results'] = 'Invalid origin or destination entered.'
        ls1['results'] = {"status": 400, "msg": "Invalid origin or destination entered."}
        return ls1

    elif Destination not in list_ori_des:
        ls1['results'] = {"status": 400, "msg": "Invalid origin or destination entered."}
        return ls1

    else:

        # for i in flight_code_json:
        #
        #       if  i['places'] == Origin.capitalize():
        #           Origin = i['airport_code']
        #
        # for j in flight_code_json:
        #
        #       if j['places'] == Destination.capitalize():
        #           Destination = j['airport_code']

        DepartDate = param_json['depart_date']
        print(DepartDate)
        deptDate_for_payload = DepartDate.replace("-","")
        print(deptDate_for_payload)
        Adult = param_json['adult']
        Child = param_json['child']
        Infant = param_json['infant']

        url = "https://www.makevoyage.com/dispatch.jsp?nonce=0.5898738475848477"

        payload = f"opid=FS000&actioncode=SEARCHCOUPONFARES&agentid=MV24858&origin={Origin}&destination={Destination}&jdate={deptDate_for_payload}&numadults={Adult}&numchildren={Child}&numinfants={Infant}".replace(
            "-", "")

        headers = {
            'accept': 'text/html, */*; q=0.01',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'connection': 'keep-alive',
            'content-length': '136',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': b,
            'cookie': f'JSESSIONID={jsessionid}',
            'host': 'www.makevoyage.com',
            'origin': 'https://www.makevoyage.com',
            # 'referer': f'https://www.makevoyage.com/series-fare-search.jsp?org={Origin}&des={Destination}',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        # response = session.post(url, headers=headers, data=payload)
        try:
            response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies_uk, verify=False)
        except Exception as e:
            print(e)
        a = response.text
        print()

        my_xml = response.text
        dict_data = xmltodict.parse(my_xml)

        json_data = json.dumps(dict_data)
        json_data = json.loads(json_data)
        json_data = json_data['Root']['Result']
        print()

        if json_data == 'RRRRRR':
            ls1['results'] = {"status": 200, "HasResults": False, "data": list()}
            return ls1

        if json_data is None:
            ls1['results'] = {"status": 200, "HasResults": False, "data": "Internal Server Error"}
            return ls1

        # ls = {"results": list()}
        res_json = dict()
        main_result_list = list()

        if ':::' in json_data:
            b = json_data.split(':::')

            for info in b:
                result = {"Departure_Sector": None, "Arrival_Sector": None,
                          "Airlines": None, "Flight_number": None,
                          "No_of_stops": None, "Departure_Date_&_time": None,
                          "Arrival_Date_&_time": None, "No_of_available_seats": None,
                          "Price_per_seat": {}, "Domain": {}}
                c = str(info).split(",")

                result["Departure_Sector"] = str(c[3])
                result["Arrival_Sector"] = str(c[4])

                result["Flight_number"] = str(c[0] + "-" + c[1])

                for im in airline:
                    for k, v in im.items():
                        if k == str(c[0]):
                            result["Airlines"] = v
                # result["Airlines"] = ''
                result["No_of_stops"] = "Non Stop"
                Departure_Time = str(c[5])
                Departure_Time = Departure_Time[:2] + ":" + Departure_Time[2:]
                Departure_Time = datetime.datetime.strptime(Departure_Time, "%H:%M").strftime("%I:%M %p")

                Departure_Date = str(c[7])
                Departure_Date = Departure_Date[:4] + "-" + Departure_Date[4:6] + "-" + Departure_Date[6:]
                result["Departure_Date_&_time"] = Departure_Date + " " + Departure_Time

                Arrival_Time = str(c[6])
                Arrival_Time = Arrival_Time[:2] + ":" + Arrival_Time[2:]
                Arrival_Time = datetime.datetime.strptime(Arrival_Time, "%H:%M").strftime("%I:%M %p")

                Arrival_Date = str(c[8])
                Arrival_Date = Arrival_Date[:4] + "-" + Arrival_Date[4:6] + "-" + Arrival_Date[6:]

                result["Arrival_Date_&_time"] = Arrival_Date + " " + Arrival_Time
                result["No_of_available_seats"] = str(c[21])
                result["Price_per_seat"]["adult"] = str(int(str((int(str(c[28]).split(".")[0])) + (int(str(c[31]).split(".")[0])))))
                result["Price_per_seat"]["child"] = str(int(str((int(str(c[29]).split(".")[0])) + (int(str(c[32]).split(".")[0])))))
                result["Price_per_seat"]["infant"] = str(int(str(c[33]).split(".")[0]))
                result["Domain"] = 'makevoyage'
                main_result_list.append(result)
                # ls["results"].append(result)
                res_json['results'] = {"status": 200, "HasResults": True, "data": main_result_list}

            return res_json

        else:
            result = {"Departure_Sector": None, "Arrival_Sector": None,
                      "Airlines": None, "Flight_number": None,
                      "No_of_stops": None, "Departure_Date_&_time": None,
                      "Arrival_Date_&_time": None, "No_of_available_seats": None,
                      "Price_per_seat": {}, "Domain": {}}

            c = json_data.split(",")
            result["Departure_Sector"] = str(c[3])
            for i in flight_code_json:

                if i['airport_code'] == result["Departure_Sector"]:
                    result["Departure_Sector"] = i['places']
            result["Arrival_Sector"] = str(c[4])

            for j in flight_code_json:

                if j['airport_code'] == result['Arrival_Sector']:
                    result['Arrival_Sector'] = j['places']

            result["Flight_number"] = str(c[0] + "-" + c[1])

            for im in airline:
                for k,v in im.items():
                    if k == str(c[0]):
                        result["Airlines"] = v




            result["No_of_stops"] = "Non Stop"

            Departure_Date = str(c[7])
            Departure_Date = Departure_Date[:4] + "-" + Departure_Date[4:6] + "-" + Departure_Date[6:]

            Departure_Time = str(c[5])

            Departure_Time = Departure_Time[:2] + ":" + Departure_Time[2:]
            Departure_Time = datetime.datetime.strptime(Departure_Time, "%H:%M").strftime("%I:%M %p")

            result["Departure_Date_&_time"] = Departure_Date + " " + Departure_Time

            Arrival_Date = str(c[8])
            Arrival_Date = Arrival_Date[:4] + "-" + Arrival_Date[4:6] + "-" + Arrival_Date[6:]

            Arrival_Time = str(c[6])
            Arrival_Time = Arrival_Time[:2] + ":" + Arrival_Time[2:]
            Arrival_Time = datetime.datetime.strptime(Arrival_Time, "%H:%M").strftime("%I:%M %p")

            print()

            result['Arrival_Date_&_time'] = Arrival_Date + " " + Arrival_Time
            result["No_of_available_seats"] = str(c[21])
            # print(int(c[28]))
            result["Price_per_seat"]["adult"] = str(int(str((int(str(c[28]).split(".")[0])) + (int(str(c[31]).split(".")[0])))))
            if result["Price_per_seat"]["adult"] == '0.0':
                result["Price_per_seat"]["adult"] = None

            result["Price_per_seat"]["child"] = str(int(str((int(str(c[29]).split(".")[0])) + (int(str(c[32]).split(".")[0])))))
            if result["Price_per_seat"]["child"] == "0.0":
                result["Price_per_seat"]["child"] = None

            result["Price_per_seat"]["infant"] = str(int(str(c[33]).split(".")[0]))
            if result["Price_per_seat"]["infant"] == '0.0':
                result["Price_per_seat"]["infant"] = None
            result["Domain"] = 'makevoyage'
            main_result_list.append(result)

            res_json['results'] = {"status": 200, "HasResults": True, "data": main_result_list}

            return res_json


if __name__ == '__main__':
    # data = get_json("AMD", "DXB", "yes", "economy", "2022-09-03", "2022-09-23", 1, 1, 1, 12345)
    param_json = {
        "origin": "GAU",
        "destination": "RUP",
        "is_return": '',
        "flight_class": "",
        "depart_date": "2023-02-21",  # "01-09-2022"
        "return_date": "",
        "adult": "1",
        "child": "0",
        "infant": "0",
        "domain": "makevoyage",
        "key": "test-xbyte"
    }

    #
    data = makevoyage_json(param_json, 12345)
    print(json.dumps(data))
