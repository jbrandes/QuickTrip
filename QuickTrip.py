from hyperlink import URL


# prints: https://github.com/python-hyper/




def Europe():
    print("Time to plan your trip!")
    url = URL.from_text(u'https://www.kayak.com/flight-routes/United-States-US0/Europe-EU0')
    better_url = url.replace(scheme=u'https', port=443)
    org_url = better_url.click(u'.')

    print(org_url.to_text())



def Africa():
    print("Time to plan your trip!")
    url = URL.from_text(u'https://www.farecompare.com/flights/africa/zone.html?utm_source=google&utm_medium=cpc&utm_campaign=dsa_us_desktop&utm_term=&gclid=EAIaIQobChMI3JzdhMnT4gIVnrfACh1oFQpOEAAYAyAAEgIFHfD_BwE#quote?quoteKey=CCHICJNB20190702R20190709P1CTF')
    better_url = url.replace(scheme=u'https', port=443)
    org_url = better_url.click(u'.')

    print(org_url.to_text())


def Asia():
    print("Time to plan your trip!")
    url = URL.from_text(u'https://www.justfly.com/cheap-flights-to-Asia-2/?campaign=146&route=X-SHA&adgroupid=26220101560&gclid=EAIaIQobChMIqKD4nMnT4gIV07fACh227A5TEAAYASAAEgLFLfD_BwE')
    better_url = url.replace(scheme=u'https', port=443)
    org_url = better_url.click(u'.')

    print(org_url.to_text())


print("Welcome to the program. What is your name?")
name = input()
print("It's nice to meet you " + name)
print("Let's go on a journey. Where would you like to go first: Europe, Africa or Asia?")

dest = input()
if dest == "Europe":
    Europe()
if dest == "Africa":
    Africa()
if dest == "Asia":
    Asia()


