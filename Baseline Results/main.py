import pandas as pd
import pickle
import string

processed_file_path = "Processed_Country_and_Titles.csv"
positional_index_path = "positional_index.pkl"

def preprocess_text(text):
    if isinstance(text, str):  
        text_cleaned = text.lower().translate(str.maketrans('', '', string.punctuation + '0123456789'))
        tokens = [token.strip() for token in text_cleaned.split() if token.strip()]
        return tokens
    else:
        return []

df = pd.read_csv(processed_file_path, converters={'Titles 1': eval, 'Titles 2': eval, 'Titles 3': eval, 'Titles 4': eval, 'Titles 5': eval})

positional_index = {}

for index, row in df.iterrows():
    for column in ['Titles 1', 'Titles 2', 'Titles 3', 'Titles 4', 'Titles 5']:
        tokens = row[column]
        for pos, token in enumerate(tokens):
            if token not in positional_index:
                positional_index[token] = {}
            if index not in positional_index[token]:
                positional_index[token][index] = []
            positional_index[token][index].append(pos)

with open(positional_index_path, 'wb') as f:
    pickle.dump(positional_index, f)

def preprocess_query(query):
    return preprocess_text(query)

def phrase_search(query, positional_index):
    query_tokens = preprocess_query(query)
    phrase_positions = {}
    if query_tokens[0] not in positional_index:
        return []
    initial_positions = positional_index[query_tokens[0]]
    for doc_id in initial_positions:
        for pos in initial_positions[doc_id]:
            match = True
            current_position = pos
            for token in query_tokens[1:]:
                current_position += 1
                if token not in positional_index or doc_id not in positional_index[token] or current_position not in positional_index[token][doc_id]:
                    match = False
                    break
            if match:
                if doc_id not in phrase_positions:
                    phrase_positions[doc_id] = []
                phrase_positions[doc_id].append(pos)
    return phrase_positions

import csv
import os
import string
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk
nltk.download('stopwords')
nltk.download('punkt')

