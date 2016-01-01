from bs4 import BeautifulSoup
import csv

# Open the HTML file
record = BeautifulSoup(open("src/Paycheck-2015-12-24.html"), "html.parser")

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

# Write to CSV
f = csv.writer(open("src/paycheck_data.csv", "w"))
f.writerow(["Date", "Total Pay", "Net Pay", "Hours", "Rate", "Deductions"]) # Write column headers as the first line
f.writerow([date, total, net, hours, rate, deductions])

print date, total, deductions, taxes, net, hours, rate
