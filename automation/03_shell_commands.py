"""
    Run Shell Commands (subprocess)
"""

import subprocess

# Run a shell command and capture output
# result = subprocess.run(["ls", "-l"],capture_output=True, text=True)
# print(result.stdout)

# Windows version
result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(result.stdout)

"""
"cmd" : Runs the Windows Command Prompt
"/c"  : Run the next command and then exit
"dir" : List directory contents
"""
