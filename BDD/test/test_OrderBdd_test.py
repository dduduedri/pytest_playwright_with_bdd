import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.api_base import APIUtils

scenarios('../features/orderTransaction.feature')

@pytest.fixture
def shared_data ():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_order(playwright : Playwright ,username, password,shared_data) :
    user_credentials= {"userEmail": username, "UserPassword": password}

    api_util= APIUtils ()
    order_id = api_util.create_order(playwright,user_credentials)
    shared_data['order_id'] = order_id

@given('the user is on login page')
def login_user(context_setup,shared_data):
    login_page = LoginPage(context_setup)
    shared_data['login_page'] = login_page

@when(parsers.parse('I login to portal with {username} and {password}'))
def open_dashboard(shared_data,username, password,):
    login_page= shared_data['login_page']
    dashboard_page = login_page.login_and_dashboard(username,password)
    shared_data['dashboard_page'] = dashboard_page

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    order_history = shared_data['dashboard_page'].order_nav_link_to_history()
    shared_data['order_history'] = order_history

@when('select the orderId')
def select_order_id(shared_data):
    order_details=shared_data['order_history'].select_order_from_history_and_details(shared_data['order_id'])
    shared_data['order_details'] = order_details

@then('order message is successfully displayed')
def order_message(shared_data):
    shared_data['order_details'].verify_order_message()

