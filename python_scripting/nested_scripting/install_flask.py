import os

def main():
    print("Creating venv")
    os.system("python -m venv venv")
    print("installing flask")
    result = os.system(". venv/bin/activate ; pip install flask --upgrade pip")
    if result == 0:
        print("Flask installation completed")
        os.system(". venv/bin/activate ; pip freeze > requirements.txt")
    else:
        print("Flask installation failed")

if __name__ == "__main__":
     main()