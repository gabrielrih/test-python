import os
import sys
import unittest
#import pytest

from unittest import mock


HERE = os.path.dirname(os.path.realpath(__file__))
root_path = f'{HERE}/../../..'
sys.path.insert(0, root_path)

from test.unit import model
from resources.rabbit import Rabbit

class TestRabbit(unittest.TestCase):
    def setUp(self):
        self.get_environment_variable = mock.patch('os.getenv', lambda *x: 'fake_variable')
        self.startMock()

    def startMock(self):
        self.get_environment_variable.start()

    def stopMock(self):
         self.get_environment_variable.stop()

    @mock.patch('resources.rabbit.Rabbit.open_connection')
    def test_open_channel(self, mock_open_conn):
        # Given
        rabbit = Rabbit()
        mock_open_conn.return_value = model.Connection()

        # When
        channel = rabbit.open_channel()

        # Then
        self.assertEqual(None, channel)