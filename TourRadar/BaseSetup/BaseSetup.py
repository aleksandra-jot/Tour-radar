import unittest
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from TourRadar.BaseSetup.ServerUrl import ServerName


@pytest.mark.usefixtures("web_driver")
class Base(unittest.TestCase):

    @pytest.fixture(scope="class")
    def web_driver(self, request):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(ServerName.start_url)
        request.cls.driver = driver
        yield
        driver.close()





