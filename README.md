# paycheck-scraper


I wrote a python script to scrape a folder of HTML files for my online [paycheck records](https://www.paycheckrecords.com), extract the right data I wanted, and then output the data into a CSV file. 

_Because #taxes_

**Disclaimer**: anything found in the `/sample` folder is **FAKE** data! It's there to show you that the script works.

---

### Working example
[a sample csv](https://github.com/sodevious/paycheck-scraper/blob/master/sample/sample_data.csv)


### To use the sample
	mkvirtualenv paycheck_scraper
	pip install -r requirements.txt
	python sample/sample.py