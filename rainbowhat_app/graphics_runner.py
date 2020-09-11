import shlex
import subprocess
import os


class ScriptRunner(object):
    def __init__(self) -> None:
        super().__init__()
        self.current_gpid = 0

    def run(self, command: [str]):
        child = subprocess.Popen(command, universal_newlines=True, preexec_fn=os.setpgrp)
        self.current_gpid = os.getpgid(child.pid)
        print("Task running on: {}".format(child.pid))
        # stdout, stderr = child.communicate()
        # if stderr:
        #     raise Exception("Error "+str(stderr))

    def stop(self, command_fn):
        subprocess.check_call(command_fn(self.current_gpid))


class GraphicsExecutor:

    def __init__(self) -> None:
        super().__init__()
        self.runner = None

    def start_graphics(self):
        self.runner = ScriptRunner()
        command = shlex.split("pipenv run sudo python3 ./rainbowhat_app/itv_pic.py")
        self.runner.run(command)
        print("stariing")

    def stop_graphics(self):
        print("stopping")
        self.runner.stop(lambda gpid: shlex.split("sudo kill -SIGINT {}".format(gpid)))
        self.runner = None

    def is_running(self):
        return self.runner is not None
