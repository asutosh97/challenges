import unittest
from selenium import webdriver

class SimpleTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.PhantomJS()

	def test_heading(self):
		self.driver.get("http://pybites.pythonanywhere.com/")
		heading = self.driver.find_element_by_css_selector('h1').text
		self.assertIn(u'PyBites 100 Days of Django', heading)

	def test_navbar(self):
		self.driver.get("http://pybites.pythonanywhere.com/")
		nav = self.driver.find_elements_by_css_selector('#login a')
		self.assertEqual(u'Login', nav[0].text)
		self.assertEqual(u'Home', nav[1].text)

	def test_one(self):
		self.driver.get("http://pybites.pythonanywhere.com/")
		main = self.driver.find_element_by_css_selector('main ul li a')
		self.assertEqual(u'PyPlanet Article Sharer App', main.text)

	def test_two(self):
		self.driver.get("http://pybites.pythonanywhere.com/")
		self.driver.find_element_by_css_selector('main ul li a').click()
		self.assertEqual("http://pybites.pythonanywhere.com/pyplanet/", self.driver.current_url)
		table_heading = self.driver.find_element_by_css_selector('th').text
	 	self.assertEqual(u'Title', table_heading)
	 	table_rows = self.driver.find_elements_by_css_selector('tr')
	 	self.assertEqual(101, len(table_rows))

	def test_three(self):
	 	self.driver.get("http://pybites.pythonanywhere.com/")
		self.driver.find_element_by_css_selector('main ul li a').click()
		link_text = self.driver.find_element_by_css_selector('tr td a').text
		self.driver.find_elements_by_css_selector('tr td a')[0].click()
		next_page_link_text = self.driver.find_element_by_css_selector("h2").text
		self.assertEqual(link_text, next_page_link_text) 
		button_text = self.driver.find_element_by_css_selector('.pure-button').text
		button_link = self.driver.find_element_by_css_selector('.pure-button').get_attribute('href')
		self.assertEqual(u'Go back', button_text)
		self.assertEqual(u'http://pybites.pythonanywhere.com/pyplanet/', button_link)

	def test_login(self):
		self.driver.get("http://pybites.pythonanywhere.com/")
		heading = self.driver.find_element_by_css_selector('#login a').click()
		self.driver.find_element_by_css_selector('#id_username').send_keys("guest")
		self.driver.find_element_by_css_selector('#id_password').send_keys("changeme")
		self.driver.find_element_by_css_selector('button').click()
		self.assertEqual(self.driver.current_url, u'http://pybites.pythonanywhere.com/')
		self.assertEqual(self.driver.find_element_by_css_selector('#login').text, u'Welcome back, guest! Logout  | Home')

		#testing logout
		self.driver.get("http://pybites.pythonanywhere.com/")
		self.driver.find_element_by_css_selector('li a').click()
		self.driver.find_element_by_css_selector('tr td a').click()
		tweet_btn = self.driver.find_element_by_css_selector('.pure-button').text
		self.assertEqual(tweet_btn, u'Tweet this')

		#testing logout text
		self.driver.find_element_by_css_selector('#login a').click()
		log_out_text = self.driver.find_element_by_css_selector('h1').text
		self.assertEqual(log_out_text, u'See you!')

	def tearDown(self):
		self.driver.quit()