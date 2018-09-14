import sys, csv

sys.path.append("C:\\Users\\joshu\\WorkSpace\\")
from AnsibleTC.DatabaseTools.Src import Connections

## combine csv files

csvPath = "C:\\Users\\joshu\\WorkSpace\\AnsibleTC\\CsvFiles"

csvList = []
csvList.append("\\compiled-x.csv")
csvList.append("\\compiled-z.csv")
csvList.append("\\compiled.csv")
csvList.append("\\compiledm-r.csv")
csvList.append("\\g-lcompiled.csv")

pathList = []
for i in csvList:
    pathList.append(csvPath + i)


finalList = []

for i in pathList:

    with open(i, 'r') as f:
        listMaker = csv.reader(f, delimiter=',')
        rowList = []
        for j in listMaker:
            rowList.append(j)

        for k in range(1, len(rowList)):
            finalList.append(rowList[k])

## move to database table

ansb = Connections.DbConnection("ANSIBLE101")

insertString = "insert into agentlist "

sqlList = []

for i in finalList:
    # sqlList.append(insertString + "values('" + i[0] + "','" + i[1] + "','" + i[2] + "','" + i[3] + "','" + i[4] + "')")
    sqlList.append(insertString+"values('{}','{}','{}','{}'.'{}')".format(i[0].replace('"', ''),i[1].replace('"', ''),i[2].replace('"', ''),i[3].replace('"', ''),i[4].replace('"', '')))


# print(sqlList[0])


for i in sqlList:
    ansb.executeQuery(i)









# print(sqlList[0])

# query = ";\n".join(sqlList)
#
# ansb.executeQuery(query)






































##
