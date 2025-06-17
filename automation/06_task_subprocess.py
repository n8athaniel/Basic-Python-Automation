# Use subprocess to run the echo command and print "Automate all the things!"

import subprocess

result = subprocess.run("echo Automate all the things!", 
                        capture_output=True, text=True, shell=True)
print(result.stdout.strip())

"""
NB: Using shell=True only safe when...
- You control the command string
- You're not passing in user input
"""