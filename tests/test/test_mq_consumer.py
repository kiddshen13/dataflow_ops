import asyncio
import unittest
from unittest.mock import patch, Mock

from src.mq.mq_consumer import MQConsumer

class TestMQConsumer(unittest.TestCase):
    @patch('..mq.mq_consumer.aio_pika')
    @patch('..mq.mq_consumer.FlowManager')
    def test_process_data_item(self, mock_flow_manager, mock_aio_pika):
        mock_config = {'config_dir': 'config_dir', 'queues': [{'name': 'queue1', 'type': 'flow1'}]}
        mock_data_item = Mock()
        mock_flow_manager_instance = Mock()
        mock_flow_manager.return_value = mock_flow_manager_instance

        mq_consumer = MQConsumer(mock_config)

        async def test_coroutine():
            await mq_consumer.process_data_item(mock_data_item)
            mock_flow_manager.assert_called_with('config_dir', 'flow1')
            mock_flow_manager_instance.execute.assert_called_with(mock_data_item)
            mock_data_item.save_results.assert_called_once()

        asyncio.run(test_coroutine())

    # Add more tests for other MQConsumer methods

if __name__ == '__main__':
    unittest.main()