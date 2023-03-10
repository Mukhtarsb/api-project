import unittest
import requests

class TestCalculatorRoute(unittest.TestCase):
    
    def test_valid_request(self):
        url = 'http://localhost:8000/calculator'
        headers = {'Content-Type': 'application/json'}
        data = {"expr": "10,/,2"}
        response = requests.post(url, headers=headers, json=data)
        self.assertEqual(response.status_code, 200)
        
    def test_invalid_request(self):
        url = 'http://localhost:8000/calculator'
        headers = {'Content-Type': 'application/json'}
        data = {"expr": "10,/,0"}
        response = requests.post(url, headers=headers, json=data)
        self.assertEqual(response.status_code, 403)
        
    def test_malformed_request(self):
        url = 'http://localhost:8000/calculator'
        headers = {'Content-Type': 'application/json'}
        data = {"expr": "10,2"}
        response = requests.post(url, headers=headers, json=data)
        self.assertEqual(response.status_code, 400)
