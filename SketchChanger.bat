@echo off
set CODE="<absolute-path-to-code.py>"
set CMD="wmic logicaldisk where VolumeName="CIRCUITPY" get DeviceID | findstr :"
echo %CMD%
for /F "tokens=*" %%n in ('%CMD%') do @(set DRIVE=%%n)
set DRIVE=%DRIVE:~0,2%\code.py
echo %DRIVE%
copy %CODE% %DRIVE% 
pause