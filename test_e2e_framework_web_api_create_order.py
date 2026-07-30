import json
import time

import pytest
from playwright.sync_api import Playwright, expect
from pageObjects.login import LoginPage
from utils.api_base import APIUtils

def load_credentials():
    with open('data/credentials.json') as json_file:
        test_data = json.load(json_file)
        print(test_data)
        user_list = test_data["user_credentials"]
    return user_list

@pytest.mark.smoke
def test_e2e_api_create_order_first_user(playwright:Playwright ,context_setup) :
    user_credential=load_credentials()[0]
    user_email=user_credential["userEmail"]
    user_password=user_credential["UserPassword"]

    #from chromium_setup in conftest file
    # my_browser = playwright.chromium.launch(headless=False)
    # my_context = my_browser.new_context()
    # my_page = my_context.new_page()

    api_util= APIUtils ()
    #print(f"token :{api_util.get_token (playwright,user_credential)}")
    order_id = api_util.create_order(playwright,user_credential)
    #print(f"order_id :{order_id}")

    login_page = LoginPage(context_setup)
    # login_page.navigate() #in conftest

    login_page.login_and_dashboard(user_email, user_password)

    time.sleep(2)

@pytest.mark.smoke
def test_e2e_api_create_order_sec_user(playwright:Playwright ,context_setup) :
    user_credential=load_credentials()[1]
    user_email=user_credential["userEmail"]
    user_password=user_credential["UserPassword"]

    #from chromium_setup in conftest file
    # my_browser = playwright.chromium.launch(headless=False)
    # my_context = my_browser.new_context()
    # my_page = my_context.new_page()

    api_util= APIUtils ()
    #print(f"token :{api_util.get_token (playwright,user_credential)}")
    order_id = api_util.create_order(playwright,user_credential)
    #print(f"order_id :{order_id}")

    login_page=LoginPage(context_setup)
    #login_page.navigate() #in conftest

    login_page.login_and_dashboard(user_email,user_password)

    time.sleep(2)



