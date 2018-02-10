Import-Module -Name PsIni

$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']

$body = (Import-Csv -Path .\ip.csv).ip | ConvertTo-Json -Compress

$params = @{
    uri                  = "https://$ip/api/reference_data/sets/bulk_load/DEMO_IP"
    headers              = @{'SEC' = $key }
    Method               = 'Post'
    body                 = $body
    SkipCertificateCheck = $true
    ContentType          = 'application/json'
}

$json_data = Invoke-RestMethod @params
$json_data
