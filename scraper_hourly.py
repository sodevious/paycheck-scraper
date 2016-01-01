import csv, glob, os, time
from bs4 import BeautifulSoup

# Directory of html files
input_dir = "src/html/"

# Create the CSV and header row
f = csv.writer(open("src/paycheck_data.csv", "w"))
f.writerow(["Date", "Total Pay", "Net Pay", "Hours", "Rate", "Deductions"])

# Write to CSV
for file_name in glob.glob(input_dir+ "*.html"):

	# Open the HTML files
    with open(file_name) as fp:
        record = BeautifulSoup(fp, "html.parser")

	# Get paystub dates
	date = record.find(id="paystub_form_tbl").td.get_text(strip=True).strip("Pay stub for period:").lstrip()

	# Get the relevant sections
	summary_table = record.find(id="paystub_summary_tbl").find_all('div')
	pay_table = record.find(id="paystub_pay_tbl").find_all('div')
	net_table = record.find(id="paystub_net_tbl").find_all('td')

	# Create lists
	summaries = []
	pay_rows = []
	net_rows = []

	# Clean data
	for item in summary_table:
		item = item.get_text("", strip=True).encode('utf-8')
		summaries.append(item)

	for item in pay_table:
		item = item.get_text(",", strip=True).encode('utf-8')
		pay_rows.append(item)

	for item in net_table:
		item = item.get_text(",", strip=True).encode('utf-8')
		net_rows.append(item)

	# Create items from cleaned arrays
	total = summaries[0]
	deductions = summaries[2]
	taxes = summaries[4]	
	hours = pay_rows[4]
	rate = pay_rows[5]
	net = net_rows[1]

	f.writerow([date, total, net, hours, rate, deductions])

	print date, total, deductions, taxes, net, hours, rate

# Add timestamp
generated = time.strftime("%I:%M:%S, %d/%m/%Y")

f.writerow(["Generated:", generated, " ", " ", " ", " "])
