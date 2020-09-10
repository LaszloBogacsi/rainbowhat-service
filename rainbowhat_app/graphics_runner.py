import subprocess
import os

from rainbowhat_app import celery


class ScriptRunner(object):
    def run(self, command: [str]):
        print("Running task")
        path = os.getcwd()
        print(path)
        popen = subprocess.Popen(command, universal_newlines=True)
        stdout, stderr = popen.communicate()
        if stderr:
            raise Exception("Error "+str(stderr))


scriptRunner = ScriptRunner()


@celery.task
def run_graphics():
    print("Running task")
    command = ["pipenv", "run", "sudo", "python", "itv_pic.py"]
    scriptRunner.run(command)