cmap = {'WORLD': '900', 'Burundi': '108', 'Comoros': '174', 'Djibouti': '262', 'Eritrea': '232', 'Ethiopia': '231', 'Kenya': '404', 'Madagascar': '450', 'Malawi': '454', 'Mauritius*': '480', 'Mayotte*': '175', 'Mozambique': '508', 'Réunion*': '638', 'Rwanda': '646', 'Seychelles': '690', 'Somalia': '706', 'South Sudan': '728', 'Uganda': '800', 'United Republic of Tanzania*': '834', 'Zambia': '894', 'Zimbabwe': '716', 'Angola': '24', 'Cameroon': '120', 'Central African Republic': '140', 'Chad': '148', 'Congo': '178', 'Democratic Republic of the Congo': '180', 'Equatorial Guinea': '226', 'Gabon': '266', 'Sao Tome and Principe': '678', 'Algeria': '12', 'Egypt': '818', 'Libya': '434', 'Morocco': '504', 'Sudan': '729', 'Tunisia': '788', 'Western Sahara': '732', 'Botswana': '72', 'Eswatini': '748', 'Lesotho': '426', 'Namibia': '516', 'South Africa': '710', 'Benin': '204', 'Burkina Faso': '854', 'Cabo Verde': '132', "Côte d'Ivoire": '384', 'Gambia': '270', 'Ghana': '288', 'Guinea': '324', 'Guinea-Bissau': '624', 'Liberia': '430', 'Mali': '466', 'Mauritania': '478', 'Niger': '562', 'Nigeria': '566', 'Saint Helena*': '654', 'Senegal': '686', 'Sierra Leone': '694', 'Togo': '768', 'Kazakhstan': '398', 'Kyrgyzstan': '417', 'Tajikistan': '762', 'Turkmenistan': '795', 'Uzbekistan': '860', 'China*': '156', 'China, Hong Kong SAR*': '344', 'China, Macao SAR*': '446', 'China, Taiwan Province of China*': '158', "Dem. People's Republic of Korea": '408', 'Japan': '392', 'Mongolia': '496', 'Republic of Korea': '410', 'Brunei Darussalam': '96', 'Cambodia': '116', 'Indonesia': '360', "Lao People's Democratic Republic": '418', 'Malaysia*': '458', 'Myanmar': '104', 'Philippines': '608', 'Singapore': '702', 'Thailand': '764', 'Timor-Leste': '626', 'Viet Nam': '704', 'Afghanistan': '4', 'Bangladesh': '50', 'Bhutan': '64', 'India': '356', 'Iran (Islamic Republic of)': '364', 'Maldives': '462', 'Nepal': '524', 'Pakistan': '586', 'Sri Lanka': '144', 'Armenia': '51', 'Azerbaijan*': '31', 'Bahrain': '48', 'Cyprus*': '196', 'Georgia*': '268', 'Iraq': '368', 'Israel': '376', 'Jordan': '400', 'Kuwait': '414', 'Lebanon': '422', 'Oman': '512', 'Qatar': '634', 'Saudi Arabia': '682', 'State of Palestine*': '275', 'Syrian Arab Republic': '760', 'Turkey': '792', 'United Arab Emirates': '784', 'Yemen': '887', 'Belarus': '112', 'Bulgaria': '100', 'Czechia': '203', 'Hungary': '348', 'Poland': '616', 'Republic of Moldova*': '498', 'Romania': '642', 'Russian Federation': '643', 'Slovakia': '703', 'Ukraine*': '804', 'Channel Islands*': '830', 'Denmark*': '208', 'Estonia': '233', 'Faroe Islands*': '234', 'Finland*': '246', 'Iceland': '352', 'Ireland': '372', 'Isle of Man*': '833', 'Latvia': '428', 'Lithuania': '440', 'Norway*': '578', 'Sweden': '752', 'United Kingdom*': '826', 'Albania': '8', 'Andorra': '20', 'Bosnia and Herzegovina': '70', 'Croatia': '191', 'Gibraltar*': '292', 'Greece': '300', 'Holy See*': '336', 'Italy': '380', 'Malta': '470', 'Montenegro': '499', 'North Macedonia': '807', 'Portugal': '620', 'San Marino': '674', 'Serbia*': '688', 'Slovenia': '705', 'Spain*': '724', 'Austria': '40', 'Belgium': '56', 'France*': '250', 'Germany': '276', 'Liechtenstein': '438', 'Luxembourg': '442', 'Monaco': '492', 'Netherlands*': '528', 'Switzerland': '756', 'Anguilla*': '660', 'Antigua and Barbuda': '28', 'Aruba*': '533', 'Bahamas': '44', 'Barbados': '52', 'Bonaire, Sint Eustatius and Saba*': '535', 'British Virgin Islands*': '92', 'Cayman Islands*': '136', 'Cuba': '192', 'Curaçao*': '531', 'Dominica': '212', 'Dominican Republic': '214', 'Grenada': '308', 'Guadeloupe*': '312', 'Haiti': '332', 'Jamaica': '388', 'Martinique*': '474', 'Montserrat*': '500', 'Puerto Rico*': '630', 'Saint Barthélemy*': '652', 'Saint Kitts and Nevis': '659', 'Saint Lucia': '662', 'Saint Martin (French part)': '663', 'Saint Vincent and the Grenadines': '670', 'Sint Maarten (Dutch part)': '534', 'Trinidad and Tobago': '780', 'Turks and Caicos Islands*': '796', 'United States Virgin Islands*': '850', 'Belize': '84', 'Costa Rica': '188', 'El Salvador': '222', 'Guatemala': '320', 'Honduras': '340', 'Mexico': '484', 'Nicaragua': '558', 'Panama': '591', 'Argentina': '32', 'Bolivia (Plurinational State of)': '68', 'Brazil': '76', 'Chile': '152', 'Colombia': '170', 'Ecuador': '218', 'Falkland Islands (Malvinas)': '238', 'French Guiana': '254', 'Guyana': '328', 'Paraguay': '600', 'Peru': '604', 'Suriname': '740', 'Uruguay': '858', 'Venezuela (Bolivarian Republic of)': '862', 'Bermuda*': '60', 'Canada': '124', 'Greenland*': '304', 'Saint Pierre and Miquelon*': '666', 'United States of America*': '840', 'Australia*': '36', 'New Zealand*': '554', 'Fiji': '242', 'New Caledonia*': '540', 'Papua New Guinea': '598', 'Solomon Islands': '90', 'Vanuatu': '548', 'Guam*': '316', 'Kiribati': '296', 'Marshall Islands': '584', 'Micronesia (Fed. States of)': '583', 'Nauru': '520', 'Northern Mariana Islands*': '580', 'Palau': '585', 'American Samoa*': '16', 'Cook Islands*': '184', 'French Polynesia*': '258', 'Niue*': '570', 'Samoa': '882', 'Tokelau*': '772', 'Tonga': '776', 'Tuvalu': '798', 'Wallis and Futuna Islands*': '876'}
d = {'900': 'WORLD', '108': 'Burundi', '174': 'Comoros', '262': 'Djibouti', '232': 'Eritrea', '231': 'Ethiopia', '404': 'Kenya', '450': 'Madagascar', '454': 'Malawi', '480': 'Mauritius*', '175': 'Mayotte*', '508': 'Mozambique', '638': 'Réunion*', '646': 'Rwanda', '690': 'Seychelles', '706': 'Somalia', '728': 'South Sudan', '800': 'Uganda', '834': 'United Republic of Tanzania*', '894': 'Zambia', '716': 'Zimbabwe', '24': 'Angola', '120': 'Cameroon', '140': 'Central African Republic', '148': 'Chad', '178': 'Congo', '180': 'Democratic Republic of the Congo', '226': 'Equatorial Guinea', '266': 'Gabon', '678': 'Sao Tome and Principe', '12': 'Algeria', '818': 'Egypt', '434': 'Libya', '504': 'Morocco', '729': 'Sudan', '788': 'Tunisia', '732': 'Western Sahara', '72': 'Botswana', '748': 'Eswatini', '426': 'Lesotho', '516': 'Namibia', '710': 'South Africa', '204': 'Benin', '854': 'Burkina Faso', '132': 'Cabo Verde', '384': "Côte d'Ivoire", '270': 'Gambia', '288': 'Ghana', '324': 'Guinea', '624': 'Guinea-Bissau', '430': 'Liberia', '466': 'Mali', '478': 'Mauritania', '562': 'Niger', '566': 'Nigeria', '654': 'Saint Helena*', '686': 'Senegal', '694': 'Sierra Leone', '768': 'Togo', '398': 'Kazakhstan', '417': 'Kyrgyzstan', '762': 'Tajikistan', '795': 'Turkmenistan', '860': 'Uzbekistan', '156': 'China*', '344': 'China, Hong Kong SAR*', '446': 'China, Macao SAR*', '158': 'China, Taiwan Province of China*', '408': "Dem. People's Republic of Korea", '392': 'Japan', '496': 'Mongolia', '410': 'Republic of Korea', '96': 'Brunei Darussalam', '116': 'Cambodia', '360': 'Indonesia', '418': "Lao People's Democratic Republic", '458': 'Malaysia*', '104': 'Myanmar', '608': 'Philippines', '702': 'Singapore', '764': 'Thailand', '626': 'Timor-Leste', '704': 'Viet Nam', '4': 'Afghanistan', '50': 'Bangladesh', '64': 'Bhutan', '356': 'India', '364': 'Iran (Islamic Republic of)', '462': 'Maldives', '524': 'Nepal', '586': 'Pakistan', '144': 'Sri Lanka', '51': 'Armenia', '31': 'Azerbaijan*', '48': 'Bahrain', '196': 'Cyprus*', '268': 'Georgia*', '368': 'Iraq', '376': 'Israel', '400': 'Jordan', '414': 'Kuwait', '422': 'Lebanon', '512': 'Oman', '634': 'Qatar', '682': 'Saudi Arabia', '275': 'State of Palestine*', '760': 'Syrian Arab Republic', '792': 'Turkey', '784': 'United Arab Emirates', '887': 'Yemen', '112': 'Belarus', '100': 'Bulgaria', '203': 'Czechia', '348': 'Hungary', '616': 'Poland', '498': 'Republic of Moldova*', '642': 'Romania', '643': 'Russian Federation', '703': 'Slovakia', '804': 'Ukraine*', '830': 'Channel Islands*', '208': 'Denmark*', '233': 'Estonia', '234': 'Faroe Islands*', '246': 'Finland*', '352': 'Iceland', '372': 'Ireland', '833': 'Isle of Man*', '428': 'Latvia', '440': 'Lithuania', '578': 'Norway*', '752': 'Sweden', '826': 'United Kingdom*', '8': 'Albania', '20': 'Andorra', '70': 'Bosnia and Herzegovina', '191': 'Croatia', '292': 'Gibraltar*', '300': 'Greece', '336': 'Holy See*', '380': 'Italy', '470': 'Malta', '499': 'Montenegro', '807': 'North Macedonia', '620': 'Portugal', '674': 'San Marino', '688': 'Serbia*', '705': 'Slovenia', '724': 'Spain*', '40': 'Austria', '56': 'Belgium', '250': 'France*', '276': 'Germany', '438': 'Liechtenstein', '442': 'Luxembourg', '492': 'Monaco', '528': 'Netherlands*', '756': 'Switzerland', '660': 'Anguilla*', '28': 'Antigua and Barbuda', '533': 'Aruba*', '44': 'Bahamas', '52': 'Barbados', '535': 'Bonaire, Sint Eustatius and Saba*', '92': 'British Virgin Islands*', '136': 'Cayman Islands*', '192': 'Cuba', '531': 'Curaçao*', '212': 'Dominica', '214': 'Dominican Republic', '308': 'Grenada', '312': 'Guadeloupe*', '332': 'Haiti', '388': 'Jamaica', '474': 'Martinique*', '500': 'Montserrat*', '630': 'Puerto Rico*', '652': 'Saint Barthélemy*', '659': 'Saint Kitts and Nevis', '662': 'Saint Lucia', '663': 'Saint Martin (French part)', '670': 'Saint Vincent and the Grenadines', '534': 'Sint Maarten (Dutch part)', '780': 'Trinidad and Tobago', '796': 'Turks and Caicos Islands*', '850': 'United States Virgin Islands*', '84': 'Belize', '188': 'Costa Rica', '222': 'El Salvador', '320': 'Guatemala', '340': 'Honduras', '484': 'Mexico', '558': 'Nicaragua', '591': 'Panama', '32': 'Argentina', '68': 'Bolivia (Plurinational State of)', '76': 'Brazil', '152': 'Chile', '170': 'Colombia', '218': 'Ecuador', '238': 'Falkland Islands (Malvinas)', '254': 'French Guiana', '328': 'Guyana', '600': 'Paraguay', '604': 'Peru', '740': 'Suriname', '858': 'Uruguay', '862': 'Venezuela (Bolivarian Republic of)', '60': 'Bermuda*', '124': 'Canada', '304': 'Greenland*', '666': 'Saint Pierre and Miquelon*', '840': 'United States of America*', '36': 'Australia*', '554': 'New Zealand*', '242': 'Fiji', '540': 'New Caledonia*', '598': 'Papua New Guinea', '90': 'Solomon Islands', '548': 'Vanuatu', '316': 'Guam*', '296': 'Kiribati', '584': 'Marshall Islands', '583': 'Micronesia (Fed. States of)', '520': 'Nauru', '580': 'Northern Mariana Islands*', '585': 'Palau', '16': 'American Samoa*', '184': 'Cook Islands*', '258': 'French Polynesia*', '570': 'Niue*', '882': 'Samoa', '772': 'Tokelau*', '776': 'Tonga', '798': 'Tuvalu', '876': 'Wallis and Futuna Islands*'}

