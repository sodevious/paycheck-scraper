from bs4 import BeautifulSoup
import csv

# Open the HTML file
record = BeautifulSoup(open("src/Paycheck-2015-12-24.html"), "html.parser")

# Get paystub dates
date = record.find(id="paystub_form_tbl").td.get_text(strip=True).strip("Pay stub for period:").lstrip()

# Sample
salary = "Salary"
net = "Net Pay"
reimbursement = "Reimbursement"
deductions = "Deductions"
insurance = "Health Insurance"
taxes= "Taxes Paid"

# Write to CSV
f = csv.writer(open("data.csv", "w"))
f.writerow([date, salary, net, reimbursement, deductions, insurance, taxes])

print date, salary, net, reimbursement, deductions, insurance, taxes