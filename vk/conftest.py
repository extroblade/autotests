import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browserName',\
                    action='store',\
                    default="chrome",\
                    help="Choose browser: chrome or firefox")
    parser.addoption('--language',\
                    action='store',\
                    default="ru",\
                    help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browserName = request.config.getoption("browserName")
    user_language = request.config.getoption("language")

    if browserName == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print("\n..start chrome browser for test..\n..")
        browser = webdriver.Chrome(options=options)

    elif browserName == "firefox": 
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\n..start firefox browser for test..\n..")
        browser = webdriver.Firefox(firefox_profile=fp)
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("..\n..quit browser..")
    browser.quit()