# Preprocessing and Storing the results
def PreProcess():
    entries = {}
    filename = "output.csv"
    idx = 1
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            entries[idx] = row
            idx += 1
    return entries

def InvertedIndex(entries):
    table = {}
    # Reading Preprocessed results
    for key, value in entries.items():
        if value[-2] == "male":
            if "male" in table:
                table["male"].append(key)
            else:
                table["male"] = [key]
        else:
            if "female" in table:
                table["female"].append(key)
            else:
                table["female"] = [key]
        
        if value[1] in table:
            if value[1] in table:
                table[value[1]].append(key)
            else:
                table[value[1]] = [key]
        else:
            table[value[1]] = [key]
    return table

def PositionalIndex():
    table = {}
    # Reading Preprocessed results
    for doc in range(1, 1000):
        file = open(f"./Processed_result/file{doc}.obj", 'rb')
        object_file = pickle.load(file)
        for idx in range(len(object_file)):
            word = object_file[idx]
            if word in table:
                if(table[word][-1][0] == doc):
                    table[word][-1][1].append(idx)
                else:
                    table[word].append([doc, [idx]])
            else:
                temp = [doc, [idx]]
                table[word] = [temp]
        file.close()
    
    # Dumping positional index
    filehandler = open(f"positional_index.obj","wb")
    pickle.dump(table, filehandler)
    filehandler.close()

