from playwright.sync_api import Playwright


orders_payload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}

class APIUtils:
    def get_token (self, playwright: Playwright , user_cred):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        login_payload = {"userEmail": user_cred["userEmail"], "userPassword": user_cred["UserPassword"]}

        response = api_request_context.post("/api/ecom/auth/login",
                                        data=login_payload,
                                        headers={"Content-Type": "application/json"})
        assert response.ok, (
            f"Login failed for {user_cred['userEmail']} "
            f"(status {response.status}): {response.text()}"
        )
        response_body = response.json()
        return response_body["token"]

    def create_order(self,playwright:Playwright,user_cred):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=orders_payload,
                                 headers={"Authorization": self.get_token(playwright,user_cred),
                                          "Content-Type": "application/json"})
        return response.json()["orders"][0]