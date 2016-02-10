import csv, glob, os, time, datetime
from bs4 import BeautifulSoup

# Directory of html files
input_dir = "src/html_salary/"
generated = time.strftime("%I:%M:%S, %d/%m/%Y")
timestamp = datetime.datetime.now()

# Create the CSV and header row
f = csv.writer(open("src/paycheck_salary_%s.csv" % timestamp, "w"))
f.writerow(["Date", "Total Pay", "Net Pay", "Deductions", "Generated"])

# Write to CSV
for file_name in glob.glob(input_dir+ "*.html"):

	# Open the HTML files
    with open(file_name) as fp:
        record = BeautifulSoup(fp, "html.parser")

	# Get paystub dates
	date = record.find(id="paystub_form_tbl").td.get_text(strip=True).strip("Pay stub for period:").lstrip()

	# Get the relevant sections
	summary_table = record.find(id="paystub_summary_tbl").find_all('div')
	net_table = record.find(id="paystub_net_tbl").find_all('td')
	tax_table = record.find(id="paystub_ee_taxes_tbl").find_all('td')

	# Create lists
	summaries = []
	net_rows = []
	tax_rows = []

	# Clean data
	for item in summary_table:
		item = item.get_text("", strip=True).encode('utf-8')
		summaries.append(item)

	for item in net_table:
		item = item.get_text(",", strip=True).encode('utf-8')
		net_rows.append(item)

	for item in tax_table:
		item = item.get_text(",", strip=True).encode('utf-8')
		tax_rows.append(item)

	# Create items from cleaned arrays
	total = summaries[0]
	deductions = summaries[2]
	taxes_total = summaries[4]	
	federal_taxes = tax_rows[1]
	social_security = tax_rows[4]
	medicare = tax_rows[7]
	state_tax = tax_rows[10]
	city_tax = tax_rows[13]
	net = net_rows[1]

	f.writerow([date, total, net, taxes_total, federal_taxes, social_security, medicare, state_tax, city_tax, deductions, generated])

	print date, total, net, taxes_total, federal_taxes, social_security, medicare, state_tax, city_tax, deductions, generated
