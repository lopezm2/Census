from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

def getData():
	options = webdriver.ChromeOptions() 
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\elopez\Documents\chromedriver.exe')
	time.sleep(30)
	driver.get('https://usatrade.census.gov/data/Perspective60/View/dispview.aspx')
	time.sleep(3)
	element=driver.find_element_by_name("struserid")
	element.send_keys("8YRN87M")
	element = driver.find_element_by_name("pwdfld")
	element.send_keys("Newtradedata1!")
	element = driver.find_element_by_name("submit")
	element.click()
	time.sleep(3)
	element = driver.find_element_by_xpath('//a[@href="javascript:OnLoadFirstDimension(6541)"]') #13307 for imports
	element.click()
	time.sleep(3)
	l=driver.find_element_by_xpath("//a[@title='Select members of Measures']")
	l.click()
	time.sleep(3)
	l=driver.find_elements_by_xpath("//input[@type='checkbox']")
	for checkbox in l:
		checkbox.click()
	l=driver.find_element_by_xpath("//a[@title='Select members of Country']")
	l.click()
	time.sleep(3)
	l=driver.find_element_by_xpath("//input[@alt='Select group and all members below it in hierarchy']")
	l.click()
	l=driver.find_element_by_xpath("//a[@title='Select members of Time - time series hierarchy']")
	l.click()
	time.sleep(7000)
	
	
	
	x=10
	while x > 5:
		if x==10:
			years=driver.find_elements_by_xpath("//input[@alt='Select group and all members below it in hierarchy']")
			years[x].click()
			time.sleep(5)
			x=x-1
		else:
			clearYear = driver.find_elements_by_xpath("//input[@alt='Clear group and all members below it in hierarchy']")
			clearYear[x+1].click()
			time.sleep(5)
			years=driver.find_elements_by_xpath("//input[@alt='Select group and all members below it in hierarchy']")
			years[x].click()
			time.sleep(5)
			x=x-1
		c=44 #starts at commodity c+1
		while c>-1:
			if c==98:
				time.sleep(2)
				l=driver.find_element_by_xpath("//a[@title='Select members of Commodity']")
				l.click()
				time.sleep(3)
				commodities = driver.find_elements_by_xpath("//input[@alt='Select group and all members below it in hierarchy']")
				time.sleep(3)
				commodities[c].click()
				time.sleep(3)
				c=c-1
				l=driver.find_element_by_xpath("//a[@title='Select members of State']")
				l.click()
				states=driver.find_elements_by_xpath("//input[@type='checkbox']")
				time.sleep(2)
				i=3
			else:
				time.sleep(2)
				l=driver.find_element_by_xpath("//a[@title='Select members of Commodity']")
				l.click()
				time.sleep(3)
				commodities = driver.find_elements_by_xpath("//input[@alt='Select group and all members below it in hierarchy']")
				clearComm = driver.find_elements_by_xpath("//input[@alt='Clear group and all members below it in hierarchy']")
				clearComm[c+1].click()
				time.sleep(3)
				commodities = driver.find_elements_by_xpath("//input[@alt='Select group and all members below it in hierarchy']")
				clearComm = driver.find_elements_by_xpath("//input[@alt='Clear group and all members below it in hierarchy']")
				time.sleep(3)
				commodities[c].click()
				time.sleep(3)
				c=c-1
				l=driver.find_element_by_xpath("//a[@title='Select members of State']")
				l.click()
				states=driver.find_elements_by_xpath("//input[@type='checkbox']")
				time.sleep(2)
				i=3
				
			while i<57: #i<57 for real run
				try:
					states[i].click() #gets every states with fixed year and fixed commodity
					time.sleep(2)
				except:
					
					l=driver.find_element_by_xpath("//a[@title='Select members of Measures']")
					l.click()
					time.sleep(3)
					l=driver.find_element_by_xpath("//a[@title='Select members of State']")
					l.click()
					time.sleep(3)
					states=driver.find_elements_by_xpath("//input[@type='checkbox']")
					
					states[i].click() #gets every states with fixed year and fixed commodity
					time.sleep(2)
				try:
					l=driver.find_element_by_xpath("//a[@href='javascript:ShowUpdatedReportAfterSelection();']")
					time.sleep(2)
					l.click()
					time.sleep(5)
					l=driver.find_element_by_xpath("//img[@alt='Download report data']")
					l.click()
					time.sleep(5)
				except:
					time.sleep(10)
					print('there was an error. trying again.')
					
					l=driver.find_element_by_xpath("//a[@title='Select members of Measures']")
					l.click()
					time.sleep(3)
					l=driver.find_element_by_xpath("//a[@title='Select members of State']")
					l.click()
					time.sleep(3)
					l=driver.find_element_by_xpath("//a[@href='javascript:ShowUpdatedReportAfterSelection();']")
					time.sleep(2)
					l.click()
					time.sleep(5)
					l=driver.find_element_by_xpath("//img[@alt='Download report data']")
					l.click()
					time.sleep(5)
				
				
				l=driver.find_element_by_xpath("//select[@name='Download']/option[text()='Comma-delimited ASCII format (*.csv)']").click()
				time.sleep(1)
				l=driver.find_element_by_xpath("//select[@id='DataFormatCsv']/option[text()='List format']").click()
				time.sleep(2)
				l=driver.find_element_by_xpath("//input[@name='DownloadReportGo']")
				l.click()
				try:
					l=driver.switch_to.alert.accept()
					print('commodity ',c+2,' was skipped at state' ,i-2,' on to the next one')
					states[xs].click()
					i=60
				except:
					time.sleep(10)
					l=driver.find_element_by_xpath("//a[@title='Select members of State']")
					time.sleep(2)
					l.click()
					time.sleep(5)
					states=driver.find_elements_by_xpath("//input[@type='checkbox']")
					states[i].click()
					time.sleep(5)
					i+=1
	print('process finished')		
	
	
	
	time.sleep(3)
	driver.close()
	
def main():
		getData()
main()