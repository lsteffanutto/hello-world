# alias_doskeys

t=cd Desktop\POC_UC3_KARlab_PPO\POC1\Assets\ML-Agents\Examples\CarAgentScenario2\Config $T
ci=conda info --envs $T
a=conda activate mlagents-r17-OUI $T
clear=cls $*
l=mlagents-learn $*
docml=mlagents-learn --help
res=tensorboard --logdir results --port 6006

ac=conda activate Carla_py_3.7 $T
gc=cd C:\Users\steffanutto\Desktop\UC3_Carla
gocode=cd C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\examples | code .
carla=cd C:\Users\steffanutto\Desktop\UC3_Carla | CarlaUE4.exe /Game/Carla/Maps/Town05 -quality-level=Low -ResX=800 -ResY=500 -fps=10 -windowed $T
c=CarlaUE4 -carla-server /Game/Carla/Maps/Town01 -windowed -ResX=1000 -ResY=500
ocmd=start cmd.exe "/K" C:\Users\steffanutto\Anaconda3\Scripts\activate.bat C:\Users\steffanutto\Anaconda3\envs\Carla_py_3.7
ir=cd C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\examples
wp=python --version
e=exit
mc=cd C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\examples | python C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\examples\manual_control.py
sv=cd C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\examples | python C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\examples\spawn_npc.py -n 200
t= python ppo_carla\hellocarla.py
cm=cd C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\util | python C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\util\config.py --map Town05
gu=cd C:\Users\steffanutto\Desktop\UC3_Carla\PythonAPI\util
ifconfig = ipconfig /all
m= runas.exe /savecred /user:LucasAdmin "C:\Program Files\MATLAB\R2021a\bin\matlab.exe" 
o=start .\
c=code .
cudainfo=nvcc --version
cudainfo2=nvidia-smi

alias   = doskey $*
cat     = type $*
clear   = cls $*
cp      = copy $*
cpr     = xcopy $*
grep    = find $*
history = doskey /history
kill    = taskkill /PID $*
ls      = dir $*
man     = help $*
mv      = move $*
ps      = tasklist $*
pwd     = cd
rm      = del $*
rmr     = deltree $*
sudo    = runas /user:administrator $*
