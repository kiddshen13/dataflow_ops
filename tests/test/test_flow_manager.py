import unittest
from unittest.mock import patch, Mock

from src.dataflow.flow_manager import FlowManager

class TestFlowManager(unittest.TestCase):
    @patch('..dataflow.flow_manager.ConfigLoader')
    @patch('..dataflow.flow_manager.TaskExecutor')
    def test_build_task_graph(self, mock_task_executor, mock_config_loader):
        mock_config = {
            'flows': {
                'flow1': {
                    'tasks': [
                        {'name': 'task1', 'dependencies': []},
                        {'name': 'task2', 'dependencies': ['task1']},
                        {'name': 'task3', 'dependencies': ['task1']}
                    ]
                }
            }
        }
        mock_config_loader.return_value.load_config.return_value = mock_config
        flow_manager = FlowManager('config_dir', 'flow1')

        expected_task_graph = {
            'task1': ['task2', 'task3']
        }
        self.assertEqual(flow_manager.task_graph, expected_task_graph)

    # Add more tests for other FlowManager methods

if __name__ == '__main__':
    unittest.main()