# 负责解析配置文件,管理数据流程的执行。





"""
这个 FlowManager 类负责管理数据流程的执行。它在初始化时接收配置信息和流程名称,并构建任务依赖关系图。build_task_graph 方法根据配置文件中的 tasks 部分构建这个依赖关系字典。

topological_sort 方法实现了拓扑排序算法,用于获取任务的执行顺序,确保先执行依赖任务。

execute 方法是执行数据流程的主要入口点。它首先调用 topological_sort 获取任务执行顺序,然后遍历配置文件中定义的 parallel_groups。对于每个并行组,它会创建一个协程列表,每个协程执行一个任务。最后,使用 asyncio.gather 并行执行这些协程。

在 execute 方法中,我们假设 TaskExecutor 类已经实现了 execute_task 方法,用于执行单个任务。
"""
import asyncio
from collections import defaultdict
from .context import Context

from .task_graph import TaskGraph
from ..utils.config_loader import ConfigLoader

class FlowManager:
    def __init__(self, config_dir, flow_name):
        self.config_loader = ConfigLoader(config_dir)
        self.config = self.config_loader.load_config()
        self.flow_name = flow_name
        self.flow_config = self.config['flows'][flow_name]
        self.task_graph = TaskGraph()
        self.build_task_graph()

    def build_task_graph(self):
        flow_config = self.config_loader.load_flow_config(self.flow_name)
        for task_config in flow_config['tasks']:
            task_name = task_config['name']
            dependencies = task_config['dependencies']
            self.task_graph.add_task(task_name, dependencies)

    def execute(self, data_item, context):
        self.task_graph.execute(data_item, context)