with open("./0513-0519.csv",encoding="utf-8") as f, open("./n_0513-0519.csv", 'w',encoding="utf-8") as n:
    n.write("Id,ComputerName,UUID,Time,DiskGeneral\n")
    for line in f:
        line = line.replace(",[{",",\"[{")
        line = line.replace("{\"","{\"\"")
        line = line.replace("\":\"","\"\":\"\"")
        line = line.replace("\",\"","\"\",\"\"")
        line = line.replace("\"}","\"\"}")
        line = line.replace("\":[","\"\":[")
        line = line.replace("]}]","]}]\"")
        n.write(line)