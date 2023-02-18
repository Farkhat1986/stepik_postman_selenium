import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language !=  None:
        print("\nstart selected RU for test..")
        browser = webdriver.Chrome(options=options)
    else:
        print(language)
        raise pytest.UsageError("--language should be en, fr, es or ru")
    yield browser
    print("\nquit browser..")
    browser.quit()