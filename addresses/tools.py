import json
import requests
from lxml import objectify
import urllib
from addresses.models import Address

def geocode(address):

    #address = urllib.parse.urlencode(address)
    resp = requests.post("http://ags.cuzk.cz/arcgis/rest/services/RUIAN/Vyhledavaci_sluzba_nad_daty_RUIAN/MapServer/exts/GeocodeSOE/find", data={"text": address, "f":"json"})

    address = resp.json()["locations"][0]["feature"]["attributes"]["Match_addr"]

    with open("/home/jachym/src/czechinvest/data/target/addresscachefile-cuzk.json") as cache: 
        data = json.load(cache)
        for item in data:
            if data[item] and address == data[item]["formatted_address"]:
                return data[item]["id"].replace("AD.", "")

    print("############## going deeper")
    return __cuzk_geocoder(address)

def __cuzk_geocoder(address):

    resp = requests.get("http://services.cuzk.cz/wfs/inspire-AD-wfs.asp?service=WFS&request=GetFeature&version=2.0.0&STOREDQUERY_ID=GetAddressFW&SEARCH_FOR={}".format(address))
    #url = "http://services.cuzk.cz/wfs/inspire-AD-wfs.asp?service=WFS&request=GetFeature&version=2.0.0&STOREDQUERY_ID=GetAddressFW&SEARCH_FOR={}".format(address)
    #print(url)
    root = objectify.fromstring(resp.content)

    if hasattr(root, "member"):

        return int(root.member["{http://inspire.ec.europa.eu/schemas/ad/4.0}Address"].attrib["{http://www.opengis.net/gml/3.2}id"].replace("AD.",""))
    else:
        raise "No address found: f{address}"
