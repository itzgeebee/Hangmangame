# A webscraping script that uses selenium to scrape pay data for college major in the USA from payscale.com
# Creates a csv from the collected data which can be used for data analysis or other projects
# Endeavor to delete the current csv file if you want to run the code 
from data_collect import ScrapeEngine, InputGoogleForms
import pandas as pd
scraper = ScrapeEngine()
data_collector = InputGoogleForms()

# get data from all 34 pages of payscale.com
d = 34
while d > 0:
    scraper.get_details()
    scraper.click_button()
    d-=1

# the early career pay and meid career pay have the same class name 
# so you have to create a new list after scraping the data
new_ecp = []
new_mcp = []
a = 0
b = 1

for i in range(len(scraper.ecp)):
    try:
        new_ecp.append(scraper.ecp[a].replace("$","").replace(",",""))
        new_mcp.append(scraper.ecp[b].replace("$","").replace(",",""))
        
        a += 3
        b += 3
        
    except IndexError:
        break

# Creates a list that will be used for the dataframe
data_list = []
for i in range(len(scraper.major)):
    data_list.append((scraper.major[i], new_ecp[i], new_mcp[i]))

df = pd.DataFrame(data_list, columns = ['column1','column2','column3' ])

# create a csv directly. Much shorter process than filling the google forms
new_csv = df.to_csv("college_salaries.csv", index=False)

# optional. Use google forms to populate collected data... uses an average of 3 hours
for i in range(len(scraper.major)):
    data_collector.enter_data(major=scraper.major[i], ecp=new_ecp[i], mcp=new_mcp[i])