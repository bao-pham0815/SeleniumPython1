import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


from TestData.HomePageData import HomePageData
from TestData.HomePageData2 import HomePageData2

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        # driver.find_element_by_name("name").send_keys("Rahul")
        #driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
        #driver.find_element_by_id("exampleCheck1").click()
        #driver.find_element_by_name("email").send_keys("Shetty")
        # select class provide the methods to handle the options in dropdown
        #dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        #dropdown.select_by_visible_text("Female")
        #sel.select_by_visible_text("Male")
        #dropdown.select_by_index(0)
        #driver.find_element_by_xpath("//input[@type='submit']").click()
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

        #alert = driver.find_element_by_class_name("alert-success").text
        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

#("Bao Pham", "baopham@udemy111.com", "Male"),("Tram Truong", "Truong.Tram@whateverkjd.com", "Female")
    @pytest.fixture(params=HomePageData2.getAllTestData2())
    #@pytest.fixture(params=HomePageData.getAllTestData("Testcase1")) # use this to run only single test case.
    def getData(self, request):
        return request.param


