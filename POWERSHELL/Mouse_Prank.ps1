Add-Type -AssemblyName System.Windows.Forms
$originalPOS = [System.Windows.Forms.Cursor]::Position.X

while (1 -eq 1) {
    if ([Console]::KeyAvailable -or [Windows.Forms.Cursor]::Position.X -eq $originalPOS){
        sleep 2
    }
    else {
		Function Set-Speaker($Volume){$wshShell = new-object -com wscript.shell;1..50 | % {$wshShell.SendKeys([char]174)};1..$Volume | % {$wshShell.SendKeys([char]175)}} & Set-Speaker -Volume 40
		sleep 2
		Start-Process "https://www.youtube.com/watch?v=X8dtA6YdfOM"
		sleep 4
		rundll32.exe user32.dll,LockWorkStation
		msg * Ferme ta session !!!
        break
    }
}