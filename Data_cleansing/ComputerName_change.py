# 前為取代檔，後為新檔
with open("1564140294_1765652.csv",encoding="utf-8") as f, open("computername.txt", 'w',encoding="utf-8") as n:
    for line in f:
        line=line.strip('\n')
        n.write("<choice value=\""+line+"\">"+line+"</choice>\n")
