Import-Module -Name PsIni

$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']

$body = ('100.100.100.6', '100.100.100.7', '100.100.100.8', '100.100.100.9') | ConvertTo-Json -Compress
$body

$params = @{
    uri                  = "https://$ip/api/reference_data/sets/bulk_load/DEMO_IP"
    headers              = @{'SEC' = $key }
    Method               = 'Post'
    body                 = $body
    SkipCertificateCheck = $true
    ContentType          = 'application/json'

}

$params
$json_data = Invoke-RestMethod @params
$json_data
