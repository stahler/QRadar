# QRadar Reference Map: Bulk load example
Import-Module -Name PsIni

$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']


$body = @{
    hill01 = 'Benny Hill'
    simp01 = 'Homer Simpson'
    simp02 = 'Marge Simpson'
} | ConvertTo-Json -Compress

$params = @{
    uri                  = "https://$ip/api/reference_data/maps/bulk_load/DEMO_MAP2?"
    headers              = @{'SEC' = $key }
    body                 = $body
    Method               = 'Post'
    SkipCertificateCheck = $true
    ContentType          = 'application/json'
}

$json_data = Invoke-RestMethod @params
$json_data

