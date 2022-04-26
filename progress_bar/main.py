import subprocess

commands = ["pip","show","-f","about-time"]
result = subprocess.run(commands,stdout=subprocess.PIPE,text=True)
print("-----------------------------------------")
print(result.args)
print(result.returncode)
print(result.stderr)
print(result.stdout)

commands = ["pip","list","-u"]
result = subprocess.run(commands,stdout=subprocess.PIPE,text=True)
print("-----------------------------------------")
print(result.args)
print(result.returncode)
print(result.stderr)
print(result.stdout)