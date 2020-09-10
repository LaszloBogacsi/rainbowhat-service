import subprocess

from rainbowhat_app import celery


class ScriptRunner(object):
    def run(self, command: [str]):
        print("Running task")
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
