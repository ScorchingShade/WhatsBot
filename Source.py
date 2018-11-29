from selenium import webdriver

driver= webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name=input("Enter User/Group: ")
msg=input("Message: ")
count=int(input("Message Count: "))

input("Scan the QR code and enter anything thereafter")

user=driver.find_element_by_xpath('//span[@title ="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button=driver.find_element_by_class_name('_35EW6')
    button.click()