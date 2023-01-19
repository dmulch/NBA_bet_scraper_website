# aux functions that don't have a client call and response
from myap.models import Currency, Teams


def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "https://thefactfile.org/countries-currencies-symbols/"
    response = requests.get(url)
    if not response.status_code == 200:
        return currency_list
    soup = BeautifulSoup(response.content)
    data_lines = soup.find_all('tr') #lines in the list
    for line in data_lines:
        try:
            detail = line.find_all('td')
            currency = detail[2].get_text().strip()
            iso = detail[3].get_text().strip()
            if (currency, iso) in currency_list:
                continue
            currency_list.append((currency, iso))
        except:
            continue
    return currency_list

def add_currencies(currency_list):
    for currency in currency_list:
        currency_name = currency[0]
        currency_symbol = currency[1]
        try:
            c= Currency.objects.get(iso=currency_symbol)
        except:
            c = Currency(long_name=currency_name, iso=currency_symbol)
            #c.save() #To test out the code, replace this by print(c)
            print(c)

def get_teams():
    url = 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations'
    team_out = list()
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    data_lines = soup.find_all('tr')
    for lines in data_lines:
        try:
            td_tags = lines.find_all('td')
            short_name = td_tags[0].get_text().strip()
            long_name = td_tags[1].get_text().strip()

            if short_name.startswith('Abbr') == False:
                #print(short_name + long_name)
                team_out.append((short_name,long_name))
        except:
            continue
    return team_out

def add_teams(team_list):
    for teams in team_list:
        short_names = teams[0]
        long_names = teams[1]
        try:
            t = Teams.objects.get(short_name=short_names)
        except:
            t = Teams(short_name=short_names, long_name=long_names)
            print(t)
            t.save()

def get_currency_rates(iso_code):
    url = "http://www.xe.com/currencytables/?from=" + iso_code
    import requests
    from bs4 import BeautifulSoup
    x_rate_list = list()
    try:
        page_source = BeautifulSoup(requests.get(url).content)
    except:
        return x_rate_list
    data = page_source.find('tbody')
    data_lines = data.find_all('tr')
    for line in data_lines:
        symbol = line.find('th').get_text()
        data=line.find_all('td')
        try:
            x_rate = float(data[2].get_text().strip())
            x_rate_list.append((symbol,x_rate))
        except:
            continue
    return x_rate_list
