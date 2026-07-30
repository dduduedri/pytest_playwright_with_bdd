from playwright.sync_api import Page

from pageObjects.dashboard import DashboardPage


class LoginPage:

    def __init__(self,my_page):
        self.page=my_page

    # def navigate(self):
    #     self.page.goto("http://rahulshettyacademy.com/client") #In conftest

    def login(self,user_email,user_password):
        self.page.locator("#userEmail").fill(user_email)
        self.page.locator("#userPassword").fill(user_password)
        self.page.locator("#login").click()

    def login_and_dashboard(self,user_email,user_password):
        self.login(user_email,user_password)
        dashboard_page = DashboardPage(self.page)
        return dashboard_page
