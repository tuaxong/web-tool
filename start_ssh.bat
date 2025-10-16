@echo off
:: Check if OpenSSH Server is installed
powershell -Command "Get-WindowsCapability -Online | Where-Object {$_.Name -like 'OpenSSH.Server*'}"

:: Install OpenSSH Server if not installed
powershell -Command "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"

:: Start the SSH service
net start sshd

:: Set service to start automatically on boot
sc config sshd start= auto

:: Show status
netstat -an | find "22"

echo.
echo SSH Server is running.
echo You can now connect with:
echo ssh YOUR_USERNAME@YOUR_PC_IP
pause
