import os,sys
fname=input("enter the filname")
if os.path.isfile(fname):
    print("file exists",fname)
    f=open(fname,"r")
else:
    print(" file does not exit ",fname)
    sys.exit(0)
print("the content of file is:")
data=f.read()
print(data)
