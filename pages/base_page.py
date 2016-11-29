#coding:utf-8
from selenium import webdriver

class BasePage(object):
	url=None
	driver=None

	"""docstring for BasePage"""
	def __init__(self, driver):
		self.driver=driver
		self.domain="http://172.29.20.19/wordpress/wp-admin/"

	def title(self):
		return self.driver.title

	def url(self):
		return self.driver.url

	def navigate(self):
		return self.driver.get(self.url)

	def by_css(self,css_selector):
		return self.driver.find_element_by_css_selector(css_selector)
	def by_id(self,the_id):
		return self.driver.find_element_by_id(the_id)
	def by_name(self,name):
		return self.driver.find_element_by_name(name)
	def by_xpath(self,xpath):
		return self.driver.find_element_by_xpath(xpath)