import subprocess

def run_command(command:list):
    
    result = subprocess.run(command,stdout=subprocess.PIPE,text=True)
    return result

if __name__ == "__main__":

    #Initializing CLI
    print("Initializing CLI -- version:1.0")
    command = ["./cli"]
    result = run_command(command)
