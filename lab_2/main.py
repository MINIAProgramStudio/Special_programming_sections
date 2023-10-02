import requests
import pandas as pd

url= "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID=1&country=UKR&yearlyTag=Weekly&type=Mean&TagCropland=land&year1=1982&year2=2023"

vhi_url = requests.get(url) #get data
out = open('vhi_id_16.txt','wb') #create text file for data
out.write(vhi_url.content) #save data
out.close() #close file

file_with_commas = open("vhi_id_16.txt",'r') #open file with data
text_with_commas = file_with_commas.read() #read file
file_with_commas.close #close file

first_enter = text_with_commas.find('\n') #delete first line step 1
text_with_commas = text_with_commas[first_enter+1:] #delete first line step 2

arrow_right_pos = text_with_commas.find('<')
arrow_left_pos = text_with_commas.find('>')
while not arrow_right_pos+arrow_left_pos <= -1:
    text_with_commas = text_with_commas[0:arrow_right_pos]+text_with_commas[arrow_left_pos+1:] #deleting html
    arrow_right_pos = text_with_commas.find('<')
    arrow_left_pos = text_with_commas.find('>')

text_clean = text_with_commas.replace(',\n','\n') #delete commas at the end of the lines
text_clean = text_clean.replace(',',';') #replace comas with ;

file_clean = open("vhi_id_16.txt",'w') #open text file for data
file_clean.write(text_clean) #save data
file_clean.close() #close file

print ("VHI is downloaded...")
vhi_csv = pd.read_csv('vhi_id_16.txt')
vhi_csv.to_csv('vhi_id_16.csv')
