import unittest
from unittest.mock import mock_open, patch

from src.utils.config_loader import ConfigLoader


class TestConfigLoader(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='global_config: {}')
    def test_load_global_config(self, mock_file):
        config_loader = ConfigLoader('config_dir')
        global_config = config_loader.load_global_config()
        self.assertEqual(global_config, {'global_config': {}})

    @patch('builtins.open', new_callable=mock_open, read_data='flow_config: {}')
    def test_load_flow_config(self, mock_file):
        config_loader = ConfigLoader('config_dir')
        flow_config = config_loader.load_flow_config('flow1')
        self.assertEqual(flow_config, {'flow_config': {}})

    # Add more tests for other ConfigLoader methods

if __name__ == '__main__':
    unittest.main()