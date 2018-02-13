Import-Module -Name PsIni

$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']

$params = @{
    uri                  = "https://$ip/api/siem/offenses"
    headers              = @{'SEC' = $key }
    body                 = $body
    Method               = 'Get'
    SkipCertificateCheck = $true
    ContentType          = 'application/json'
}

$json_data = Invoke-RestMethod @params
$json_data |  Select-Object status, Description

