# external/java_caller.py
import subprocess

class JavaCaller:
    def __init__(self, config):
        self.config = config

    async def call_java_method(self, method_name, parameters, data_item):
        command = ['java', '-cp', self.config['classpath'], method_name]
        command.extend(parameters)

        process = await subprocess.create_subprocess_exec(
            *command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            # Process successful output
            pass
        else:
            # Handle error
            pass