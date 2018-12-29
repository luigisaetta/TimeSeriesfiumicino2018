import urllib.request
from bs4 import BeautifulSoup

# base URL, must be concatenated with thedate
# it embeds FCO, for "Fiumicino Airport"
baseUrl = "http://www.adr.it/bsn-dati-di-traffico?p_p_id=1_WAR_trafficdataportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=1&p_p_col_count=2&_1_WAR_trafficdataportlet_tabs1=FCO&_1_WAR_trafficdataportlet_dataRif="

# the function that gets the page corresponding to the date 
# parse it and extract the number (of passenger)
# thedate must be like "201002"
#
#return the # of passengers
def getData(thedate):

    myURL =  baseUrl + thedate

    page = urllib.request.urlopen(myURL)
    soup = BeautifulSoup(page, 'html.parser')

    all_tables=soup.find_all('table')

    # print(all_tables)

    right_table = all_tables[0]

    # get the right row
    i = 0
    for row in right_table.findAll("td"):
        i = i + 1
        if i == 5:
            psg = row.find(text=True).replace(".","")
    return psg

#
#
# Main
#
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

#header 
print("month, passengers")

# loop over yers and months
for year in range(2004,2019):
    # print(year)
    for m in months:
        thedate = str(year)+m
        
        # gets passengers for year and month
        psg = getData(thedate)
        # psg is the number of passegnergs in transit for thedate
        
        print('"' + str(year) + '-' + m + '"' + ',' + psg)
        # the print can be redirected using Unix re-direction, in a file
 