def helper(token, table):
    if token not in table:
        return []
    return table[token]

def NOT(docs1):
    res = []
    i = 1
    idx = 0
    while ((idx < len(docs1)) and (i < 1000)):
        if(i == docs1[idx]):      
            i += 1
        elif(i < docs1[idx]):
            res.append(i)
            i += 1
        elif(i > docs1[idx]):
            idx += 1
    
    while(i < 1000):
        res.append(i)
        i += 1
    
    return res

def AND(docs1, docs2):
    res = []
    i, j = 0, 0
    while(i < len(docs1) and j < len(docs2)):
        if(docs1[i] == docs2[j]):
            res.append(docs1[i])
            i += 1
            j += 1
        elif(docs1[i] < docs2[j]):
            i += 1
        else:
            j += 1  
    
    return res

def OR(docs1, docs2):
    res = []
    i, j = 0, 0
    while(i < len(docs1) and j < len(docs2)):
        if(docs1[i] == docs2[j]):
            res.append(docs1[i])
            i += 1
            j += 1
        elif(docs1[i] < docs2[j]):
            res.append(docs1[i])
            i += 1
        else:
            res.append(docs2[j])
            j += 1  

    while(i < len(docs1)):
        res.append(docs1[i])
        i += 1

    while(j < len(docs2)):
        res.append(docs2[j])
        j += 1

    return res

