from selenium import webdriver
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
        homePage.shopItems().click()
        checkOutPage = CheckOutPage(self.driver)
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            #print(cardText)
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        checkOutPage.checkOutItems().click()

        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        log.info("Entering country name as ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is "+successText)
        assert "Success! Thank you!" in successText
