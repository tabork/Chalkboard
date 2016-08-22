#!/usr/bin/python
from distutils.core import setup
import py2exe, os

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
       if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:
               return 0
       return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

setup(
    windows = [
        {
            "script": "launch.py",
            "icon_resources": [(1, "icon.ico")]
        }
    ],
    options = {
        "py2exe":{
            "dll_excludes": ["MSVCP90.dll"]
        }
    },
    data_files=["icon.ico"]
)
