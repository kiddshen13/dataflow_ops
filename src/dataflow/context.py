# 管理执行任务时所需的上下文信息,如数据库连接。
'''
    这个 Context 类是一个上下文管理器,用于管理数据库连接和外部调用器实例。它在初始化时接收配置信息,并创建 DatabaseManager 和 ExternalCallerManager 实例。

get_database 方法用于获取指定类型的数据库连接对象,如 Elasticsearch、MongoDB 或 MySQL 连接。它将调用 DatabaseManager 的相应方法来获取连接。

get_external_caller 方法用于获取指定的外部调用器实例,如 Java 方法调用器或其他外部服务调用器。它将调用 ExternalCallerManager 的相应方法来获取调用器实例。

这个上下文管理器的作用是提供一个统一的入口点,用于获取任务执行所需的数据库连接和外部调用器实例。通过将这些资源的管理集中在 Context 中,我们可以更好地控制和管理它们的生命周期,同时也提高了代码的可维护性和可扩展性。

在实际使用时,您可能需要实现 DatabaseManager、DatabaseConnection、ExternalCallerManager 和 ExternalCaller 等相关类,以支持不同类型的数据库和外部调用需求。

'''

import asyncio

# dataflow/context.py
from ..db.base_db import create_db_connections

class Context:
    def __init__(self, config):
        self.config = config
        self.db_connections = None

    async def __aenter__(self):
        self.db_connections = await create_db_connections(self.config)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close_db_connections()

    async def close_db_connections(self):
        for db_handler in self.db_connections.values():
            await db_handler.__aexit__(None, None, None)