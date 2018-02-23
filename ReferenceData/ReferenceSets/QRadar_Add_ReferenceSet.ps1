# QRadar Reference Sets: Add example
Import-Module -Name PsIni

$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']

$value = '100.101.102.103'
$params = @{
    uri                  = "https://$ip/api/reference_data/sets/DEMO_IP?value=$value"
    headers              = @{'SEC' = $key }
    Method               = 'Post'
    SkipCertificateCheck = $true
}

$json_data = Invoke-RestMethod @params
$json_data
