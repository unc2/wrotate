import sys
from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["win32api"], "excludes": [
    "tkinter"]}
base = None

setup(name="Rotate",
      version="0.1",
      description="Rotate Windows Screen",
      options={"build_exe": build_exe_options},
      executables=[Executable("src/main.py", base=base, icon="20210112013603.ico")])
