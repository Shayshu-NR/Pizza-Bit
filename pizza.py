from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

STREET_ADDRESS = '123 Fake St'
CITY = 'New York City'
POSTAL_CODE = 'ABC 123'
COUPON = 'coupon'
FIRST_NAME = 'Bob'
LAST_NAME = 'Jim'
EMAIL = 'throwaway@gmail.com'
PHONE = '1234567890'
CREDIT_CARD = '123456678123'
CC_MONTH = {'//*[@id="Expiration_Month"]/option[0]',
            '//*[@id="Expiration_Month"]/option[1]',
            '//*[@id="Expiration_Month"]/option[2]',
            '//*[@id="Expiration_Month"]/option[3]',
            '//*[@id="Expiration_Month"]/option[4]',
            '//*[@id="Expiration_Month"]/option[5]',
            '//*[@id="Expiration_Month"]/option[6]',
            '//*[@id="Expiration_Month"]/option[7]',
            '//*[@id="Expiration_Month"]/option[8]',
            '//*[@id="Expiration_Month"]/option[9]',
            '//*[@id="Expiration_Month"]/option[10]',
            '//*[@id="Expiration_Month"]/option[11]',
            '//*[@id="Expiration_Month"]/option[12]'}
CC_YEAR = { '//*[@id="Expiration_Year"]/option[0]',
            '//*[@id="Expiration_Year"]/option[1]',
            '//*[@id="Expiration_Year"]/option[2]',
            '//*[@id="Expiration_Year"]/option[3]',
            '//*[@id="Expiration_Year"]/option[4]',
            '//*[@id="Expiration_Year"]/option[5]',
            '//*[@id="Expiration_Year"]/option[6]',
            '//*[@id="Expiration_Year"]/option[7]',
            '//*[@id="Expiration_Year"]/option[8]',
            '//*[@id="Expiration_Year"]/option[9]',
            '//*[@id="Expiration_Year"]/option[10]',
            '//*[@id="Expiration_Year"]/option[11]',
            '//*[@id="Expiration_Year"]/option[12]',
            '//*[@id="Expiration_Year"]/option[13]',
            '//*[@id="Expiration_Year"]/option[14]',
            '//*[@id="Expiration_Year"]/option[15]',
            '//*[@id="Expiration_Year"]/option[16]',}
exp_month = int(input("Credit card month experation: "))
exp_year = int(input("Credit card year experation: ")) - 2019

CC_SECURITY_CODE = '123'

class pizzaBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/bin/chromedriver.exe')
    
    def select_store(self):
        #load webpage
        self.driver.get('https://www.dominos.ca/')
        sleep(3)

        #click delivery
        self.driver.find_element_by_xpath('//*[@id="homeWrapper"]/main/section[1]/div/div[2]/a[1]').click()

        sleep(10)

        #enter street address
        self.driver.find_element_by_xpath('//*[@id="Street"]').send_keys(STREET_ADDRESS)

        #enter city
        self.driver.find_element_by_xpath('//*[@id="City"]').send_keys(CITY)

        #choose city
        self.driver.find_element_by_xpath('//*[@id="Region"]/option[10]').click()

        #enter postal code
        self.driver.find_element_by_xpath('//*[@id="Postal_Code"]').send_keys(POSTAL_CODE)

        #search locations
        self.driver.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[3]/button').click()
        sleep(3)

    def make_pizza(self):
        #select thin crust
        self.driver.find_element_by_xpath('//*[@id="entreesPage"]/div[2]/div[6]/ul/li[3]/a').click()     
        sleep(1)

        #select medium
        self.driver.find_element_by_xpath('//*[@id="SizeCrustWrapper"]/div[4]/div/div[2]/label/span[1]').click()

        #cheese and toppings
        self.driver.find_element_by_xpath('//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button').click()
        sleep(0.5)

        #no extra cheese pls
        self.driver.find_element_by_xpath('//*[@id="stepUpsell"]/div/button[1]').click()
        sleep(0.5)

        #vegetables
        self.driver.find_element_by_xpath('//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[5]').click() 
        self.driver.find_element_by_xpath('//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[8]').click() 
        self.driver.find_element_by_xpath('//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[3]').click() 
        self.driver.find_element_by_xpath('//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[4]').click() 

        #add to order
        self.driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button').click()

    def pay(self):
        #checkout
        self.driver.find_element_by_xpath('//*[@id="js-myOrderPage"]/a/span').click()
        sleep(1)

        #I DON"T WANT PARMESAN BITES FOR $3.49
        self.driver.find_element_by_xpath('//*[@id="genericOverlay"]/section/header/button').click() 
        sleep(2)

        #enter coupon
        #self.driver.find_element_by_xpath('//*[@id="Coupon_Code_Cart"]').send_keys(COUPON)
        #self.driver.find_element_by_xpath('//*[@id="js-checkoutColumns"]/div/div/div[2]/div[1]/div[7]/form/div/div[2]/button').click()
        
        #continue checkout
        self.driver.find_element_by_xpath('//*[@id="js-checkoutColumns"]/aside/div[3]/a').click()
        sleep(3)

        #your information
        self.driver.find_element_by_xpath('//*[@id="First_Name"]').send_keys(FIRST_NAME)
        self.driver.find_element_by_xpath('//*[@id="Last_Name"]').send_keys(LAST_NAME)
        self.driver.find_element_by_xpath('//*[@id="Email"]').send_keys(EMAIL)
        self.driver.find_element_by_xpath('//*[@id="Callback_Phone"]').send_keys(PHONE)

        #select credit card
        self.driver.find_element_by_xpath('//*[@id="orderPaymentPage"]/form/div[4]/div/div[2]/div[2]/div[5]/label/input').click()
        self.driver.find_element_by_xpath('//*[@id="Credit_Card_Number"]').send_keys(CREDIT_CARD)


        self.driver.find_element_by_xpath(CC_MONTH[exp_month]).click()
        self.driver.find_element_by_xpath(CC_YEAR[exp_year]).click()
        self.driver.find_element_by_xpath('//*[@id="Credit_Card_Security_Code"]').send_keys(CC_SECURITY_CODE)
        self.driver.find_element_by_xpath('//*[@id="Billing_Postal_Code"]').send_keys(POSTAL_CODE) 
        self.driver.find_element_by_xpath('//*[@id="orderPaymentPage"]/form/div[5]/div/div[4]/button').click()
        


order_bot = pizzaBot()
order_bot.select_store()
order_bot.make_pizza()
order_bot.pay()        
        
        







        
        
        
        










