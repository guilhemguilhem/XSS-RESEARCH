$Cred = New-Object -TypeName System.Management.Automation.PSCredential `
              -ArgumentList "NOM UTILISATEUR", (Get-Content PATH_KEY_A_CHANGER | ConvertTo-SecureString -Key $variable_de_cle)
$Cred.GetNetworkCredential().Password