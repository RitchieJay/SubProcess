import subprocess

subprocess.run(
    ["ifconfig", "eth0"],
    shell=True,
)