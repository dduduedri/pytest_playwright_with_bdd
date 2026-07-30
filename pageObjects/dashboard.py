from pageObjects.orderHistory import OrderHistoryPage


class DashboardPage:

     def __init__(self, my_page):
          self.page = my_page

     def select_order_nav_link(self):
          self.page.get_by_role("button", name="ORDERS").click()

     def order_nav_link_to_history(self):
          self.select_order_nav_link()
          order_history_page=OrderHistoryPage(self.page)
          return order_history_page
