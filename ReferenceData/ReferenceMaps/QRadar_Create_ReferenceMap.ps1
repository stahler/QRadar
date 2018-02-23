# QRadar Reference Map: Create example
Import-Module -Name PsIni

$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']

$params = @{
    uri                  = "https://$ip/api/reference_data/maps?"
    headers              = @{'SEC' = $key }
    body                 = @{
        element_type     = 'ALNIC'
        name             = 'DEMO_MAP2'
    }
    Method               = 'Post'
    SkipCertificateCheck = $true
}

$json_data = Invoke-RestMethod @params
$json_data