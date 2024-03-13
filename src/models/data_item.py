# 定义了一个数据项的模型,包含了需要执行的任务列表和每个任务的执行结果。
import abc

class DataItem:
    def __init__(self, data, flow_names):
        self.data = data
        self.flow_names = flow_names
        self.task_results = []

    def add_task_result(self, task_result):
        self.task_results.append(task_result)

    def save_results(self, storage):
        """
        保存任务执行结果到指定的存储后端
        :param storage: 存储后端实例,需要实现 save_data_item 方法
        """
        storage.save_data_item(self)

    @classmethod
    @abc.abstractmethod
    def from_message(cls, message_body):
        """
        从MQ消息中解析出数据和需要执行的流程列表
        :param message_body: MQ消息体
        :return: DataItem 实例
        """
        pass


class JSONDataItem(DataItem):
    @classmethod
    def from_message(cls, message_body):
        import json
        message_data = json.loads(message_body)
        data = message_data['data']
        flow_names = message_data['flow_names']
        return cls(data, flow_names)