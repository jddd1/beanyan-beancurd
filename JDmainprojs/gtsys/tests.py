# from django.test import TestCase
# from gtsys.views import MainPage
# '''
# from django.http import HttpRequest
# from django.template.loader import render_to_string
# from django.urls import resolve
# '''

# class HomePageTest(TestCase):
# 	def test_mainpage_as_seen_client(self):
# 		response = self.client.get('/')
# 		self.assertTemplateUsed(response, 'mainpage.html')

# 	def test_responding_post_request(self):
# 		resp = self.client.post('/', data={'customername' :'newcustomName',
# 			'customeremail': 'newcustomEmail',
# 			'customerconcern': 'newcustomConcern',
# 			'customerphone': 'newcustomPhone',
# 			'customeraddress': 'newcustomAdd',
# 			'customermessage': 'newcustomMessage'})
# 		self.assertIn('newcustomName', resp.content.decode())
# 		self.assertTemplateUsed(resp, 'mainpage.html')

from django.test import TestCase
from gtsys.views import MainPage
from .models import Customer_info
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', {'customername': 'John Dale Ranario',
			'customeremail': 'johndale.ranario@gmail.com', 
			'customerphone': '09567031773',
			'customeraddress': 'Laguna',
			'customerconcern': 'Delivery Issues',
			'customermessage': 'Late Delivery',})

		self.assertEqual(Customer_info.objects.count(), 1)
		newInfo = Customer_info.objects.first()
		self.assertEqual(newInfo.YourName, 'John Dale Ranario')
		self.assertEqual(newInfo.YourEmail, 'johndale.ranario@gmail.com')
		self.assertEqual(newInfo.YourPhone, '09567031773')
		self.assertEqual(newInfo.YourAddress, 'Laguna')
		self.assertEqual(newInfo.YourConcern, 'Delivery Issues')
		self.assertEqual(newInfo.YourMessage, 'Late Delivery')

	def test_only_saves_items_uf_necessary(self):
		self.client.get('/')
		self.assertEqual(Customer_info.objects.count(), 0)

	def test_save_POST_redirect(self):
		response = self.client.post('/', {'customername': 'John Dale Ranario',
			'customeremail': 'johndale.ranario@gmail.com', 
			'customerphone': '09567031773',
			'customeraddress': 'Laguna',
			'customerconcern': 'Delivery Issues',
			'customermessage': 'Late Delivery',})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], '/')
	

class ORMTEST(TestCase):
    def test_saving_retrive(self):

    	Customer_list = Customer_info()
    	Customer_list.YourName = 'John Dale Ranario'
    	Customer_list.YourEmail= 'johndale.ranario@gmail.com'
    	Customer_list.YourPhone= '09567031773'
    	Customer_list.YourAddress= 'Laguna'
    	Customer_list.YourConcern= 'Delivery Issues'
    	Customer_list.YourMessage= 'Late Delivery'
    	Customer_list.save()

    	Customer_list = Customer_info()
    	Customer_list.YourName = 'Jeremiah Encluna'
    	Customer_list.YourEmail= 'jeremiah.encluna@gmail.com'
    	Customer_list.YourPhone= '09245692341'
    	Customer_list.YourAddress= 'Dasmarinas'
    	Customer_list.YourConcern= 'Question'
    	Customer_list.YourMessage= 'How to order?'
    	Customer_list.save()

    	Info = Customer_info.objects.all()
    	self.assertEqual(Info.count(), 2)

    	Customer1 = Info[0]
    	Customer2 = Info[1]

    	self.assertEqual(Customer1.YourName, 'John Dale Ranario')
    	self.assertEqual(Customer1.YourEmail, 'johndale.ranario@gmail.com')
    	self.assertEqual(Customer1.YourPhone, '09567031773')
    	self.assertEqual(Customer1.YourAddress, 'Laguna')
    	self.assertEqual(Customer1.YourConcern, 'Delivery Issues')
    	self.assertEqual(Customer1.YourMessage, 'Late Delivery')

    	self.assertEqual(Customer2.YourName, 'Jeremiah Encluna')
    	self.assertEqual(Customer2.YourEmail, 'jeremiah.encluna@gmail.com')
    	self.assertEqual(Customer2.YourPhone, '09245692341')
    	self.assertEqual(Customer2.YourAddress, 'Dasmarinas')
    	self.assertEqual(Customer2.YourConcern, 'Question')
    	self.assertEqual(Customer2.YourMessage, 'How to order?')

    
