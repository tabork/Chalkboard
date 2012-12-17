#!/usr/bin/python
from distutils.core import setup
import py2exe

setup(
    windows = [
        {
            "script": "launch.py",
            "icon_resources": [(1, "icon.ico")]
        }
    ],
    data_files=["icon.ico", "license.txt", "Readme.txt", "jre-7u10-windows-i586.exe", "javaTest.bat", "Chalkboard.exe", "version.txt"]
)
