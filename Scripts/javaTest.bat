@echo off

if exist "C:\Program Files (x86)\Java\jre7\bin\java.exe" goto existing
if exist "C:\Program Files\Java\jre7\bin\java.exe" goto check
goto install

:check
if exist "C:\Program Files (x86)" goto install
goto existing

:install
echo installing
jre-7u13-windows-i586-iftw.exe
goto existing

:existing
echo done