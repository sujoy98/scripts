import subprocess

subprocess.call("sudo apt update", shell=True)
subprocess.call("sudo apt dist-upgrade", shell=True)
