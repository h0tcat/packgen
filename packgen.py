import sys
import os

if(not len(sys.argv)==2):
    print("Usage: packgen PackageName")
    sys.exit(0)
else:
    path=sys.argv[1].replace(".","/")
    os.makedirs(path)