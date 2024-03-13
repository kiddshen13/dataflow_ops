# 负责加载配置文件。
import yaml
'''


在这个 ConfigLoader 类中,我们提供了三个方法来加载不同的配置文件:

load_global_config 方法加载 global_config.yaml 文件,返回一个包含全局配置的字典。
load_flow_config 方法加载指定流程的配置文件,如 flow_1.yaml。
load_config 方法首先加载全局配置,然后遍历 data_types 配置中定义的流程名称,依次加载每个流程的配置文件,并将它们合并到一个完整的配置字典中。
通过这个 ConfigLoader 类,我们可以轻松地加载分散在多个文件中的配置信息。 
'''
class ConfigLoader:
    def __init__(self, config_dir):
        self.config_dir = config_dir

    def load_global_config(self):
        """
        加载全局配置文件。

        Returns:
            dict: 全局配置字典。
        """
        global_config_file = f"{self.config_dir}/global_config.yaml"
        with open(global_config_file, 'r') as file:
            global_config = yaml.safe_load(file)
        return global_config

    def load_flow_config(self, flow_name):
        """
        加载指定流程的配置文件。

        Args:
            flow_name (str): 流程名称。

        Returns:
            dict: 流程配置字典。
        """
        flow_config_file = f"{self.config_dir}/flows/{flow_name}.yaml"
        with open(flow_config_file, 'r') as file:
            flow_config = yaml.safe_load(file)
        return flow_config

    def load_config(self):
        """
        加载所有配置文件。

        Returns:
            dict: 完整的配置字典。
        """
        config = self.load_global_config()
        config['flows'] = {}
        for flow_name in config['data_types'].values():
            config['flows'][flow_name] = self.load_flow_config(flow_name)
        return config