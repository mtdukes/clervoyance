import urllib2, urllib
from bs4 import BeautifulSoup
import csv, os.path

#Load the existing csv data, if it exists
def loadSchools():
	if not os.path.isfile('/Users/mtdukes/Documents/development/clervoyance/source/schools.csv'):
		school_writer = csv.writer(open('/Users/mtdukes/Documents/development/clervoyance/source/schools.csv','wb'))
		school_writer.writerow(['dl_time', 'school', 'subhead', 'file_name','file_url'])
		print 'ALERT: New database created...'
	#if log.csv exists, alert user that future entries will append onto existing file
	else:
		school_writer = csv.writer(open('/Users/mtdukes/Documents/development/clervoyance/source/schools.csv','a'))
		print 'ALERT: database exists, appending...'

	#Read in the DOE Clery act page
	try:
		response = urllib2.urlopen('https://studentaid.ed.gov/sa/about/data-center/school/clery-act')
		html = response.read()
		print 'ALERT: Page successfully opened'
	except:
		print 'ERROR: invalid feed url'
		return

	soup = BeautifulSoup(html)


#Load schools listed in the <select> tag with id="schoolDD"

#If the school doesn't already exist in the database, navigate to the page and download all new reports

#If the school exists in the database, navigate to the page and check if the reports listed match those in the database

#If the report does not exist in the database, download it

#Upload all new reports to the S3 bucket

#Update JSON file in S3 bucket describing reports in the database (JS/footables in the html will render as sortable table on page load)

#HOLD ONTO YOUR BUTTS
if __name__ == '__main__':
	print 'Welcome to Clervoyance!'

	loadSchools()

	print 'All done ...'

	print 'Thank you for using Clervoyance!'