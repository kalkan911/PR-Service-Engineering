import time
import sys

def main():
    print("Running best App")
    print("Sleeping for 5 seconds")
    time.sleep(5)
    print("woke up")
    raise Exception("Exiting with Error")

if __name__ == "__main__":
    main()
