# Usage

This module can be used to scrape the Envirofacts database for all consistently maintained datatables. It takes a single optional argument to direct output to a specified directory.

`python epa-envirofacts-scraper -o ./downloaded-data`

## Scraping tool for Envirofacts

Envirofacts is a unified system for accessing geographically relevant environmental data from a variety of differ
ent data sources. It provides a single API to access many different data models. This tool is to collect as much of that data as possible.

Some useful links:
- [About the data](https://www.epa.gov/enviro/about-data) - Descriptions of the many datasets included in Envirofacts
- [Data models](https://www.epa.gov/enviro/envirofacts-model) - Top level hierarchy of datasets. Each model pertains to a certain topic (air, water, radiation, etc.) and contains several tables.
- [API](https://www.epa.gov/enviro/web-services) - Used  by this code to download and retrieve this data


## Downloaded file directory structure

Due to a server-side restriction, we can only download 10,0000 rows of data per request. For this reason, the data is paginated into .csv files with 10,0000 rows of data each. Table headers are repeated in each file.

Within the downloaded-data subdirectory, a new folder is created for each table and populated with .csv files as follows:

```
+-- downloaded-data
|   +-- table_foo
|   |   +-- table_foo_rows_0_9999.csv
|   |   +-- table_foo_rows_10000_19999.csv
|   |   +-- (etc.)
|   +-- table_bar
|   |   +-- table_bar_rows_0_9999.csv
|   |   +-- table_bar_rows_10000_19999.csv
|   |   +-- (etc.)
```

where table_foo and table_bar and surrogates for table names extracted by the script.

## Server-side request limit

On occasion, we have witnessed requests denied by the server. This is likely due to server settings to combat DDOS attacks. For this reason, it may be necessary to insert some lag time in between successive requests.


## Models not included

The following models, which appear on the [data models](https://www.epa.gov/enviro/envirofacts-model) page, are not retrieved by the code in this project because their pages do not follow the same format as the others. A separate URL has been submitted to the web app (https://www.archivers.space/urls) for each of these.

1. SRS (Substance Registry Service) <br>
Appears to have its own API which we will need to call separately <br>
https://iaspub.epa.gov/sor_internet/registry/substreg/automatedservices/index.jsp

2. ECHO (Enforcement and Compliance History Online) <br>
Automated weekly uploads in .zip format to this website: <br>
https://echo.epa.gov/tools/data-downloads#downloads <br>

3. Cleanups in My Community <br>
Online query interface available here: <br>
https://ofmpub.epa.gov/apex/cimc/f?p=cimc:createtable

4. TSCA (Toxic Substance Control Act) <br>
Online query interface available here:  <br>
https://www3.epa.gov/enviro/facts/tsca/tsca_search.html

5. UV Index <br>
Doesn't appear to be much data. Just a chart ranking the severity of different UV levels. <br>
https://www.epa.gov/enviro/uv-index-overview

6. Information Collection Rule (ICR) <br>
Appears to use Envirofacts like well-behaved datasets, but the model description pages are formatted differently <br>
https://archive.epa.gov/enviro/html/icr/web/html/icr_model.html

## Contact
Contact the authors at @aniketaranake, @cabhishek, github/dgkf
