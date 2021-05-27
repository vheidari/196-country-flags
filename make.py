import os
import re
import shutil
import glob


buffer_fname_fcode = []
row = []
i = 0

#read country_list
country_list = open('196_courntyr_list.txt', 'r')
flagsList = country_list.readlines()

#buffer and splite name and code of country_list 
for flag in flagsList:
	temp = re.split(r'__', flag)
	fname = temp[0].strip()
	fcode = temp[1].strip()
	row = []
	row.append(fname)
	row.append(fcode)
	buffer_fname_fcode.append(row)

#show country fullname and code list
#print(buffer_fname_fcode)

#read svg file and move to flags_fullname
for svgFile in glob.glob('./circle-flags/flags/*.svg'):
	svgName = re.search(r'(?<=.\/circle-flags/flags\\)(.*)(?=.svg)', svgFile).group(0)
	for index in buffer_fname_fcode:
		if svgName.strip() == index[1].strip():
			print(str(i) + " : " + index[0] + " : " + index[1] + " : is made :)" )
			i = i+1
			
			#copy and rename flags name to flgas_fullname folder 
			if not os.path.exists('./flags_fullname'):
				os.mkdir('./flags_fullname')
			shutil.copy(svgFile, './flags_fullname/' + index[0].strip() + '.svg')
			
			
			#copy flags code to flgas_codename folder 
			if not os.path.exists('./flags_codname'):
				os.mkdir('./flags_codname')
			shutil.copy(svgFile, './flags_codname/' + index[1].strip() + '.svg' )
	
	if svgName == 'xx':
		if not os.path.exists('./flags_fullname'):
			os.mkdir('./flags_fullname')
		shutil.copy(svgFile, './flags_fullname/' + svgName.strip() + '.svg' )
	
		if not os.path.exists('./flags_codname'):
			os.mkdir('./flags_codname')
		shutil.copy(svgFile, './flags_codname/' + svgName.strip() + '.svg' )


