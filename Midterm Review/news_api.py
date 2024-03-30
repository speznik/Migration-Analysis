import csv
import requests
import time
API_KEY = 'pub_40995f8d05094917516c0e95b0551378d91af'

BASE_URL = 'https://newsdata.io/api/1/news'

countries = {
    'af': 'Afghanistan', 'al': 'Albania', 'dz': 'Algeria', 'ad': 'Andorra',
    'ao': 'Angola', 'ar': 'Argentina', 'am': 'Armenia', 'au': 'Australia',
    'at': 'Austria', 'az': 'Azerbaijan', 'bs': 'Bahamas', 'bh': 'Bahrain',
    'bd': 'Bangladesh', 'bb': 'Barbados', 'by': 'Belarus', 'be': 'Belgium',
    'bz': 'Belize', 'bj': 'Benin', 'bm': 'Bermuda', 'bt': 'Bhutan',
    'bo': 'Bolivia', 'ba': 'Bosnia And Herzegovina', 'bw': 'Botswana',
    'br': 'Brazil', 'bn': 'Brunei', 'bg': 'Bulgaria', 'bf': 'Burkina Faso',
    'bi': 'Burundi', 'kh': 'Cambodia', 'cm': 'Cameroon', 'ca': 'Canada',
    'cv': 'Cape Verde', 'ky': 'Cayman Islands', 'cf': 'Central African Republic',
    'td': 'Chad', 'cl': 'Chile', 'cn': 'China', 'co': 'Colombia',
    'km': 'Comoros', 'cg': 'Congo', 'cr': 'Costa Rica', 'hr': 'Croatia',
    'cu': 'Cuba', 'cy': 'Cyprus', 'cz': 'Czech Republic', 'dk': 'Denmark',
    'dj': 'Djibouti', 'dm': 'Dominica', 'do': 'Dominican Republic', 'cd': 'DR Congo',
    'ec': 'Ecuador', 'eg': 'Egypt', 'sv': 'El Salvador', 'gq': 'Equatorial Guinea',
    'er': 'Eritrea', 'ee': 'Estonia', 'sz': 'Eswatini', 'et': 'Ethiopia',
    'fj': 'Fiji', 'fi': 'Finland', 'fr': 'France', 'pf': 'French Polynesia',
    'ga': 'Gabon', 'gm': 'Gambia', 'ge': 'Georgia', 'de': 'Germany',
    'gh': 'Ghana', 'gr': 'Greece', 'gd': 'Grenada', 'gt': 'Guatemala',
    'gn': 'Guinea', 'gy': 'Guyana', 'ht': 'Haiti', 'hn': 'Honduras',
    'hk': 'Hong Kong', 'hu': 'Hungary', 'is': 'Iceland', 'in': 'India',
    'id': 'Indonesia', 'ir': 'Iran', 'iq': 'Iraq', 'ie': 'Ireland',
    'il': 'Israel', 'it': 'Italy', 'ci': 'Ivory Coast', 'jm': 'Jamaica',
    'jp': 'Japan', 'je': 'Jersey', 'jo': 'Jordan', 'kz': 'Kazakhstan',
    'ke': 'Kenya', 'ki': 'Kiribati', 'xk': 'Kosovo', 'kw': 'Kuwait',
    'kg': 'Kyrgyzstan', 'la': 'Laos', 'lv': 'Latvia', 'lb': 'Lebanon',
    'ls': 'Lesotho', 'lr': 'Liberia', 'ly': 'Libya', 'li': 'Liechtenstein',
    'lt': 'Lithuania', 'lu': 'Luxembourg', 'mo': 'Macau', 'mk': 'Macedonia',
    'mg': 'Madagascar', 'mw': 'Malawi', 'my': 'Malaysia', 'mv': 'Maldives',
    'ml': 'Mali', 'mt': 'Malta', 'mh': 'Marshall Islands', 'mr': 'Mauritania',
    'mu': 'Mauritius', 'mx': 'Mexico', 'fm': 'Micronesia', 'md': 'Moldova',
    'mc': 'Monaco', 'mn': 'Mongolia', 'me': 'Montenegro', 'ma': 'Morocco',
    'mz': 'Mozambique', 'mm': 'Myanmar', 'na': 'Namibia', 'nr': 'Nauru',
    'np': 'Nepal', 'nl': 'Netherlands', 'nz': 'New Zealand', 'ni': 'Nicaragua',
    'ne': 'Niger', 'ng': 'Nigeria', 'kp': 'North Korea', 'no': 'Norway',
    'om': 'Oman', 'pk': 'Pakistan', 'pw': 'Palau', 'pa': 'Panama',
    'pg': 'Papua New Guinea', 'py': 'Paraguay', 'pe': 'Peru', 'ph': 'Philippines',
    'pl': 'Poland', 'pt': 'Portugal', 'pr': 'Puerto Rico', 'qa': 'Qatar',
    'ro': 'Romania', 'ru': 'Russia', 'rw': 'Rwanda', 'ws': 'Samoa',
    'sm': 'San Marino', 'sa': 'Saudi Arabia', 'sn': 'Senegal', 'rs': 'Serbia',
    'sc': 'Seychelles', 'sl': 'Sierra Leone', 'sg': 'Singapore', 'sk': 'Slovakia',
    'si': 'Slovenia', 'sb': 'Solomon Islands', 'so': 'Somalia', 'za': 'South Africa',
    'kr': 'South Korea', 'es': 'Spain', 'lk': 'Sri Lanka', 'sd': 'Sudan',
    'sr': 'Suriname', 'se': 'Sweden', 'ch': 'Switzerland', 'sy': 'Syria',
    'tw': 'Taiwan', 'tj': 'Tajikistan', 'tz': 'Tanzania', 'th': 'Thailand',
    'tl': 'Timor-Leste', 'tg': 'Togo', 'to': 'Tonga', 'tn': 'Tunisia',
    'tr': 'Turkey', 'tm': 'Turkmenistan', 'tv': 'Tuvalu', 'ug': 'Uganda',
    'ua': 'Ukraine', 'ae': 'United Arab Emirates', 'gb': 'United Kingdom',
    'us': 'United States of America', 'uy': 'Uruguay', 'uz': 'Uzbekistan',
    'vu': 'Vanuatu', 'va': 'Vatican', 've': 'Venezuela', 'vi': 'Vietnam',
    'ye': 'Yemen', 'zm': 'Zambia', 'zw': 'Zimbabwe'
}


csv_file = 'migration_news_by_country.csv'

def fetch_news_for_country(country_code):
    params = {
        'apikey': API_KEY,
        'q': 'migration',
        'country': country_code,
        'language': 'en'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Failed to fetch articles for {country_code}", response.status_code)
        return []

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country ID', 'Country Name', '1st tuple', '2nd tuple', '3rd tuple', '4th tuple', '5th tuple', '6th tuple', '7th tuple', '8th tuple', '9th tuple', '10th tuple'])
    
    for code, name in countries.items():
        articles = fetch_news_for_country(code)
        article_data = []
        for article in articles:
            title = article.get('title', 'No Title')
            description = article.get('description', 'No Description')
            url = article.get('link', '#')
            article_data.append((title, description, url))
        
        while len(article_data) < 10:
            article_data.append(('No Title', 'No Description', '#'))
        
        writer.writerow([code, name] + article_data)

print(f"CSV file '{csv_file}' has been created.")
