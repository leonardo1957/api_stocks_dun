import requests
from bs4 import BeautifulSoup

def scrape_marketwatch(stock_symbol):
    url = f"https://www.marketwatch.com/investing/stock/{stock_symbol}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data for {stock_symbol}, status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    performance_data = {}
    try:
        performance_section = soup.find('div', {'class': 'element element--table performance'})
        performance_data = {
            'five_days': float(performance_section.find('td', text='5 Day').find_next_sibling('td').text.strip('%')) / 100,
            'one_month': float(performance_section.find('td', text='1 Month').find_next_sibling('td').text.strip('%')) / 100,
            'three_months': float(performance_section.find('td', text='3 Month').find_next_sibling('td').text.strip('%')) / 100,
            'year_to_date': float(performance_section.find('td', text='YTD').find_next_sibling('td').text.strip('%')) / 100,
            'one_year': float(performance_section.find('td', text='1 Year').find_next_sibling('td').text.strip('%')) / 100
        }
    except AttributeError:
        raise Exception(f"Failed to parse performance data for {stock_symbol}")

    competitors = []
    try:
        competitors_section = soup.find('div', {'class': 'element element--table competitors'})
        for row in competitors_section.find_all('tr')[1:]:
            columns = row.find_all('td')
            name = columns[0].text.strip()
            market_cap = columns[1].text.strip()
            currency, value = market_cap.split(' ')
            competitors.append({
                'name': name,
                'market_cap': {
                    'currency': currency,
                    'value': float(value.replace(',', ''))
                }
            })
    except AttributeError:
        raise Exception(f"Failed to parse competitors data for {stock_symbol}")

    return performance_data, competitors
