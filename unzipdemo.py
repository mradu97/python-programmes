from zipfile import *
f=ZipFile("zip1.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print("file name:",name)
    print("the contents of this file is:")
    f1=open(name,'r')
    print(f1.read())
    f1.close()
