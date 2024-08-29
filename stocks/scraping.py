import requests
from bs4 import BeautifulSoup

def scrape_marketwatch(stock_symbol):
    stock_symbol = stock_symbol.lower()
    url = f"https://www.marketwatch.com/investing/stock/{stock_symbol}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Cookie": "refresh=off; letsGetMikey=enabled; mw_loc=%7B%22Region%22%3A%22SC%22%2C%22Country%22%3A%22BR%22%2C%22Continent%22%3A%22NA%22%2C%22ApplicablePrivacy%22%3A0%7D; gdprApplies=false; ab_uuid=b5fdf5e2-6ac6-4a06-b0d2-118854e1299a; fullcss-section=section-6ce9341cfd.min.css; refresh=off; icons-loaded=true; letsGetMikey=enabled; _lr_geo_location_state=SC; _lr_geo_location=BR; _pubcid=8a9a8245-f30c-41a5-b71d-668d309fb8e0; _pubcid_cst=DCwOLBEsaQ%3D%3D; _sp_su=false; permutive-id=27fbab6c-9e9d-4157-9d2c-1ee9b756ba8b; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; _ncg_domain_id_=1613ab64-a0d2-4f37-bbac-9aa35b42d77e.1.1724865033.1756401033; ajs_anonymous_id=0a82bbe7-b9fe-4218-8252-c62c6073ae08; _fbp=fb.1.1724865034303.1672969768; _meta_facebookTag_sync=1724865034304; _ncg_g_id_=368cf919-78b6-447b-b8f0-16e15b1067b7.3.1724865034.1756401033; _pcid=%7B%22browserId%22%3A%22m0e43udmahav02hr%22%7D; cX_P=m0e43udmahav02hr; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIE4AmHgZi4CsvAIwB2DqIAMADkHTRvEAF8gA; _meta_cross_domain_id=3ad1c536-8fb2-44de-a9b9-99b4b3fdecef; _meta_cross_domain_recheck=1724865034670; _ncg_id_=; s_cc=true; _ga=GA1.1.94768172.1724865035; _gcl_au=1.1.993566803.1724865035; _scor_uid=6f245566521c445197cd895184f40ac7; _dj_sp_id=5b468ce5-4b42-43af-ab30-c4e5f90473f5; cX_G=cx%3A3tdjy536h61yx28uhg9zrznayh%3A2fzzc4wpyelqs; fullcss-quote=quote-4deea2bb10.min.css; recentqsmkii=Stock-US-AAPL; _ncg_sp_ses.f57d=*; _dj_ses.cff7=*; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C19964%7CMCMID%7C27025784814243904541218141341505755730%7CMCAAMLH-1725496061%7C4%7CMCAAMB-1725496061%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724898461s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19971%7CvVersion%7C4.4.0; utag_main=v_id:019199f7b5350022dc97f0eea01e05065004805d00bd0$_sn:2$_ss:0$_st:1724893491512$vapi_domain:marketwatch.com$ses_id:1724891260759%3Bexp-session$_pn:3%3Bexp-session$_prevpage:MW_Quote_Page%3Bexp-1724895291522; _dj_id.cff7=.1724865035.2.1724891692.1724865048.1908bc1a-d6a1-4b52-ad09-ae0ef552a22f; _ga_K2H7B9JRSS=GS1.1.1724891261.2.1.1724891692.59.0.0; _ncg_sp_id.f57d=.1724865035.2.1724891692.1724865048.656aa1e5-cbf5-4a7e-a4d2-46ee94bdda84.1f9d9cdc-800b-49fe-9cec-b3702741d066.8ff3d189-2bf8-4583-993a-b6fa25a52f57.1724891260955.7; _rdt_uuid=1724865034693.44398b43-98ca-4bd9-bcef-c5af18572efb; datadome=UJzKpQjQpbhG7Mempk1i9Ju~JkmMEyIFfZ6cecBXekRB0X5e8nY4d9ZSp3_N6LRdqpMZVveCxCi~8h8payIScK0_7HU7hmSSBBhNev6ZHYJ7IYx4xwD6BwG~s9EbYvIe; s_tp=3292; s_ppv=MW_Quote_Page%2C29%2C29%2C959",
        "Priority": "u=0, i",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data for {stock_symbol}, status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    performance_data = {}
    try:
        performance_section = soup.find('div', {'class': 'element element--table performance'})

        def extract_performance_data(label):
            cell = performance_section.find('td', text=label).find_next('td')
            value = cell.text.replace('\n', '').strip().strip('%')
            return float(value) / 100
        
        performance_data = {
            'five_days': extract_performance_data('5 Day'),
            'one_month': extract_performance_data('1 Month'),
            'three_months': extract_performance_data('3 Month'),
            'year_to_date': extract_performance_data('YTD'),
            'one_year': extract_performance_data('1 Year')
        }
    except AttributeError:
        raise Exception(f"Failed to parse performance data for {stock_symbol}")

    competitors = []
    try:
        competitors_section = soup.find('div', {'class': 'element element--table overflow--table Competitors'})
        rows = competitors_section.find_all('tr')[1:]
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:
                name = columns[0].text.strip()
                market_cap = columns[2].text.strip()
                try:
                    if market_cap.startswith('$'):
                        currency = 'USD'
                        value = market_cap[1:].replace(',', '')
                    elif market_cap.startswith('₩'):
                        currency = 'KRW'
                        value = market_cap[1:].replace(',', '')
                    elif market_cap.startswith('¥'):
                        currency = 'JPY'
                        value = market_cap[1:].replace(',', '')
                    else:
                        continue
                    
                    value = float(value)
                    competitors.append({
                        'name': name,
                        'market_cap': {
                            'currency': currency,
                            'value': value
                        }
                    })
                except ValueError:
                    continue
    except AttributeError:
        raise Exception(f"Failed to parse competitors data for {stock_symbol}")

    return performance_data, competitors
