import config
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


login_url = 'https://manybooks.net/mnybks-login-form'
url = 'https://manybooks.net'
timeout = 3

driver = webdriver.Firefox(executable_path='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/geckodriver')
driver.get(login_url)
try:
    element_present = EC.presence_of_element_located((By.ID, 'edit-submit'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

email = driver.find_element_by_id("edit-email")
password = driver.find_element_by_id("edit-pass")
button = driver.find_element_by_id("edit-submit")

print(email, password, button)
email.send_keys(config.USERNAME)
password.send_keys(config.PASSWORD)
button.click()

time.sleep(4)

driver.get(url)
try:
    element_present = EC.presence_of_element_located((By.ID, 'edit-submit'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

for index in range(2):
	books_page = f"https://manybooks.net/search-book?language=All&field_genre[10]=10&field_genre[52]=52&field_genre[68]=68&field_genre[13]=13&field_genre[32]=32&field_genre[69]=69&field_genre[71]=71&field_genre[15]=15&field_genre[48]=48&field_genre[45]=45&field_genre[64]=64&field_genre[54]=54&field_genre[16]=16&field_genre[29]=29&field_genre[57]=57&field_genre[44]=44&field_genre[67]=67&field_genre[17]=17&field_genre[30]=30&field_genre[59]=59&field_genre[72]=72&field_genre[60]=60&field_genre[55]=55&field_genre[56]=56&field_genre[11]=11&field_genre[58]=58&field_genre[12]=12&field_genre[18]=18&field_genre[28]=28&field_genre[61]=61&field_genre[46]=46&field_genre[40]=40&field_genre[19]=19&field_genre[43]=43&field_genre[47]=47&field_genre[37]=37&field_genre[34]=34&field_genre[70]=70&field_genre[39]=39&field_genre[20]=20&field_genre[62]=62&field_genre[21]=21&field_genre[22]=22&field_genre[53]=53&field_genre[51]=51&field_genre[35]=35&field_genre[49]=49&field_genre[23]=23&field_genre[24]=24&field_genre[38]=38&field_genre[31]=31&field_genre[25]=25&field_genre[26]=26&field_genre[41]=41&field_genre[65]=65&field_genre[33]=33&field_genre[66]=66&field_genre[42]=42&field_genre[27]=27&field_genre[36]=36&field_genre[50]=50&field_genre[14]=14&search=&sticky=All&created_op=%3C&created[value]=0&created[min]=&created[max]=&author_uid_op=%3E%3D&author_uid[value]=0&author_uid[min]=&author_uid[max]=&sort_by=field_downloads&page={index}"
	driver.get(books_page)
	try:
		element_present = EC.presence_of_element_located((By.ID, 'edit-submit'))
		WebDriverWait(driver, timeout).until(element_present)
	except TimeoutException:
		print("Timed out waiting for page to load")
	finally:
		print(f"Page loaded - {index}")
	articles = driver.find_elements_by_tag_name('article')
	for data in articles:
		try:
			url_data = data.get_attribute("about")
			print(url+url_data)
		except:
			pass
driver.close()
