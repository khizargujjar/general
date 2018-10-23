@ECHO OFF
SETLOCAL

IF exist "env\" GOTO requirements

call :newline
echo Attempting to create a new Virtual Environment for the project
call :newline

virtualenv env 2>&1 && (
	call :newline
	echo Virtual directory successfully created
	call :newline
) || (
	call :newline
	echo Could not call virtualenv, using pip to install it
	call :newline
	pip install virtualenv 2>&1 && (
		call :newline
		echo Installed virtualenv
		call :newline
		virtualenv env

) || (
	call :newline
	echo Error occurred using pip to install virtualenv. Do you have pip installed on this environment?
	call :newline
	EXIT /B 1
))

:requirements
call :newline
echo Installing requirements to the Virtual Environment
env\Scripts\pip install -r requirements.txt

call :newline
echo Active the Virtual Environment
cmd.exe /K "env\Scripts\activate && cd src"
        
EXIT /B 0

:newline
echo.
exit /b
