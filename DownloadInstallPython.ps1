invoke-WebRequest -uri "https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe" -OutFile $env:TEMP\python-3.6.2.exe

#You want to add the "prependPath" in order to add python to the local path.
Write-Host "Installing Python"
Start-Process powershell.exe -ArgumentList "$env:TEMP\python-3.6.2.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait