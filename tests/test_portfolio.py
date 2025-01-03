import os
from dotenv import load_dotenv
from selenium import webdriver
from pages.login_page import LoginPage
from pages.portfolio_page import PortfolioPage
from utils.email_utils import get_verification_email, click_verification_link
load_dotenv()

def test_portfolio_value():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    url      = os.getenv("DOMAIN")

    driver = webdriver.Chrome()
    driver.get(url)

    login_page = LoginPage(driver)
    login_page.login(username, password)




    portfolio_page = PortfolioPage(driver)
    portfolio_value = portfolio_page.get_portfolio_value()
    print(portfolio_value)
    assert portfolio_value == "0.00"

    driver.quit()
