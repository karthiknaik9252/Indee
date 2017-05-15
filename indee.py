from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCase(LiveServerTestCase):


    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('https://indee.tv/signup')

        # find the form element

        Email = selenium.find_element_by_Xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[1]/input')
        Password = selenium.find_element_by_Xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[3]/input')
        Confirm_password = selenium.find_element_by_Xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[5]/input')
        First_name = selenium.find_element_by_Xpath( '//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[7]/input')
        Last_name = selenium.find_element_by_Xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[9]/input')
        Company_name = selenium.find_element_by_Xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[11]/input')

        # check box and Submit button


        driver.find_element_by_Xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[12]/label').click()

        submit = selenium.find_element_by_Xpath('//*[@id="__nuxt"]/div[2]/div/div/div/div[1]/div[2]/form/div[13]/button')

    # Fill the form with data

        Email.send_keys('username"+ randomInt +"@gmail.com')
        Password.send_keys('Test@123')
        Confirm_password.send_keys('Test@123')
        First_name.send_keys('Ram')
        Last_name.send_keys('Raj')
        Company_name.send_keys('TestCompany')

    # submitting the form

        submit.send_keys(Keys.RETURN)

    # check the returned result

        assert 'WELCOME TO INDEE. LET’S GET STARTED!' in selenium.page_source