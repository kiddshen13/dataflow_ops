# external/external_caller.py
from .java_caller import JavaCaller

class ExternalCaller:
    def __init__(self, config):
        self.config = config
        self.java_caller = JavaCaller(config.get('java', {}))

    async def call_external_method(self, step_config, data_item):
        method_name = step_config['method_name']
        parameters = step_config.get('parameters', [])

        if method_name.startswith('com.example'):
            await self.java_caller.call_java_method(method_name, parameters, data_item)
        else:
            # Implement calls to other external systems or services
            pass