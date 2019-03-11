@echo off
title Nginx
echo Kill existed nginx
taskkill /F /IM nginx.exe
echo Nginx running...
%~dp0nginx/nginx.exe -p %~dp0nginx
exit