import glob
import os
import csv
from bs4 import BeautifulSoup

input_dir = "/Users/nicoledominguez/sites/paycheck-scraper/src/html/"
output_dir = "/Users/nicoledominguez/sites/paycheck-scraper/src/"


# Open the HTML file
record = BeautifulSoup(open("src/html/Paycheck-2015-12-24.html"), "html.parser")

f = csv.writer(open("src/paycheck_data.csv", "w"))


   


pay_table = record.find(id="paystub_pay_tbl").find_all('div')

pay_rows = []

for item in pay_table:
	item = item.get_text(",", strip=True).encode('utf-8')
	pay_rows.append(item)

print ",".join(str(x) for x in pay_rows[4:6])

#print total



# print rows
# print ', '.join([str(ro) for ro in rows])



#net = record.find(class="paycheck")

#print net.get_text(",", strip=True)

#for td in net_td:
	#print td.get_text(",", strip=True)

# net = record.find(id="paystub_net_tbl")
#print(net, net_td)
# print(record.prettify())