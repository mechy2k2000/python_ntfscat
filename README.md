WARNING !!!!
===============
Very EXPERIMENTAL AND HACKISH. USE with caution!!!           

python_ntfscat by Rafeal Stewart


INTRODUCTION
=================
A simple Python 3 linux command line application that provides a simple user interface for the unix command ntfscat. I wrote to provide a quicker way of grab individual files from NTFS partitions on failing hard drives.


INSTALLING
===========
you need to clone the python_ntfscat.py and ensure your operating system has ntfsprogs installed


RUNNING THE SCRIPT
=================

$ ./python_ntfscat.py 

[user@localhost python_ntfscat]# python3 test_main.py 

Please enter the directory: /
Please enter the device (/dev/sda#): /dev/sda4
/dev/sda4
/
/
****
****
****
****
0 : WARNING: Dirty volume mount was forced by the 'force' mount option.
1 : hiberfil.sys
2 : $RECYCLE.BIN
3 : Boot
4 : bootmgr
5 : BOOTNXT
6 : CPQSYSTEM
7 : Documents and Settings
8 : Intel
9 : MSSTBJ.CAT
10 : pagefile.sys
11 : PerfLogs
12 : Program Files
13 : Program Files (x86)
14 : ProgramData
15 : Python34
16 : runonce.reg
17 : swapfile.sys
18 : System Recovery
19 : System Volume Information
20 : Users
21 : Windows
Select your option: 21
*******/n/n******
 passed file
 $RECYCLE.BIN passed file
 MSSTBJ.CAT passed file
 pagefile.sys passed file
 runonce.reg passed file
 swapfile.sys passed file
 //Windows is a directory
 Do you want me to open [yes/no/back]? yes
 /dev/sda4
 //Windows
 /
 ****
 ****
 ****
 ****
 0 : WARNING: Dirty volume mount was forced by the 'force' mount option.
 1 : .
 2 : addins
 3 : ADFS
 4 : AppCompat
 5 : apppatch
 6 : AppReadiness
 7 : assembly
 8 : bfsvc.exe
 9 : Boot
 10 : bootstat.dat
 11 : Branding
 12 : Camera
 13 : CbsTemp
 14 : CORE.xml
 15 : CoreSingleLanguage.xml
 16 : CSUP.TXT
 17 : Cursors
 18 : debug
 19 : DesktopTileResources
 20 : diagnostics
 21 : DigitalLocker
 22 : DirectX.log
 23 : Downloaded Installations
 24 : Downloaded Program Files
 25 : DPINST.LOG
 26 : DtcInstall.log
 27 : ELAMBKUP
 28 : en-US
 29 : explorer.exe
 30 : FileManager
 31 : Fonts
 32 : Globalization
 33 : Help
 34 : HelpPane.exe
 35 : hh.exe
 36 : IME
 37 : ImmersiveControlPanel
 38 : Inf
 39 : InputMethod
 40 : L2Schemas
 41 : LiveKernelReports
 42 : Logs
 43 : Media
 44 : MediaViewer
 45 : MFGSTAT.zip
 46 : mib.bin
 47 : Microsoft.NET
 48 : Migration
 49 : ModemLogs
 50 : modules.log
 51 : notepad.exe
 52 : Offline Web Pages
 53 : Panther
 54 : Performance
 55 : PFRO.log
 56 : PLA
 57 : PolicyDefinitions
 58 : Prefetch
 59 : py.exe
 60 : pyw.exe
 61 : regedit.exe
 62 : Registration
 63 : rescache
 64 : Resources
 83 : system.ini
 84 : System32
 85 : SystemResources
 86 : SysWOW64
 87 : TAPI
 88 : Tasks
 89 : Temp
 90 : ToastData
 91 : tracing
 92 : twain_32
 93 : twain_32.dll
 94 : vmgcoinstall.log
 95 : vpnplugins
 Select your option: 98
 *******/n/n******
  passed file
  bfsvc.exe passed file
  bootstat.dat passed file
  CORE.xml passed file
  CoreSingleLanguage.xml passed file
  CSUP.TXT passed file
  DirectX.log passed file
  DPINST.LOG passed file
  DtcInstall.log passed file
  WMSysPr9.prx passed file
  write.exe passed file
  win.ini
  
  //Windows/win.ini is a file
  Do you want me to grab : //Windows/win.ini[yes/no]? yes
  Grabbing file.......
  Continue running [Yes/No]: no
  Continue running [Yes/No]: no

[user@localhost ~] $



TODO 
========
Have more error handling and clean up the user experience. Implement a better way of determining wether an object is a file or a directory. Implement a feature to be recursive when grabbing whole directories 


LICENSE
========
The MIT License (MIT)

Copyright (c) 2015 Rafeal N Stewart

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
