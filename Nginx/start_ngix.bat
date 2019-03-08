@echo off
title Nginx
echo Nginx running...
taskkill /F /IM nginx.exe
%~dp0nginx/nginx.exe -p %~dp0nginx
exit