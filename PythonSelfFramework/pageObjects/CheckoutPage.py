from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    #driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)