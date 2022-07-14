import glob 
import os.path
import pandas as pd
import fnmatch
from pandas.tseries.offsets import Minute
from pandas.tseries.offsets import Second

# 載入所有csv檔
#f = glob.glob(r'C:\Users\Mirella\Documents\處理資料\5分內連續\all_in5_com\data3\*.csv') 
read_path= r"C:\Users\Mirella\Desktop\ASE_Log07_1_cpu\memory"
os.chdir(read_path)

file_list= fnmatch.filter(os.listdir(os.getcwd()),'*.csv')
print(file_list)

def get_frequency(data):
    com_frequency = {}
    for i in range(0,data.shape[0]):
        com_frequency[data['ComputerName'][i]] = com_frequency.get(data['ComputerName'][i], 0) + 1
    if data.shape[0]>=3:
        return com_frequency,data.shape[0]
      
# 重新指定執行位址
os.chdir("C:\\Users\\Mirella\\Desktop\\ASE_Log07_1_cpu")
os.getcwd()

# 寫入檔案
with open("./over3/memory_over3countin5min_1.csv", 'w',encoding="utf-8") as n:
    print("num , ComputerName , over 3 count in 5 min")
    n.write("num , ComputerName , over 3 count in 5 min\n")
    num= 0
    for csv in file_list: 
        filename = os.path.basename(csv)
        df = pd.read_csv('./memory/'+filename)
        data = pd.DataFrame(df)

        # new_time轉換成datetime
        data['new_time']=pd.to_datetime(data.new_time,format='%Y-%m-%d %H:%M:%S')  

        # 將資料開始時間、結束時間，按5m分割（由於時間段可能剛好不是5m的倍數，为避免最后一個時間丢失，因此在最后加上5m）
        frequency = 5
        time_range = pd.date_range(data['new_time'][0], data['new_time'][data.shape[0]-1]+frequency*Minute(), 
                               freq='%sT'%frequency)

        # 將date變為索引
        data = data.set_index('new_time')
        count= 0

        for i in range(0,len(time_range)-1):        
            if get_frequency(data.loc[time_range[i]:time_range[i+1]-1*Second()]) != None:
                #print (data.loc[time_range[i]:time_range[i+1]-1*Second()])
                #print (get_frequency(data.loc[time_range[i]:time_range[i+1]-1*Second()]))
                count+=1            
        if count==0:
            continue
        else:
            num=num+1
            print(num,",",data['ComputerName'][0],",",count)
            n.write(str(num)+","+data['ComputerName'][0]+","+str(count)+"\n")

print("完成")
