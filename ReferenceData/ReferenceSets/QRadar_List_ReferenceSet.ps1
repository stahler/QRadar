Import-Module -Name PsIni
$path = 'C:\Users\stah06\Documents\QRadar\config.ini'
$ini = Get-IniContent -FilePath $path
$ip  = $ini['SIEM']['IP']
$key = $ini['SIEM']['KEY']

$params = @{
    uri     = "https://$ip/api/reference_data/sets/DEMO_IP"
    headers = @{
        'SEC' = $key
    }
    Method               = 'Get'
    SkipCertificateCheck = $true
}
#https://www.red-gate.com/simple-talk/sysadmin/powershell/powershell-data-basics-file-based-data/

$json_data = Invoke-RestMethod @params
$json_data.data