import urllib2, urllib
from bs4 import BeautifulSoup
import re, csv, os.path
from datetime import datetime

#Load the existing csv data, if it exists
def loadSchools():
	#declare a few variables
	values_in_page = []
	schools_in_page = []
	file_path = '/Users/mtdukes/Documents/development/clervoyance/source/schools.csv'
	clery_url = 'https://studentaid.ed.gov/sa/about/data-center/school/clery-act'

	#check if a database exists
	if not os.path.isfile(file_path):
		school_writer = csv.writer(open(file_path,'wb'))
		school_writer.writerow(['dl_time', 'anchor_value', 'school', 'subhead', 'file_name','file_url'])
		print 'ALERT: New database created...'
	else:
		#read in values of existing spreadsheet and store them in an array
		school_reader = csv.reader(open(file_path,'rU'),delimiter=',')
		for row in school_reader:
			values_in_page.append(row[1])
			schools_in_page.append(row[2])
		#if log.csv exists, alert user that future entries will append onto existing file
		school_writer = csv.writer(open(file_path,'a'))
		print 'ALERT: database exists, appending...'

	#Read in the DOE Clery act page
	try:
		response = urllib2.urlopen(clery_url)
		html = response.read()
		print 'ALERT: Page successfully opened'
	except:
		print 'ERROR: invalid feed url'
		return

	soup = BeautifulSoup(html)

	#Load schools listed in the <select> tag with id="schoolDD" and a value
	for select in soup.find('select',id=re.compile('schoolDD')):
		if select.get('value'):
			#If the school doesn't exist in the database, add it
			if select.get('value') not in values_in_page:
				school_writer.writerow([str(datetime.now()),select.get('value'),select.get_text()])
				values_in_page.append(select.get('value'))
				schools_in_page.append(select.get_text())

	#loop through all the file locations and download each file to a directory
	#for value in values_in_page:
	##NOTE: Take a closer look at the hidden divs with id=school. They've got a mistake in their code that messes the divs up, but this may be a better way to navigate through the files


###TODO###
#If the school doesn't already exist in the database, navigate to the page and# download all new reports

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