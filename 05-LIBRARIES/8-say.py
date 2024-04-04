import cowsay
import sys
if len(sys.argv) >1:
    cowsay.cow("Hello, "+ sys.argv[1])