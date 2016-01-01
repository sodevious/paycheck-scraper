import glob
import os
import csv
from bs4 import BeautifulSoup

input_dir = "/Users/nicoledominguez/sites/paycheck-scraper/src/html/"
output_dir = "/Users/nicoledominguez/sites/paycheck-scraper/src/"


# Open the HTML file
# record = BeautifulSoup(open("src/html/Paycheck-2015-12-24.html"), "html.parser")

f = csv.writer(open("src/paycheck_data.csv", "w"))


for file_name in glob.glob(input_dir+ "*.html"):
    with open(file_name) as fp:
        record = BeautifulSoup(fp, "html.parser")
	
	date = record.find(id="paystub_form_tbl").td.get_text(strip=True).strip("Pay stub for period:").lstrip()

	# f.writerow(["Date", "Total Pay", "Net Pay", "Hours", "Rate", "Deductions"]) # Write column headers as the first line
	
	print file_name

	f.writerow([date])

   


summary = record.find(id="paystub_summary_tbl").find_all('div')

rows = []

for row in summary:
	row = row.get_text(",", strip=True).encode('utf-8')
	rows.append(row)

total = rows[:1]
#print ",".join(str(x) for x in total)





# print rows
# print ', '.join([str(ro) for ro in rows])



#net = record.find(class="paycheck")

#print net.get_text(",", strip=True)

#for td in net_td:
	#print td.get_text(",", strip=True)

# net = record.find(id="paystub_net_tbl")
#print(net, net_td)
# print(record.prettify())