@echo off&title MP4 批量掐头去尾（运行版）
setlocal enabledelayedexpansion
echo 该脚本可以批量将目录内MP4文件，从头尾裁减固定时间。（如将多个视频，开头剪3s，结尾剪5s）
echo 如需批量指定视频的开始结束时间，请打开另一个脚本。（如指定多个视频，都从1分12秒开始，到5分27秒结束）
echo 如果您是从其他地方获取的该脚本，请先看一下b站视频，有详细介绍，谢谢。https://www.bilibili.com/video/BV1ic411N7ny/
echo 该脚本基于ffmpeg，请确保您已将ffmpeg添加到环境。
echo 时间作差部分依靠 @随风 @https://pokes.blog.csdn.net/
echo 获取视频文件时长借鉴 @亦良Cool @https://blog.csdn.net/annita2019/article/details/128747458
echo 作者虎啸ROAR b站：https://space.bilibili.com/19075528 个人网站：https://www.luotianyi.blue

rem 提示用户输入开头裁剪的时间，或者跳过
echo 若当前选项为0，可直接按回车
set /p sh=请输入开头切割的 小时部分（如开头无需切割，输入-1）:
if "%sh%" == "-1" goto zs  
if not "%sh%" == "-1" goto os
:zs
set st=00:00:00.00
echo 开头裁剪时长 %st%
goto end
exit
:os
rem 用户输入小时、分钟、秒和毫秒，设置开头裁剪时间
set sh=00
set /p sm=请输入开头切割的 分钟部分:
if "%sm%" == ""  set sm=00
set /p ss=请输入开头切割的 秒部分:
if "%ss%" == ""  set ss=00
set /p sms=请输入开头切割的 毫秒部分:
if "%sms%" == ""  set sms=00
set st=%sh%:%sm%:%ss%.%sms%
echo 开头裁剪时长 %st%
goto end
exit

:end
rem 提示用户输入结尾裁剪的时间，或者跳过
set /p eh=请输入结尾切割的 小时部分（如结尾无需切割，输入-1）:
if "%eh%" == "-1" ( goto ze) else ( goto oe)
exit

:ze
set et=00:00:00.00
echo 结尾裁剪时长 %et%
goto fin
exit
:oe
rem 用户输入小时、分钟、秒和毫秒，设置结尾裁剪时间
set eh=00
set /p em=请输入开头切割的 分钟部分:
if "%em%" == ""  set em=00
set /p es=请输入开头切割的 秒部分:
if "%es%" == ""  set es=00
set /p ems=请输入开头切割的 毫秒部分:
if "%ems%" == ""  set ems=00
set et=%eh%:%em%:%es%.%ems%
echo 结尾裁剪时长 %et%
goto fin
exit
:fin

rem set st=0
rem set et=00:00:02.80 
rem 创建结果目录
cd /d %~dp0
md result

rem 对每个MP4文件进行裁剪
for /f "delims=" %%i in ('dir /b /s /a-d *.mp4') do (
rem 获取视频持续时间
for /f "tokens=2 delims=, " %%a in ('ffmpeg -i "%%i" 2^>^&1 ^| find "Duration:"') do (
    set str=%%a
)
rem 设置裁剪结束时间为输入的结束时间
set time=%et%:!str!
set t=!time!
call :time0 "!t!" "!time!" ok
echo  本视频开始时间为 %st%  结束时间为：!ok!
rem 执行裁剪操作
ffmpeg -ss %st% -to !ok! -accurate_seek -i "%%~si" -c:v copy -c:a copy "result\%%~ni.mp4"
)

pause

rem 将输入的时间转换为ffmpeg可识别的格式
:time0  
@echo off&setlocal&set /a n=0
for /f "tokens=1-8 delims=.: " %%a in ("%~1:%~2") do (
set /a n+=10%%a%%100*360000+10%%b%%100*6000+10%%c%%100*100+10%%d%%100
set /a n-=10%%e%%100*360000+10%%f%%100*6000+10%%g%%100*100+10%%h%%100)
set /a s=n/360000,n=n%%360000,f=n/6000,n=n%%6000,m=n/100,n=n%%100
set "ok=%s%:%f%:%m%.%n%"
endlocal&set %~3=%ok:-=%