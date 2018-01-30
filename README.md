# QRadar API

Examples of [QRadar API](https://www.ibm.com/support/knowledgecenter/SSKMKU/com.ibm.qradar.doc_cloud/c_rest_api_getting_started.html) using Python and PowerShell (PowerShell examples coming soon).

All examples are utilized with [IBM QRadar Community Edition](https://developer.ibm.com/qradar/ce/) running on [CentOS Minimal](https://www.centos.org/download/)
* Ariel
    * searches
        * [Pass AQL](https://github.com/stahler/QRadar/blob/master/Ariel/searches/QRadar_AQL.py)
* Offenses
    * [List](https://github.com/stahler/QRadar/blob/master/Offenses/QRadar_List_Offenses.py)
* [Reference Data](https://www.ibm.com/support/knowledgecenter/en/SS42VS_7.3.1/com.ibm.qradar.doc/c_qradar_adm_ref_data_collection_overview.html)
    * Reference Sets (The only reference collection you can manage in the web console)
        * [Create](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_Create_ReferenceSet.py)
        * [Add (individual)](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_Add_ReferenceSet.py)
        * [Add (bulk)](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_Add_Bulk_ReferenceSet.py)
        * [List](https://github.com/stahler/QRadar/blob/master/ReferenceData/ReferenceSets/QRadar_List_ReferenceSet.py)
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