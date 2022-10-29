import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




def pytest_addoption(parser):
    parser.addoption('--browserName', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browserName = request.config.getoption("browserName")
    browser = None

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'user_language'})

    if browserName == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browserName == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
