# 異常機台偵測
找出廠區異常機台
## 判斷規則
以五分鐘為一個區間，在此區間中1分鐘內CPU高於80%以上，連續出現3次即判斷為異常。
## 程式說明
* CSV_DataCleansing.py
  * 資料清洗
* catch in 5 min over 3 event.py
  * 抓取異常機台並存入新檔 
## 使用套件
* os
* glob
* pandas
* fnmatch
