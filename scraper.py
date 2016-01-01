from bs4 import BeautifulSoup
import csv

record = BeautifulSoup(open("src/Paycheck-2015-12-24.html"), "html.parser")

date = record.find(id="paystub_form_tbl")

print "Date: " + date.td.get_text(strip=True).strip("Pay stub for period:").lstrip()