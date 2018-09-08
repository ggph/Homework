try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    import time
    import yagmail
    import os
except:
    print("You must install selenium, time, yagmail and os.")
#What email the homework will be sent to
send_to_email = ' '
#Your FieldSchool username
website_username = ' '
#Your FieldSchool password
website_password = ' '
#If the homework assignments should be deleted after the email is sent. (True = Yes, False = No)
remove_files = True
#EVRYTHING BELLOW, DO NOT EDIT!!!

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '62.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768'
}

driver = webdriver.Remote(
    command_executor='http://jakestrouse1:a8h4yFzxtqBHkyj1YxsS@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)


driver.get("https://fieldschool.myschoolapp.com/app/#login")
driver.set_page_load_timeout(10000)

name = driver.find_element_by_id('Username')
driver.set_page_load_timeout(10000)
submit = driver.find_element_by_id('nextBtn')
name.send_keys(website_username)
submit.click()
driver.set_page_load_timeout(10000)
password = driver.find_element_by_id('Password')
password.send_keys(website_password)
driver.set_page_load_timeout(10000)
login = driver.find_element_by_id('loginBtn')
login.click()



time.sleep(10)


driver.get("https://fieldschool.myschoolapp.com/app/student#academicclass/22606731/0/bulletinboard")
time.sleep(10)
assment = driver.find_element_by_id('assignments-link')
assment.click()
time.sleep(10)
driver.save_screenshot('Math.png')

driver.get("https://fieldschool.myschoolapp.com/app/student#academicclass/22606898/0/bulletinboard")
time.sleep(10)
assment = driver.find_element_by_id('assignments-link')
assment.click()
time.sleep(10)
driver.save_screenshot('Bio.png')

driver.get("https://fieldschool.myschoolapp.com/app/student#academicclass/22607085/0/bulletinboard")
time.sleep(10)
assment = driver.find_element_by_id('assignments-link')
assment.click()
time.sleep(10)
driver.save_screenshot('English.png')

driver.get("https://fieldschool.myschoolapp.com/app/student#academicclass/22606761/0/bulletinboard")
time.sleep(10)
assment = driver.find_element_by_id('assignments-link')
assment.click()
time.sleep(10)
driver.save_screenshot('History.png')

driver.get("https://fieldschool.myschoolapp.com/app/student#academicclass/22607144/0/bulletinboard")
time.sleep(10)
assment = driver.find_element_by_id('assignments-link')
assment.click()
time.sleep(10)
driver.save_screenshot('Spanish.png')


driver.quit()
yag = yagmail.SMTP('zipshop9', 'jakerocks')
contents = [
        "Homework from the fieldschool website has been taken",
"Bio.png","English.png","History.png","Math.png","Spanish.png"

    ]
yag.send(send_to_email, 'Homework Found!', contents)
if remove_files == True:
    os.remove('Bio.png')
    os.remove('English.png')
    os.remove('History.png')
    os.remove('Math.png')
    os.remove('Spanish.png')
