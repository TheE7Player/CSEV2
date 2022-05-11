set requirement_path=%cd%\requirements.txt

@echo off
cls

echo CSEV2: Manual VEnv Script (11/05/22) [v0.1]

echo Note: Its recommended to have (at least) Python 3.9+ installed and assigned in PATH in Windows...
echo (USE THIS MANUAL SCRIPT IF THE INSTALLER IS HAVING ISSUES!)

python -m venv env
echo NOW ACTIVATING REQUIREMENTS FILE FOR VENV
cd env/Scripts

echo [STEP 1/2]: ENSURING PIP IN VENV IS THE LATEST VERSION
call "python.exe" -m pip install --upgrade pip

echo [STEP 2/2]: ACTIVING PIP FOR REQUIREMENT FILE: %requirement_path%
call "python.exe" -m pip install -r %requirement_path%


echo END OF PROGRAM: You may wish to close this window now :)
PAUSE