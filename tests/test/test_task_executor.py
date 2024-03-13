import asyncio
import unittest
from unittest.mock import patch, Mock

from src.dataflow.task_executor import TaskExecutor

class TestTaskExecutor(unittest.TestCase):
    @patch('..dataflow.task_executor.MQConsumer')
    @patch('..dataflow.task_executor.ExternalCaller')
    def test_execute_task(self, mock_external_caller, mock_mq_consumer):
        mock_config = {
            'flows': {
                'flow1': {
                    'tasks': {
                        'task1': {
                            'steps': ['step1', 'step2']
                        }
                    }
                }
            }
        }
        mock_data_item = Mock()
        mock_ctx = Mock()
        mock_get_step_config = Mock(side_effect=[
            {'type': 'api_call'},
            {'type': 'database_operation'}
        ])
        task_executor = TaskExecutor(mock_config)
        task_executor.get_step_config = mock_get_step_config
        task_executor.execute_api_call = Mock()
        task_executor.execute_database_operation = Mock()

        async def test_coroutine():
            await task_executor.execute_task('task1', mock_data_item, mock_ctx)
            task_executor.execute_api_call.assert_called_once()
            task_executor.execute_database_operation.assert_called_once()

        asyncio.run(test_coroutine())

    # Add more tests for other TaskExecutor methods

if __name__ == '__main__':
    unittest.main()