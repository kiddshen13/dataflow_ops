import asyncio
import aio_pika

from ..models.data_item import DataItem
from ..dataflow.flow_manager import FlowManager
from ..dataflow.context import Context
# MQ消费者,监听MQ队列并根据消息类型分发任务。
class MQConsumer:
    def __init__(self, config):
        self.config = config

    async def start_consuming(self):
        connection = await aio_pika.connect_robust(
            host=self.config['host'],
            port=self.config['port'],
            login=self.config['user'],
            password=self.config['password'],
        )

        async with connection:
            channel = await connection.channel()

            for queue_config in self.config['queues']:
                queue_name = queue_config['name']
                queue = await channel.declare_queue(queue_name)

                async def process_message(message: aio_pika.IncomingMessage):
                    async with message.process():
                        data_item = DataItem.from_message(message.body)
                        await self.process_data_item(data_item)

                await queue.consume(process_message, no_ack=True)

    async def process_data_item(self, data_item):
        config_dir = self.config['config_dir']
        flow_name = data_item.flow_name
        async with Context(self.config) as ctx:
            flow_manager = FlowManager(config_dir, flow_name)
            flow_manager.execute(data_item, ctx)
            data_item.save_results()

    async def execute_flow(self, flow_name, data_item):
        flow_manager = FlowManager(self.config, flow_name)
        await flow_manager.execute(data_item)