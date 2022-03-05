from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# This is a bill payment program for gas and power company for California

website = 'https://www.pge.com/'
s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
username = "username"
password = 'password'

# Opens the website
driver.get(website)
time.sleep(2)

def login():
    # User input
    userInput = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/main/div/div/div[1]/section[1]/div/div/div[1]/form/div/div/div[1]/input')
    # Clicks the account number input
    userInput.click()
    # Inputs the account number
    userInput.send_keys(username)
    time.sleep(1)

    # Password input
    passwordInput = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/main/div/div/div[1]/section[1]/div/div/div[1]/form/div/div/div[2]/input')
    passwordInput.click()
    passwordInput.send_keys(password)
    time.sleep(1)

    # Clicks log in button
    loginButton = driver.find_element(By.ID, 'home_login_submit')
    loginButton.click()
    time.sleep(3)

def creditCardInput():
    name = 'name'
    email = 'email'
    ccNum = 'credit card number'
    cvv = 'credit card cvv'
    zipC = 'zipcode'

    # Credit card input
    cardN = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[2]/li[6]/div[1]/input')
    cardN.click()
    cardN.send_keys(ccNum)
    time.sleep(1)

    # Name input
    nameInput = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[2]/li[7]/table/tbody/tr[1]/td[2]/div/input')
    nameInput.click()
    nameInput.send_keys(name)
    time.sleep(1)

    # Email input
    emailInput = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[2]/li[8]/div[1]/input')
    emailInput.click()
    emailInput.send_keys(email)
    time.sleep(1)

    # Next btn
    nextBtn = driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[3]/li/div/table/tbody/tr/td[2]/a')
    driver.execute_script("arguments[0].click();", nextBtn)
    time.sleep(1)

    # Cvv input
    cvvInput = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[2]/li[8]/div[2]/input')
    cvvInput.click()
    cvvInput.send_keys(cvv)
    time.sleep(1)

    # Exp month input
    expMonInput = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[2]/li[9]/table/tbody/tr/td[1]/label/div/div/select')
    expMonInput.click()
    expMonInput.send_keys(Keys.ARROW_DOWN * 2, Keys.ENTER)
    time.sleep(1)

    # Exp year input
    expYearInput = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[2]/li[9]/table/tbody/tr/td[3]/label/div/div/select')
    expYearInput.click()
    expYearInput.send_keys(Keys.ARROW_DOWN * 1, Keys.ENTER)
    time.sleep(1)

    # Billing zipcode input
    billingZ = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[2]/li[10]/div[1]/input')
    # driver.execute_script("arguments[0].click();", billingZ)
    billingZ.click()
    billingZ.send_keys(zipC, Keys.TAB * 2)
    time.sleep(1)

    # Next payment button
    nextPaymentButton = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/form/div[4]/div[2]/div[2]/ul[3]/li/div/table/tbody/tr/td[2]/a')
    driver.execute_script("arguments[0].click();", nextPaymentButton)
    time.sleep(3)

    # Payment button
    paymentButton = driver.find_element(By.ID,
                                        'ctl00_main_btnPay')
    driver.execute_script("arguments[0].click();", paymentButton)
    time.sleep(4)

    # Note
    paymentNote = driver.find_element(By.CLASS_NAME, 'confTitle')
    print(paymentNote)
    time.sleep(1)

    # Confirmation number
    confirmationNum = driver.find_element(By.ID, 'ctl00_main_lblConfirmCodeC')
    print(confirmationNum)
    time.sleep(10)
    driver.quit()

def makePayment():
    # Clicks make payment button
    makePaymentButton = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/button')
    driver.execute_script("arguments[0].click();", makePaymentButton)
    time.sleep(2)

    # Clicks Credit card button
    creditCardSelection = driver.find_element(By.ID,
                                              'utag-pay-credit-debit-button')
    driver.execute_script("arguments[0].click();", creditCardSelection)
    time.sleep(2)

    # Clicks next button to credit card page
    nextBtn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div/div[4]/div/div/div[3]/button[2]')
    driver.execute_script("arguments[0].click();", nextBtn)
    time.sleep(2)

    # Inputs credit card info
    creditCardInput()

def balanceCheck():
    # Gets amount
    time.sleep(8)
    amount = driver.find_element(By.ID, 'spntotalAmountDueUI')
    time.sleep(8)
    mainAmount = int(float(amount.text[1:]))
    print(mainAmount)

    # Checks if the amount is more than 0 will continue with payment process, else it will exit program
    if mainAmount > 0:
        makePayment()
    else:
        driver.quit()


login()
balanceCheck()
