from foundations.week1.conversions import fahrenheit_to_celsius

import math

def test_fahrenheit_to_celsius_100():
   assert math.isclose(fahrenheit_to_celsius(100),37.7777777778)

def test_fahrenheit_to_celsius_32():
   assert math.isclose(fahrenheit_to_celsius(32),0.00)

def test_negative_temperature():
   assert math.isclose(fahrenheit_to_celsius(-40),-40.0)