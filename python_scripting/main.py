import os
def main():

    print("Main file execution")
    print("Executing external python file")
    exec(open("hello_world.py").read())
    print("creating new file")
    result = os.system("touch new_file.txt")
    if result == 0 :
        print("file created")
    result = os.system("rm new_file.txt")
    if result == 0:
        print("file deleted")
    print("Executing subrocess")
    # exec(open("install_flask.py").read())
    result = os.system("python install_flask.py > deppendencies.txt")
    if result == 0:
        print("process completed")

if __name__ == "__main__":

    main()