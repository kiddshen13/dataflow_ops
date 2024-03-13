import asyncio
import unittest
from unittest.mock import Mock, patch
from dataflow.context import Context  # 使用绝对导入


class TestContext(unittest.TestCase):
    @patch('src.db.base_db.create_db_connections')  # 使用绝对导入路径
    def test_context_manager(self, mock_get_db_connection):
        mock_config = {'databases': {'elasticsearch': {...}, 'mongodb': {...}, 'mysql': {...}}}
        mock_get_db_connection.side_effect = [Mock(), Mock(), Mock()]

        async def test_coroutine():
            async with Context(mock_config) as ctx:
                self.assertIsInstance(ctx.db_connections['elasticsearch'], Mock)
                self.assertIsInstance(ctx.db_connections['mongodb'], Mock)
                self.assertIsInstance(ctx.db_connections['mysql'], Mock)

        asyncio.run(test_coroutine())

if __name__ == '__main__':
    unittest.main()