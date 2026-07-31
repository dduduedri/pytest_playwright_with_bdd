import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.api_base import APIUtils

scenarios('../features/orderTransaction.feature')


@given(parsers.parse('place the item order with {username} and {password}'),target_fixture='order_id')
def place_order(playwright : Playwright ,username, password) :
    user_credentials= {"userEmail": username, "UserPassword": password}

    api_util= APIUtils ()
    order_id = api_util.create_order(playwright,user_credentials)
    return order_id


@given('the user is on login page',target_fixture='login_page')
def login_user(context_setup):
    login_page = LoginPage(context_setup)
    return login_page

@when(parsers.parse('I login to portal with {username} and {password}'),target_fixture='dashboard_page')
def open_dashboard(login_page,username, password,):
    dashboard_page = login_page.login_and_dashboard(username,password)
    return dashboard_page

@when('navigate to orders page',target_fixture='order_history')
def navigate_to_orders_page(dashboard_page):
    order_history = dashboard_page.order_nav_link_to_history()
    return order_history

@when('select the orderId',target_fixture='order_details')
def select_order_id(order_history,order_id):
    order_details=order_history.select_order_from_history_and_details(order_id)
    return order_details

@then('order message is successfully displayed')
def order_message(order_details):
    order_details.verify_order_message()

