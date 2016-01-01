from bs4 import BeautifulSoup
import csv, glob, os

# Directory of html files
input_dir = "/Users/nicoledominguez/sites/paycheck-scraper/src/html/"

# Create the CSV and header row
f = csv.writer(open("src/paycheck_data.csv", "w"))
f.writerow(["Date", "Total Pay", "Net Pay", "Hours", "Rate", "Deductions"]) # Write column headers as the first line

# Write to CSV
for file_name in glob.glob(input_dir+ "*.html"):

	# Open the HTML files
    with open(file_name) as fp:
        record = BeautifulSoup(fp, "html.parser")

	# Get paystub dates
	date = record.find(id="paystub_form_tbl").td.get_text(strip=True).strip("Pay stub for period:").lstrip()

	# Get the summary section
	summary_table = record.find(id="paystub_summary_tbl").find_all('div')

	# Create a list
	summaries = []

	# Clean data
	for item in summary_table:
		item = item.get_text("", strip=True).encode('utf-8')
		summaries.append(item)

	# Create items from cleaned array
	total = summaries[0]
	deductions = summaries[2]
	taxes = summaries[4]
	
	# Sample
	hours = "Hours"
	rate = "Rate"
	net = "net"

	f.writerow([date, total, net, hours, rate, deductions])

	print date, total, deductions, taxes, net, hours, rate