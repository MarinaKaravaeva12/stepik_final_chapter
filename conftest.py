from selenium import webdriver
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.chrome.options import Options as OptionsChrome
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name',action = 'store', default='chrome',
                     help = "Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    parser.addoption('--language',action = 'store',default = 'en',
                     help = "Choose language: '--language=en' or '--language=ru'")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')

    options_chrome = OptionsChrome()
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print(f"Language set for browser: {user_language}")
    yield browser
    print("\nquit browser..")
    browser.quit()