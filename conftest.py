import pytest
from selenium import webdriver

LANGUAGES = ['ru', 'en', 'fr', 'es']


@pytest.fixture(scope='function')
def browser(request):

    options = None
    browser = None

    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options)

    else:
        raise ValueError("Неподдерживаемый браузер: {}".format(browser_name))

    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox', help="Выбор драйвера")
    parser.addoption('--language', action='store', default='en', help=f'Выбор языка из: {LANGUAGES}')