from selenium import webdriver
# Running a test invoking a browser in background and
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        homePage.shopItems().click()
        checkOutPage = CheckOutPage(self.driver)

        log.info("getting all the card titles")

        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            #print(cardText)
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
                #self.driver.find_element_by_css_selector(".card-footer button")[i].click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkOutPage.checkOutItems().click()


        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        log.info("Entering country name as ind")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is "+successText)
        assert "Success! Thank you!" in successText