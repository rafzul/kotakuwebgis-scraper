

# KOTAKU-WebGIS Scraper

This scraper was build with intention to extracting tables from Kota Tanpa Kumuh WebGIS, courtesy of Ministry of Public Works & Housing (KEMENPUPR) Republic of Indonesia. The web apps and the original tables can be accessed from http://103.12.84.58/webgis/admin/realisasi/provinsi_jabar


### Tools
The scraper was built using Scrapy, a Python open-source web crawling framework. Due to general lagginess of the WebGis (& poor internet connection in my area), the data was crawled from local version of the pages. Data was extracted from the <tr> objects of JQuery datatables used by the apps and loaded into Dataframes. From there, the rows were cleaned and transformed, and finally exported into convenient format of .xls. Json and CSV format were provided if further processing needed.

### Next Version ?
A version that crawl directly from the website (instead of the local files) could be created if necessary. Code refactoring needed to compensate for pagination in the live website and improving the overall code structures. 
