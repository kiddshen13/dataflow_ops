# 数据库操作的基类,定义通用的数据库操作方法。

# db/base_db.py
import asyncio
from abc import ABC, abstractmethod

class BaseDatabaseHandler(ABC):
    """
    Abstract base class for database handlers.
    """

    @abstractmethod
    async def execute_operation(self, step_config, data_item):
        """
        Execute the specified database operation.

        Args:
            step_config (dict): Configuration for the database operation step.
            data_item (DataItem): The data item being processed.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        """
        Asynchronous context manager entry point.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Asynchronous context manager exit point.

        Args:
            exc_type (type): Exception type, if an exception occurred.
            exc_val (Exception): Exception value, if an exception occurred.
            exc_tb (traceback): Traceback object, if an exception occurred.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError

async def get_db_handler(database_type, db_config):
    """
    Get a database handler instance based on the specified database type.

    Args:
        database_type (str): The type of the database (e.g., 'elasticsearch', 'mongodb', 'mysql').
        db_config (dict): Configuration for the database connection.

    Returns:
        BaseDatabaseHandler: An instance of the database handler.

    Raises:
        ValueError: If an unsupported database type is specified.
    """
    if database_type == 'elasticsearch':
        from .elasticsearch_db import ElasticsearchHandler
        return ElasticsearchHandler(db_config)
    elif database_type == 'mongodb':
        from .mongodb_db import MongoDBHandler
        return MongoDBHandler(db_config)
    elif database_type == 'mysql':
        from .mysql_db import MySQLHandler
        return MySQLHandler(db_config)
    else:
        raise ValueError(f"Unsupported database type: {database_type}")

async def get_db_connection(db_type, config):
    """
    Get a database connection based on the specified database type and configuration.

    Args:
        db_type (str): The type of the database (e.g., 'elasticsearch', 'mongodb', 'mysql').
        config (dict): Configuration for the database connection.

    Returns:
        Any: A database connection object or parameters for creating a connection.

    Raises:
        NotImplementedError: If the method is not implemented for the specified database type.
    """
    if db_type == 'elasticsearch':
        # Implement logic to create Elasticsearch connection
        raise NotImplementedError
    elif db_type == 'mongodb':
        # Implement logic to create MongoDB connection
        raise NotImplementedError
    elif db_type == 'mysql':
        # Implement logic to create MySQL connection
        raise NotImplementedError
    else:
        raise ValueError(f"Unsupported database type: {db_type}")

async def create_db_connections(config):
    """
    Create database connections based on the provided configuration.

    Args:
        config (dict): Configuration for the databases.

    Returns:
        dict: A dictionary mapping database types to connection objects or parameters.
    """
    db_connections = {}
    for db_type, db_config in config['databases'].items():
        db_connections[db_type] = await get_db_connection(db_type, db_config)
    return db_connections