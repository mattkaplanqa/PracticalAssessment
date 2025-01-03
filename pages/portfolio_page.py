from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PortfolioPage(BasePage):
    PORTFOLIO_VALUE = (By.XPATH, "//*[@class = 'text-ds-primary']")

    def get_portfolio_value(self):
        return self.get_text(self.PORTFOLIO_VALUE)
