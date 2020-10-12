import os,sys,inspect
sys.path.append("../sub-python-module/src")
import greet

if __name__ == "__main__":
    greet.print_version()