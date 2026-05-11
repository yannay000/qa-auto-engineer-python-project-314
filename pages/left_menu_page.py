from pages.base_page import BasePage
from pages.locators.left_menu_locators import LeftMenuLocators


class LeftMenuPage(BasePage):

	def open_users_page(self) -> None:
		self.click(LeftMenuLocators.USERS)