def ANDNOT(docs1, docs2):
    return AND(docs1, NOT(docs2))

def ORNOT(docs1, docs2):
    return OR(docs1, NOT(docs2))

def QueryInv(InputSeq, ops, table):
    tokens = InputSeq.split()
    X = ""
    for i in range(len(ops)):
        X += tokens[i] + " " + ops[i] + " "
    X += tokens[-1]
    last = helper(tokens[0], table)
    itr = 1
    for op in ops:
        if (op == "AND"):
            op1 = last
            op2 = helper(cmap[tokens[itr]], table)
            last = AND(op1, op2)
        elif (op == "OR"):
            op1 = last
            op2 = helper(tokens[itr], table)
            last = OR(op1, op2)
        elif (op == "AND NOT"):
            op1 = last
            op2 = helper(tokens[itr], table)
            last = ANDNOT(op1, op2)
        elif (op == "OR NOT"):
            op1 = last
            op2 = helper(tokens[itr], table)
            last = ORNOT(op1, op2)
        
        itr += 1

    return X, last

def Last(word, position, doc, table):
    if word == None:
        return True
    
    for dc in table[word]:
        if (dc[0] == doc):
            if position in dc[1]:
                return True

    return False

def Output(lst):
    out = ""
    for doc in lst:
        out += "file" + str(doc) + ".txt, "
    return out[:-2]

def _Output(lst, entries):
    res = []
    for x in lst:
        res.append(entries[x])
    return res

def Boolean(table, entries,InputSeq,ops):
    print("LOOK HERE MDFFFF")
    InputSeq = InputSeq + " " + ops
    print(InputSeq)
    print("AND")
    ops = ["AND"]
    X, docs = QueryInv(InputSeq, ops, table)
    print(f"Query : " + X)
    print(f"Number of documents retrieved for query : {len(docs)}")
    # print(type(docs))
    # print(type(docs[0]))
    # print(docs)
    # sorted_entries = sorted(entries, key=lambda x: float(x[2]))
    # print(f"Names of the documents retrieved for query : {_Output(docs, entries)}")
    lst = []
    for doc in docs:
        lst.append(entries[doc])
    
    lst.sort(key=lambda x: float(x[2]))
    lst.reverse()

    flst = lst[:5]
    countries = []
    for x in flst:
        countries.append(d[x[0]])
    # print(countries)
    return countries
    # N = int(input("\nEnter N: "))
    # for query in range(N):
        # InputSeq = "gender"
        # ops = "origin"
        # ops = input("Enter Operations: ").split(',')
        # for op in range(len(ops)):
            # ops[op] = ops[op].lstrip().rstrip()
        
entries = PreProcess()
    # Constructing and Saving Inverted Index
table = InvertedIndex(entries)



import ast
from flask import Flask, render_template, jsonify, request, session
from flask_pymongo import PyMongo
import openai

openai.api_key = ""


app = Flask(__name__)
# YuUivnDHe2WU7ifl
# avinash21028

app.config["MONGO_URI"] = "mongodb+srv://avinash21028:YuUivnDHe2WU7ifl@cluster1.3gpsmmq.mongodb.net/chatgpt"
mongo = PyMongo(app)



@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    # print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        # print("hefre printtin the request", request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        # print("here printtin the chat:",  chat)
        session_data = session.get("session_data", {"messages": []})
