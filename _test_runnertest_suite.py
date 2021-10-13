import unittest
from main import *

from blockchain import *
from data import *
import json


class UnitTests(unittest.TestCase):

  def test_validity_on_data(self):
      espresso.add_block()
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_block()
      espresso.add_block()
      espresso.add_block()
      espresso.add_block()
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_block()
      espresso.add_block()
      espresso.add_block()
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_block()
      espresso.add_block()
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
      espresso.add_block()
      espresso.add_block()
      espresso.add_block()
    
      valid = espresso.check_validity()
      self.assertTrue(valid)

