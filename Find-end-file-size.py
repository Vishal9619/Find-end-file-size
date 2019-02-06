import glob
import os
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('End File size')

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def get_file_size(source):
	row = 1
	allList = [x[0] for x in os.walk(source)]
	for fileORdir in allList:
		flag = True
		for fl in glob.glob(fileORdir+"\\*"):
			if(os.path.isdir(fl)):
		 		if(len(glob.glob(fileORdir+"\\*.jpg"))>=2 or len(glob.glob(fileORdir+"\\*.jpg"))>=2 or len(glob.glob(fileORdir+"\\*.png"))>=2 or len(glob.glob(fileORdir+"\\*.mp4"))>=1):
		 			flag = True
		 			break
		 		else:
			 		flag = False
			 		break
		if(flag):
				if(len(glob.glob(fileORdir+"\\*.pdf"))>=1):  #ignoring the pdf files
					continue
				if(len(glob.glob(fileORdir+"\\*.wav"))>=1):  #ignoring the voice recording
					continue
				if(len(glob.glob(fileORdir+"\\*.xlsx"))>=1):  #ignoring the excel files
					continue
				if(len(glob.glob(fileORdir+"\\*.rar"))>=1):  #ignoring the zipped files
					continue
				sz = get_size(fileORdir)  # size in bytes
				sz_mb = sz/(1024*1024)    # size in MB
					#for converting file size into GB
					# if(sz_mb > 1024):
					# 	sz_gb = sz_mb/1024
					# 	sz_mb = 0
					# sheet1.write(row,0,fileORdir)
					# if(sz_mb):
				sheet1.write(row,0,fileORdir)
				sheet1.write(row,1,str(sz_mb))
				#print(fileORdir+" -> "+str(sz_mb))
					# else:
					# 	sheet1.write(row,1,str(sz_gb)+" GB")
				row+=1

root_folder = "C:\\Users\\axafrance\\Desktop\\nitin"
get_file_size(root_folder)
wb.save('Size_estimation.xls')