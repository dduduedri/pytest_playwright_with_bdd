from pageObjects.orderDetails import OrderDetailsPage


class OrderHistoryPage:

    def __init__(self,page):
        self.page = page


    def select_order_from_history(self,order_id):
        order_raw = self.page.locator("//tbody/tr").filter(has_text=order_id)
        order_raw.locator("//td/button[contains(text(), 'View')]").click()

    def select_order_from_history_and_details(self,order_id):
        self.select_order_from_history(order_id)
        order_details=OrderDetailsPage(self.page)
        return order_details
