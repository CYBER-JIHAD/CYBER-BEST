import os, sys

try:

    __import__("om").Main()

except Exception as e:

    exit(str(e))
