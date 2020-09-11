import subprocess
import os

from rainbowhat_app import celery


class ScriptRunner(object):
    def run(self, command: [str]):
        print("Running task")
        popen = subprocess.Popen(command, universal_newlines=True, preexec_fn=os.setpgrp)
        stdout, stderr = popen.communicate()
        print("Task running on: {}".format(popen.pid))
        if stderr:
            raise Exception("Error "+str(stderr))


scriptRunner = ScriptRunner()


@celery.task
def run_graphics():
    print("Running task")
    command = ["pipenv", "run", "sudo", "python3", "./rainbowhat_app/itv_pic.py"]
    scriptRunner.run(command)
