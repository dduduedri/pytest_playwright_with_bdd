import json
import os

import pytest
from playwright.sync_api import Browser, Page, Playwright



#Not in use - there is better way to use the credential as data - its relevant for test_framework_api_cred_by_fixture_NOT_USE.py - the Udemy course solution
# @pytest.fixture(scope="session") #run for one execution
# def user_credential_fxtr(request): #request - pytest global variable
#     return request.param




with open('data/execution_data.json') as _execution_data_file:
    execution_data = json.load(_execution_data_file)



# --browser_name and --url → your custom options, so you must register them in your pytest_addoption.
# --tracing, --headed, --browser, --output, --video, --screenshot → provided by pytest-playwright, so you just read them; don't register them.
def pytest_addoption(parser): #get the input from command line and if not exist use the execution_data.json
    parser.addoption(
        "--browser_name", action="store", default=execution_data["browser"], help="my option: chrome or firefox"
    )
    parser.addoption(
        "--url", action="store", default=execution_data["application_url"], help="application url"
    )


#every parameterized test gets a new browser and new context and page.
#in case scope="session" the test will failed because its running in 2 iteration ( different users ) fo on the sec time the chromium_setup will not run
#Tracing (tracing_on) solution - since we are make page based on cntext we are creating and not using the platwrigh Page object we need to use the context.tracing.start and context.tracing.stop
# @pytest.fixture(scope="function")
# def context_setup (playwright:Playwright,request):
#     browser = playwright.chromium.launch(headless=False)
#     browser_name=request.config.getoption("--browser_name")  #get the arg from the command line : pytest -s test_e2e_framework_web_api.py --headed --browser_name firefox
#     if browser_name=="chrome":
#         browser = playwright.chromium.launch(headless=False)
#     elif browser_name=="firefox":
#         browser = playwright.firefox.launch(headless=False)

#     tracing_on = request.config.getoption("--tracing") in ("on", "retain-on-failure")

#     url = request.config.getoption("--url")
#     context = browser.new_context()
    
#     if tracing_on:
#         context.tracing.start(screenshots=True, snapshots=True, sources=True)

#     my_page = context.new_page()
#     my_page.goto(url)
#     yield my_page

#     if tracing_on:
#         trace_path = os.path.join("test-results", request.node.name, "trace.zip")
#         print(f"trace_path :{trace_path}")
#         context.tracing.stop(path=trace_path)

#     context.close()
#     browser.close()


#A more efficient structure reuses the browser but creates a fresh context per test:
@pytest.fixture(scope="session")
def browser_setup(playwright: Playwright,request): # request gives access to global variables
    browser = playwright.chromium.launch(headless=False)

    browser_name=request.config.getoption("--browser_name")  #get the arg from the command line : pytest -s test_e2e_framework_web_api.py --headed --browser_name firefox
    if browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name=="firefox":
        browser = playwright.firefox.launch(headless=False)

    yield browser

    browser.close()


#new context for each test
#Tracing (tracing_on) solution - since we are make page based on cntext we are creating and not using the platwrigh Page object we need to use the context.tracing.start and context.tracing.stop
@pytest.fixture(scope="function")
def context_setup(browser_setup: Browser,request) :

    tracing_on = request.config.getoption("--tracing") in ("on", "retain-on-failure")
    url = request.config.getoption("--url")
    context = browser_setup.new_context()
    
    if tracing_on:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto(url)
    yield page

    if tracing_on:
        trace_path = os.path.join("test-results", request.node.name, "trace.zip")
        print(f"trace_path :{trace_path}")
        context.tracing.stop(path=trace_path)

    context.close()
