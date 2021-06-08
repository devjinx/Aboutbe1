@echo off
echo Check update for run
echo.
echo By Thanakorn Chareonlertkamol or Jeong SeokJin
echo IG: _jeongseokjin
echo GitHub: jsjlabsdev
echo.
timeout 5 >null
echo Checking for python !
python --version
echo.
timeout 1 >null
echo Updating pip
pip install pip
pip install pip3
pip3 install pip
pip3 install pip3
pip install --upgrade pip
pip3 install --upgrade pip
pip install --upgrade pip3
pip3 install --upgrade pip3
echo Update pip Successfully
echo.
timeout 1 >null
echo installing module
echo.
pip install pillow 
pip3 install pillow
echo.
echo Run Project
python3 main.py 
timeout 5 >null
del null