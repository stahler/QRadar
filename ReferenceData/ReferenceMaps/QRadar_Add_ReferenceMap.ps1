Import-Module -Name PsIni

$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']

$value = "key=simp09&value=Lisa %20Simpson"

$params = @{
    uri                  = "https://$ip/api/reference_data/maps/DEMO_MAP2?$value"
    headers              = @{'SEC' = $key }
    Method               = 'Post'
    SkipCertificateCheck = $true
}

$json_data = Invoke-RestMethod @params
$json_data

