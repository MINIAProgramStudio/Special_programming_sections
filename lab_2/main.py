import requests

url= "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID=1&country=UKR&yearlyTag=Weekly&type=Mean&TagCropland=land&year1=1982&year2=2023"
vhi_url = requests.get(url)
out = open('vhi_id_16.txt','wb')
out.write(vhi_url.content)
out.close()
print ("VHI is downloaded...")