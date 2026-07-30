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

# def param_id_name(user): without lambda
#     return user["userEmail"]

# @pytest.mark.parametrize('user_credentials_params',load_credentials(),ids=param_id_name) #ids its just give id name to the parameters - without lambda

@pytest.mark.full
@pytest.mark.parametrize('user_credentials_params',load_credentials(),ids=lambda user: user["userEmail"]) #ids its just give id name to the parameters
def test_e2e_api(playwright:Playwright ,context_setup,user_credentials_params) :

    user_email=user_credentials_params["userEmail"]
    user_password=user_credentials_params["UserPassword"]

    #from chromium_setup in conftest file
    # my_browser = playwright.chromium.launch(headless=False)
    # my_context = my_browser.new_context()
    # my_page = my_context.new_page()

    api_util= APIUtils ()
    #print(f"token :{api_util.get_token (playwright,user_credentials_params)}")
    order_id = api_util.create_order(playwright,user_credentials_params)
    #print(f"order_id :{order_id}")

    login_page=LoginPage(context_setup)
    #login_page.navigate() #in conftest

    dashboard_page = login_page.login_and_dashboard(user_email,user_password)
    order_history=dashboard_page.order_nav_link_to_history()
    order_details=order_history.select_order_from_history_and_details(order_id)
    order_details.verify_order_message()

    time.sleep(2)



