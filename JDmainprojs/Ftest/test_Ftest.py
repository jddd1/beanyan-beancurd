from selenium import webdriver
import unittest

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time


class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	#def tearDown(self):
		#self.browser.quit()

	def test_start_list_and_retrieve(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Giant Taho', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Giant Taho Service Center', headerText)

		CustomerName = self.browser.find_element_by_id('CustomerName')
		self.assertEqual(CustomerName.get_attribute('placeholder'),'Enter your name here.')
		CustomerName.send_keys('John Dale Ranario')
		time.sleep(1)

		CustomerEmail = self.browser.find_element_by_id('CustomerEmail')
		self.assertEqual(CustomerEmail.get_attribute('placeholder'),'Enter your e-mail here.')
		CustomerEmail.send_keys('johndale.ranario@gmail.com')
		time.sleep(0.5)

		CustomerPhone = self.browser.find_element_by_id('CustomerPhone')
		self.assertEqual(CustomerPhone.get_attribute('placeholder'),'Enter your phone number here.')
		CustomerPhone.send_keys('09567031773')
		time.sleep(0.5)

		CustomerAddress= self.browser.find_element_by_id('CustomerAdd')
		self.assertEqual(CustomerAddress.get_attribute('placeholder'),'Enter your address here.')
		CustomerAddress.send_keys('Laguna')
		time.sleep(0.5)

		CustomerConcern = self.browser.find_element_by_id('CustomerConcern')
		self.assertEqual(CustomerConcern.get_attribute('placeholder'),'Choose your concern.')
		selectCustomerConcern = Select(CustomerConcern)
		selectCustomerConcern.select_by_visible_text('Delivery Issues')
		time.sleep(0.5)

		CustomerReview = self.browser.find_element_by_id('customerMessage')
		self.assertEqual(CustomerReview.get_attribute('placeholder'),'Enter message here.')
		CustomerReview.send_keys('Late Delivery')
		time.sleep(0.5)
      		
		but_Confirm = self.browser.find_element_by_id('but_Confirm')
		but_Confirm.click()
		time.sleep(0.5)


		self.browser.get(self.live_server_url)
		self.assertIn('Giant Taho', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Giant Taho Service Center', headerText)

		CustomerName = self.browser.find_element_by_id('CustomerName')
		self.assertEqual(CustomerName.get_attribute('placeholder'),'Enter your name here.')
		CustomerName.send_keys('Jeremiah Encluna')
		time.sleep(1)

		CustomerEmail = self.browser.find_element_by_id('CustomerEmail')
		self.assertEqual(CustomerEmail.get_attribute('placeholder'),'Enter your e-mail here.')
		CustomerEmail.send_keys('jeremiah.encluna@gmail.com')
		time.sleep(1)

		CustomerPhone = self.browser.find_element_by_id('CustomerPhone')
		self.assertEqual(CustomerPhone.get_attribute('placeholder'),'Enter your phone number here.')
		CustomerPhone.send_keys('09245692341')
		time.sleep(1)

		CustomerAddress= self.browser.find_element_by_id('CustomerAdd')
		self.assertEqual(CustomerAddress.get_attribute('placeholder'),'Enter your address here.')
		CustomerAddress.send_keys('Dasmarinas')
		time.sleep(1)

		CustomerConcern = self.browser.find_element_by_id('CustomerConcern')
		self.assertEqual(CustomerConcern.get_attribute('placeholder'),'Choose your concern.')
		selectCustomerConcern = Select(CustomerConcern)
		selectCustomerConcern.select_by_visible_text('Question')
		time.sleep(1)

		CustomerReview = self.browser.find_element_by_id('customerMessage')
		self.assertEqual(CustomerReview.get_attribute('placeholder'),'Enter message here.')
		CustomerReview.send_keys('How to order?')
		time.sleep(1)
      		
		but_Confirm = self.browser.find_element_by_id('but_Confirm')
		but_Confirm.click()
		time.sleep(1)
		
		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		gianttaho_data = table.find_elements_by_tag_name('tr')
		self.assertIn('Entry 1: John Dale Ranario, johndale.ranario@gmail.com, 09567031773, Laguna, Delivery Issues, Late Delivery', [row.text for row in gianttaho_data])
		self.assertIn('Entry 2: Jeremiah Encluna, jeremiah.encluna@gmail.com, 09245692341, Dasmarinas, Question, How to order?', [row.text for row in gianttaho_data])

		
# if __name__ == '__main__' :
# 	unittest.main(warnings='ignore')


