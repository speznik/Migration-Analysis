import csv

# Function to read data from CSV file
def read_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

# Example usage to access rows and columns
if __name__ == "__main__":
    filename = 'final_filtered_migrant_stock.csv'  # Change this to the name of your CSV file
    output = "outputf.csv"
    
    csv_data = read_csv(filename)
    
    d = {'900': 'WORLD', '108': '   Burundi', '174': '   Comoros', '262': '   Djibouti', '232': '   Eritrea', '231': '   Ethiopia', '404': '   Kenya', '450': '   Madagascar', '454': '   Malawi', '480': '   Mauritius*', '175': '   Mayotte*', '508': '   Mozambique', '638': '   Réunion*', '646': '   Rwanda', '690': '   Seychelles', '706': '   Somalia', '728': '   South Sudan', '800': '   Uganda', '834': '   United Republic of Tanzania*', '894': '   Zambia', '716': '   Zimbabwe', '24': '   Angola', '120': '   Cameroon', '140': '   Central African Republic', '148': '   Chad', '178': '   Congo', '180': '   Democratic Republic of the Congo', '226': '   Equatorial Guinea', '266': '   Gabon', '678': '   Sao Tome and Principe', '12': '   Algeria', '818': '   Egypt', '434': '   Libya', '504': '   Morocco', '729': '   Sudan', '788': '   Tunisia', '732': '   Western Sahara', '72': '   Botswana', '748': '   Eswatini', '426': '   Lesotho', '516': '   Namibia', '710': '   South Africa', '204': '   Benin', '854': '   Burkina Faso', '132': '   Cabo Verde', '384': "   Côte d'Ivoire", '270': '   Gambia', '288': '   Ghana', '324': '   Guinea', '624': '   Guinea-Bissau', '430': '   Liberia', '466': '   Mali', '478': '   Mauritania', '562': '   Niger', '566': '   Nigeria', '654': '   Saint Helena*', '686': '   Senegal', '694': '   Sierra Leone', '768': '   Togo', '398': '   Kazakhstan', '417': '   Kyrgyzstan', '762': '   Tajikistan', '795': '   Turkmenistan', '860': '   Uzbekistan', '156': '   China*', '344': '   China, Hong Kong SAR*', '446': '   China, Macao SAR*', '158': '   China, Taiwan Province of China*', '408': "   Dem. People's Republic of Korea", '392': '   Japan', '496': '   Mongolia', '410': '   Republic of Korea', '96': '   Brunei Darussalam', '116': '   Cambodia', '360': '   Indonesia', '418': "   Lao People's Democratic Republic", '458': '   Malaysia*', '104': '   Myanmar', '608': '   Philippines', '702': '   Singapore', '764': '   Thailand', '626': '   Timor-Leste', '704': '   Viet Nam', '4': '   Afghanistan', '50': '   Bangladesh', '64': '   Bhutan', '356': '   India', '364': '   Iran (Islamic Republic of)', '462': '   Maldives', '524': '   Nepal', '586': '   Pakistan', '144': '   Sri Lanka', '51': '   Armenia', '31': '   Azerbaijan*', '48': '   Bahrain', '196': '   Cyprus*', '268': '   Georgia*', '368': '   Iraq', '376': '   Israel', '400': '   Jordan', '414': '   Kuwait', '422': '   Lebanon', '512': '   Oman', '634': '   Qatar', '682': '   Saudi Arabia', '275': '   State of Palestine*', '760': '   Syrian Arab Republic', '792': '   Turkey', '784': '   United Arab Emirates', '887': '   Yemen', '112': '   Belarus', '100': '   Bulgaria', '203': '   Czechia', '348': '   Hungary', '616': '   Poland', '498': '   Republic of Moldova*', '642': '   Romania', '643': '   Russian Federation', '703': '   Slovakia', '804': '   Ukraine*', '830': '   Channel Islands*', '208': '   Denmark*', '233': '   Estonia', '234': '   Faroe Islands*', '246': '   Finland*', '352': '   Iceland', '372': '   Ireland', '833': '   Isle of Man*', '428': '   Latvia', '440': '   Lithuania', '578': '   Norway*', '752': '   Sweden', '826': '   United Kingdom*', '8': '   Albania', '20': '   Andorra', '70': '   Bosnia and Herzegovina', '191': '   Croatia', '292': '   Gibraltar*', '300': '   Greece', '336': '   Holy See*', '380': '   Italy', '470': '   Malta', '499': '   Montenegro', '807': '   North Macedonia', '620': '   Portugal', '674': '   San Marino', '688': '   Serbia*', '705': '   Slovenia', '724': '   Spain*', '40': '   Austria', '56': '   Belgium', '250': '   France*', '276': '   Germany', '438': '   Liechtenstein', '442': '   Luxembourg', '492': '   Monaco', '528': '   Netherlands*', '756': '   Switzerland', '660': '   Anguilla*', '28': '   Antigua and Barbuda', '533': '   Aruba*', '44': '   Bahamas', '52': '   Barbados', '535': '   Bonaire, Sint Eustatius and Saba*', '92': '   British Virgin Islands*', '136': '   Cayman Islands*', '192': '   Cuba', '531': '   Curaçao*', '212': '   Dominica', '214': '   Dominican Republic', '308': '   Grenada', '312': '   Guadeloupe*', '332': '   Haiti', '388': '   Jamaica', '474': '   Martinique*', '500': '   Montserrat*', '630': '   Puerto Rico*', '652': '   Saint Barthélemy*', '659': '   Saint Kitts and Nevis', '662': '   Saint Lucia', '663': '   Saint Martin (French part)*', '670': '   Saint Vincent and the Grenadines', '534': '   Sint Maarten (Dutch part)*', '780': '   Trinidad and Tobago', '796': '   Turks and Caicos Islands*', '850': '   United States Virgin Islands*', '84': '   Belize', '188': '   Costa Rica', '222': '   El Salvador', '320': '   Guatemala', '340': '   Honduras', '484': '   Mexico', '558': '   Nicaragua', '591': '   Panama', '32': '   Argentina', '68': '   Bolivia (Plurinational State of)', '76': '   Brazil', '152': '   Chile', '170': '   Colombia', '218': '   Ecuador', '238': '   Falkland Islands (Malvinas)*', '254': '   French Guiana*', '328': '   Guyana', '600': '   Paraguay', '604': '   Peru', '740': '   Suriname', '858': '   Uruguay', '862': '   Venezuela (Bolivarian Republic of)', '60': '   Bermuda*', '124': '   Canada', '304': '   Greenland*', '666': '   Saint Pierre and Miquelon*', '840': '   United States of America*', '36': '   Australia*', '554': '   New Zealand*', '242': '   Fiji', '540': '   New Caledonia*', '598': '   Papua New Guinea', '90': '   Solomon Islands', '548': '   Vanuatu', '316': '   Guam*', '296': '   Kiribati', '584': '   Marshall Islands', '583': '   Micronesia (Fed. States of)', '520': '   Nauru', '580': '   Northern Mariana Islands*', '585': '   Palau', '16': '   American Samoa*', '184': '   Cook Islands*', '258': '   French Polynesia*', '570': '   Niue*', '882': '   Samoa', '772': '   Tokelau*', '776': '   Tonga', '798': '   Tuvalu', '876': '   Wallis and Futuna Islands*'}
    # Accessing rows
    print("Rows:")
    i = 0
    temp = []
    for row in csv_data:
        t = row[:3]
        s = row[:2] + row[3:]
        if(i == 0):
            t.append("male/female")
            t.append("Country")
            temp.append(t)
        else:
            t.append("male")
            s.append("female")
            t.append(d[row[1]].lstrip())
            s.append(d[row[1]].lstrip())
            temp.append(t)
            temp.append(s)
        i += 1
    write_csv(output, temp)
    # # Accessing columns
    # print("\nColumns:")
    # for col in zip(*csv_data):
    #     print(col)