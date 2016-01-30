#current_exchange_rate
#http://www.google.com/finance?q=TWDUSD
#example usage: getRatio("TWDUSD") 
import requests
import urllib2
def getRatio (countryPair):
    if (internet_on()):
        r = requests.get("http://www.google.com/finance?q=" + countryPair)
        #ratio = float(r.text.split('bld\">')[1].split('<')[0].strip().split(" ")[0])
        return r.text
    else:
    	return 30#False



def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com/finance',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

if __name__ == '__main__':
	print getRatio('TWUSD')
