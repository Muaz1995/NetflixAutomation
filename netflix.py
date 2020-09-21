from selenium import webdriver
import sys

driver = webdriver.Chrome(executable_path= r'C:\Users\USER\Desktop\Website login/chromedriver.exe')

def watch(url):
    driver.get(url)
    driver.find_element_by_name('userLoginId').send_keys("YourNetflixEmail")
    driver.find_element_by_name('password').send_keys("YourNetflixPassword")
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
    driver.find_element_by_class_name('profile-name').click()


watch('https://www.netflix.com/browse')