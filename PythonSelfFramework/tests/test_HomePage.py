#developer branch testing

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


from TestData.HomePageData import HomePageData
from TestData.HomePageData2 import HomePageData2

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        log = self.getLogger()
        homepage = HomePage (self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        log.info("email is " + getData["email"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckBox().click()
        log.info("gender is " + getData["gender"])
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData2.getAllTestData2())
    #@pytest.fixture(params=HomePageData.getAllTestData("Testcase1")) # use this to run only single test case.
    def getData(self, request):
        return request.param


