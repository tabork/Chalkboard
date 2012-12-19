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
    data_files=["icon.ico", "changelog.txt", "license.txt", "Readme.txt", "jre-7u10-windows-i586-iftw.exe", "javaTest.bat", "Chalkboard.exe", "version.txt"]
)
