function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((Test-Admin) -eq $false)  {
    if ($elevated) {
        # tried to elevate, did not work, aborting
    } else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}

$nl = [Environment]::NewLine

Write-Host "Download VSCode Installer"$nl
Invoke-WebRequest "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user" -OutFile $env:USERPROFILE\Downloads\VSCode.exe

Write-Host "Unblock the script"$nl
Unblock-File $env:USERPROFILE\Downloads\VSCode.exe

Write-Host "CD to User Profile"$nl
Set-Location $env:USERPROFILE\Downloads\

Write-Host "Run VSCode Script"$nl
Start-Process $env:USERPROFILE\Downloads\VSCode.exe
