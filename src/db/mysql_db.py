# db/mysql_db.py
import aiomysql
from .base_db import BaseDatabaseHandler

class MySQLHandler(BaseDatabaseHandler):
    def __init__(self, connection_params):
        self.connection_params = connection_params
        self.connection = None

    async def __aenter__(self):
        self.connection = await aiomysql.connect(**self.connection_params)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

    async def execute_operation(self, step_config, data_item):
        operation = step_config['operation']
        query = step_config['query']
        params = step_config.get('params', [])

        async with self.connection.cursor() as cursor:
            await cursor.execute(query, params)
            if operation == 'select':
                result = await cursor.fetchall()
                # Process select result
            elif operation == 'insert' or operation == 'update' or operation == 'delete':
                await self.connection.commit()
            # Implement other operations as needed