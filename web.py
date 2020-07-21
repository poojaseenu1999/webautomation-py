#importing selenium
from selenium import webdriver

#linking the driver installed to chrome
driver = webdriver.Chrome()
driver.get('https://youtube.com')
driver.get('https://www.youtube.com/results?search_query=study+monk')

#linking the xpath of the searchbar to studymonk page
# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('Study Monk')
#
# #action when clicked on search button
# searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchbutton.click()
