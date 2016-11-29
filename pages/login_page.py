from pages.base_page import BasePage
from pages.dashboard_page import DashBoard_Page

class Login_page(BasePage):
	"""docstring for LoginPage"""

	url="http://172.29.20.57/wordpress/wp-admin/"

	@property
	def username_textfield(self):
		return self.by_id("user_login")

	@property
	def pwd_textfield(self):
		return self.by_id("user_pass")

	@property
	def login_btn(self):
		return self.by_id("wp-submit")


	@property
	def error_textfield(self):
		return self.by_css("#login_error")


	def login(self,username,pwd):
		self.username_textfield.send_keys(username)
		self.pwd_textfield.send_keys(pwd)
		self.login_btn.click()
		return DashBoard_Page(self.driver)



