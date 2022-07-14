import glob 
import os

#指定路徑
filepath=r'C:\Users\Mirella\Desktop\2019_0708'
os.chdir(filepath)
#尋找所有.log檔
f = glob.glob(r'C:\Users\Mirella\Desktop\2019_0708\log\*.log') 
print (os.getcwd())
print (os.getcwd())

#開始清洗
for log in f: 
    # 切割檔名
    filename = os.path.basename(log)
    filename_compulete = filename.split(".")[0]
    # 取代後第一行第一個字會變成亂碼，需手動更改
    # 前為取代檔，後為新檔
    with open("./log/"+filename_compulete+".log",encoding="utf-8") as f, open("./csv/"+filename_compulete+".csv", 'w',encoding="utf-8") as n:
        n.write("Id,Time,Data\n") # 加入欄位名稱
        id = 1
        for line in f:
            # 取代
            line = line.replace(",{\"",",\"{\"\"")
            line = line.replace("\": \"","\"\": \"\"")
            line = line.replace("\", \"","\"\", \"\"")
            line = line.replace("\": {\"","\"\": {\"\"")
            line = line.replace("K\"}","K\"\"}")
            line = line.replace("\"}, \"","\"\"}, \"\"")        
            line = line.replace("d\":","d\"\":")
            line = line.strip('\n')
            # 寫入文件
            n.write(str(id)+", "+line+"\"\n")
            id = id+1  
        print ("Compulete "+filename_compulete)
print ("All Compulete")
