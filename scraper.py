import scrapy 
from scrapy import Selector
import pandas as pd 
import csv



class  webgisSpider(scrapy.Spider):
    name = 'webgis_spider'
    start_urls = ["file:///mnt/e/Rafi/work/repo/webgis-scrapy/Webgis _ Kota Tanpa Kumuh (KOTAKU)3.html"]
    #table extraction
    def parse(self, response):
        tableitems = []
        tbody = response.xpath('//tbody/tr')
        #response.xpath('//tbody/tr[2]').xpath('td[2]//text()').extract_first() or ""
        for rows in tbody:
            item = {
                'Photo': rows.xpath('td[1]/img/@src').extract_first() or "",
                #response.xpath('//tbody/tr').css('td img::attr(src)').getall()
                'Kota': rows.xpath('td[2]//text()').extract_first() or "",
                'Kelurahan': rows.xpath('td[3]//text()').extract_first() or "",
                'Nama KSM': rows.xpath('td[4]//text()').extract_first() or "",
                'Nama': rows.xpath('td[5]//text()').extract_first() or "",
                'Volume': rows.xpath('td[6]//text()').extract_first() or None,
                'Satuan': rows.xpath('td[7]//text()').extract_first() or "",
                'Latitude': rows.xpath('td[8]//text()').extract_first() or None,
                'Longitude': rows.xpath('td[9]//text()').extract_first() or None
            }
            tableitems.append(item)
        #Convert array ke df, table transform and cleaning
        tabledf = pd.DataFrame(tableitems, columns=['Photo','Kota','Kelurahan','Nama KSM',
                'Nama','Volume','Satuan','Latitude','Longitude'])
        tabledf = tabledf.astype({'Photo': 'string','Kota': 'string','Kelurahan': 'string','Nama KSM': 'string',
                'Nama': 'string','Volume': 'float64','Satuan': 'string','Latitude': 'float64','Longitude': 'float64'})
        print(tabledf.dtypes)
        
        #table load
        yield tabledf.to_json('tabeljabar.json', orient="records")
        yield tabledf.to_csv('tabeljabar.csv',index=False, sep=",")
        yield tabledf.to_excel('tabeljabar.xlsx', sheet_name='jawabarat', index=False)


        
    




        # for rows in response.xpath('//tbody'):
        #     for gambar,kota,kelurahan,ksm,namakeg,vol,sat,lat,long,btn in rows: 