#         question = request.json.get("question")
#         chat = mongo.db.chats.find_one({"question": question})
#         print("chat is pringted here", chat)
        session_data["messages"].append({"role": "user", "content": "You are a helpful assistant. Your task is to analyze user prompts and extract specific details to form a response in a specific dictionary format. The required details are: country of origin, age group, sex, preferred destination country, and general remarks summarizing the user's request in 4-5 keywords. Age groups are defined as: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75+.  Once you have all required information, return the response in the following dictionary format: {'country_of_origin': '<answer_as_from_information_provided_by_user>', 'age_group': '<answer_as_from_information_provided_by_user>', 'sex': '<answer_as_from_information_provided_by_user either male or female>', 'preferred_destination_country': '<answer_as_from_information_provided_by_user>', 'remarks': '<answer_as_from_information_provided_by_user>'}. Output only the dictionary content when all required information is available. Use the user's input to fill the dictionary appropriately, Remeber that if there is some thing missing from the infromation provied by the user then you shoudl ask the user to provide that infromation instead of printing the dictionary. The Prompt:\n" + question + "Remember that if there is anything in the dictionary values which isnt provided by the user then you should ask the user in the response of the prompt about the missing informaiton."})
        # if chat:
            # data = {"question": question, "answer": f"{chat['answer']}"}
            # print("am i doomed")
            # return jsonify(data)
        # else:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=session_data["messages"],
        temperature=1,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
        )
        # print("here we are printing the response", response)
        try: 
            if response["choices"]:
                answer = response["choices"][0]["message"]["content"]
                # print("here is the respone finalluy", answer)
                # # Initialize or update session data based on the response
                # if "provide" in answer.lower():
                #     session_data = session.get("session_data", {"messages": []})
                #     session_data["messages"].append({"role": "system", "content": answer})
                #     print("Finally here")
                # else:
                #     session_data = {"messages": []}
                # session["session_data"] = session_data
                # Save the Q&A pair to the database
                # print("are we even saving the dat somewehre\n\n\n\n\n")
                # print(answer)
                # print("here is the question:",question)
                mongo.db.chats.insert_one({"question": question, "answer": answer})
                data = {"question": question, "answer": answer}
            else:
                data = {"error": "No response generated."}
        except Exception as e:
            # print(f"Error: {e}")
            # It's good practice to make the error message helpful for debugging
            data = {"error": f"Failed to generate response due to an exception: {str(e)}"}
        # print(response)
        # data = {"question": question, "answer": response["choices"][0]["text"]}
        # print("are we even sving the data somwwehere")
        # print("quesiton is this one: ",question)
        # print(data)
        corrected_answer_str = data["answer"]
        # print("Here is hte most importantthing \n\n\n\n\n\n\n ",corrected_answer_str)
        user_response = ast.literal_eval(corrected_answer_str)
        print(user_response)
        country = user_response["country_of_origin"]
        gender = user_response["sex"]
        # Boolean(table, entries,gender,country)
        countries = Boolean(table, entries, gender, country)

        session_data = session.get("session_data", {"messages": []})
#         question = request.json.get("question")
#         chat = mongo.db.chats.find_one({"question": question})
#         print("chat is pringted here", chat)
        session_data["messages"].append({"role": "user", "content": "following are the details of the user " + " {'country_of_origin': "+user_response["country_of_origin"]+", 'age_group': "+user_response["age_group"]+" 'sex': "+user_response["sex"]+", 'preferred_destination_country': "+user_response["preferred_destination_country"]+"'remarks': "+user_response["remarks"]+"'}" + " and based on the above detials our model has give the preference to following cuontries in order: " +  countries[0] + " " + countries[1] + " " +  countries[2] + " " + countries[3] + " " +  countries[4] + " NOw I want you to convey these results to the user and convince him that according to his needs these coutnries are the best. Explain your countrywise reasoning and step by step and comprehensively!!!. Our name if Travel Guru and our company name is IR Project"})


        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=session_data["messages"],
        temperature=0.8,
        max_tokens=512,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
        )
        example_query = user_response["remarks"]
        search_results = phrase_search(example_query, positional_index)

        print(search_results)



        mongo.db.chats.insert_one({"question": question, "answer": data["answer"]})
        data["answer"] = response["choices"][0]["message"]["content"]
        return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
        
    return jsonify(data)


app.run(host='0.0.0.0',debug=True, port=5000)
