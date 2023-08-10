import pytest
from selenium import webdriver
import time

driver = None
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--base_url", action="store", default="TEST"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    base_url = request.config.getoption("base_url")

    if base_url == "TEST":
        website_url = "https://rahulshettyacademy.com/angularpractice/"
    elif base_url == "UAT":
        website_url = "https://UATrahulshettyacademy.com/angularpractice/"
    elif base_url == "PROD":
        website_url = "https://PRODrahulshettyacademy.com/angularpractice/"
    else:
        raise ValueError("Invalid base_url argument. Please use TEST, UAT, or PROD.")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()
    else:
        raise ValueError("Invalid base_url argument. Please use chrome, firefox, or IE.")

    driver.get(website_url)
    request.cls.driver = driver
    yield
    driver.close()


# ... Rest of the script remains the same ...


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)