#coding:utf-8
from selenium import webdriver
import time,unittest,HTMLTestRunner,argparse
from pages.login_page import Login_page
global browser_type

class Login_case(unittest.TestCase):
	"""docstring for Login_case"""
	def setUp(self):
		# self.driver=webdriver.Chrome()
		# self.driver.implicitly_wait(8)


		#参数重构
		if browser_type == 1:
			self.driver=webdriver.Ie()

		elif browser_type == 2:
			self.driver=webdriver.Chrome()

		elif browser_type == 3:
			self.driver=webdriver.Firefox()

		self.driver.implicitly_wait(8)



	def test_login_success(self):
		username="gufan"
		pwd="Password@1"
		driver=self.driver


		# driver.get(url)
		# driver.find_element_by_id("user_login").send_keys(username)
		# driver.find_element_by_id("user_pass").send_keys(pwd)
		# driver.find_element_by_id("wp-submit").click()


		#第二步重构
		login_page=Login_page(self.driver)
		login_page.navigate()

		# login_page.login(username, pwd)
		# title=self.driver.title

		#第三步重构
		dashboard_page=login_page.login(username, pwd)
		title=dashboard_page.title()
		

		self.assertIn(u"UFO_team需求整理博客", title)

	def test_login_username_Null(self):
		username=""
		pwd="Password@1"
		driver=self.driver
		login_page=Login_page(self.driver)
		login_page.navigate()
		login_page.login(username, pwd)
		error=login_page.error_textfield.text
		self.assertIn(u"用户名一栏为空", error)



	def tearDown(self):
		self.driver.quit()



	# def by_css(self,css_selector):
	# 	return self.driver.find_element_by_css_selector(css_selector)
	# def by_id(self,the_id):
	# 	return self.driver.find_element_by_id(the_id)
	# def by_name(self,name):
	# 	return self.driver.find_element_by_name(name)
	# def by_xpath(self,xpath):
	# 	return self.driver.find_element_by_xpath(xpath)



if __name__ == '__main__':

	parser=argparse.ArgumentParser()
	parser.add_argument("browser",help="ie=1,chrome=2,firefox=3",type=int)
	args=parser.parse_args()
	type_id=args.browser
	browser_type=type_id
	print browser_type

	#1执行所有   入参了以后不能用unittest.main()方法
	# unittest.main()


	testsuite=unittest.TestSuite()


	#添加单独的测试用例
	# testsuite.addTest(Login_case("test_login_success"))


	#添加整个测试文件py
	try:
		testsuite.addTest(unittest.makeSuite(Login_case))
	
	


	#2调试
	# runner=unittest.TextTestRunner()
	# runner.run(testsuite)
	


	#使用HTMLTestRunner库生成测试报告
		filename="D:\\quarkscript\\wordpress_script\\report.html"
		fp=file(filename,'wb')
		runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="wordpress_report")
		runner.run(testsuite)
	except Exception, e:
		raise e

