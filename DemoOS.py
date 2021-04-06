#DemoOS.py

from os.path import *

#print(dir(os.path))

print(abspath("phython.exe"))
print(basename("c:\\python38\\python.exe"))
print(exists("c:\\python38\\python.exe"))
print(getsize("c:\\python38\\python.exe"))

#운영체제에 있는 명령어를 실행
from os import *
# c:\work2 --> c: --> c:\work2
print("현재 작업 폴더:", getcwd())
chdir("..")
chdir("c:\\work2")
print("현재 폴더:", getcwd())
#외부에 실행파일 수행
#system("notepad.exe")

#파일, 폴더 리스트
import glob
print(glob.glob("*.py"))
print("=" * 20)
for item in glob.glob("*.*"):
    print((item))
