import pandas as pd

#Examples
usa_articles = [
    ("Massive Cyberattack Targets Financial Institutions", "A coordinated cyberattack has hit several major financial institutions, highlighting vulnerabilities in the nation's cybersecurity defenses."),
    ("Supreme Court Upholds New Gun Control Measures", "In a landmark ruling, the Supreme Court upholds new gun control measures aimed at reducing gun violence."),
    ("Breakthrough in Alzheimer's Research Announced", "Scientists announce a breakthrough in Alzheimer's research, offering hope for millions affected by the disease."),
    ("Major League Baseball Expands to Mexico", "Major League Baseball announces the addition of a new team based in Mexico, marking the league's first expansion outside the United States and Canada."),
    ("Historic Climate Agreement Reached at International Summit", "The United States leads a historic agreement on climate change, committing to unprecedented emission reductions at an international summit."),
    ("Unemployment Hits Record Low", "The unemployment rate drops to a record low, signaling strong economic growth and stability."),
    ("NASA Plans Manned Mars Mission", "NASA unveils plans for its first manned mission to Mars, scheduled for the next decade."),
    ("New Immigration Policy Opens Path to Citizenship", "A new immigration policy has been introduced, offering a path to citizenship for millions of undocumented immigrants."),
    ("Federal Reserve Announces Interest Rate Hike", "The Federal Reserve announces a significant interest rate hike in response to rising inflation."),
    ("Opioid Crisis: New Legislation Targets Pharmaceutical Companies", "Congress passes new legislation targeting pharmaceutical companies in an effort to combat the ongoing opioid crisis.")
]

india_articles = [
    ("India to Host Next UN Climate Conference", "India is set to host the next United Nations Climate Change Conference, focusing on global efforts to reduce carbon emissions."),
    ("Groundbreaking Rural Internet Initiative Launched", "A new initiative to bring high-speed internet to rural areas across India has been launched, aiming to bridge the digital divide."),
    ("Record Growth in Renewable Energy Sector", "India's renewable energy sector sees record growth, with significant investments in solar and wind power."),
    ("Supreme Court Decriminalizes Certain Privacy Laws", "In a landmark ruling, the Supreme Court decriminalizes certain privacy laws, enhancing personal freedoms."),
    ("National Electric Vehicle Policy Announced", "The government announces a national policy to promote the use of electric vehicles, with incentives for manufacturers and consumers."),
    ("India's First Underwater Bullet Train Project", "The government unveils plans for India's first underwater bullet train, connecting major cities through state-of-the-art technology."),
    ("Monsoon Forecasting System Improvements", "Significant improvements in monsoon forecasting aim to mitigate the impacts of seasonal rains on agriculture and urban areas."),
    ("New Space Research Initiative Targets Asteroid Mining", "ISRO announces a new space research initiative focusing on asteroid mining, aiming to harness space resources."),
    ("India Wins Bid to Host Olympic Games", "India wins the bid to host the upcoming Olympic Games, a historic first for the country."),
    ("Major Reforms in Public Health Insurance", "The government announces major reforms in public health insurance, expanding coverage and access to healthcare services.")
]

all_articles = usa_articles + india_articles

df_articles = pd.DataFrame({
    "Country": ["USA"] * len(usa_articles) + ["India"] * len(india_articles),
    "Article Title": [article[0] for article in all_articles],
    "Summary": [article[1] for article in all_articles]
})

csv_file_path = "news_articles.csv"
df_articles.to_csv(csv_file_path, index=False)

print(f"CSV file has been created at: {csv_file_path}")
