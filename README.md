# QRadar API

Examples of [QRadar API](https://www.ibm.com/support/knowledgecenter/SSKMKU/com.ibm.qradar.doc_cloud/c_rest_api_getting_started.html) using Python and PowerShell (PowerShell examples coming soon).

All examples are utilized with [IBM QRadar Community Edition](https://developer.ibm.com/qradar/ce/) running on [CentOS Minimal](https://www.centos.org/download/)
* [Reference Data](https://www.ibm.com/support/knowledgecenter/en/SS42VS_7.3.1/com.ibm.qradar.doc/c_qradar_adm_ref_data_collection_overview.html)
    * Reference Sets
        * [Create](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_Create_ReferenceSet.py)
        * [Add (individual)](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_Add_ReferenceSet.py)
        * [Add (bulk)](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_Add_Bulk_ReferenceSet.py)
        * [List](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_List_ReferenceSet.py)
        * Video demonstration<a href="http://www.youtube.com/watch?feature=player_embedded&v=PCDJ1yCQGkY" target="_blank"><img src="http://img.youtube.com/vi/PCDJ1yCQGkY/0.jpg"
alt="QRadar commandline example" width="240" height="180" border="5" /></a>
    * Reference Maps
        * [Create](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceMaps/QRadar_Create_ReferenceMap.py)
        * [Add (individual)](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceMaps/QRadar_Add_ReferenceMap.py)
        * [Add (bulk)](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceMaps/QRadar_Add_Bulk_ReferenceMap.py)
        * [List](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceMaps/QRadar_List_ReferenceMap.py)
    * Reference Map of Sets (incomplete)
    * Reference Map of Maps (incomplete)
    * Reference Table (incomplete)

## AQL Usage
### ReferenceSets
function: [REFERENCESETCONTAINS](https://www.ibm.com/support/knowledgecenter/en/SS42VS_7.3.1/com.ibm.qradar.doc/r_aql_data_functions.html#r_aql_supported_functions__REFERENCESETCONTAINS)
```sql
SELECT DATEFORMAT(starttime,'YYYY-MM-dd HH:mm:ss') as 'Date',
       sourceIP, destinationIP, username
FROM events
WHERE REFERENCESETCONTAINS('DEMO_UserName',username)
```
### ReferenceMaps
function: [REFERENCEMAP](https://www.ibm.com/support/knowledgecenter/en/SS42VS_7.3.1/com.ibm.qradar.doc/r_aql_data_functions.html#r_aql_supported_functions__REFERENCEMAP)
```sql
SELECT username, count(*),
       REFERENCEMAP('DEMO_MAP',LOWER(username)) as Full_Name_Of_User
FROM events
GROUP BY username
```