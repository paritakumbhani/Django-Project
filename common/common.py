from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from csv import reader


def getData(fname):
    try:
        path = settings.BASE_DIR+staticfiles_storage.url(fname)
        with open(path, 'r', encoding='UTF-8-SIG') as filedata:
            fdata = list(reader(filedata, delimiter=','))
            firstRow = list(fdata)[0]
            reqColumnIdx = [x for x in range(0,len(firstRow)) if firstRow[x][-1]!='r' and firstRow[x][-2]!='F']
            allRows = list()
            for rowIdx in range(1,len(fdata)):
                row = list()
                for idx in range(0,len(firstRow)):
                    if(idx in reqColumnIdx):
                        row.append(fdata[rowIdx][idx])
                allRows.append(row)

            return allRows                            
    except:
        return "NO_DATA_FOUND"


def getColumns():
    try:
        path = settings.BASE_DIR+staticfiles_storage.url('canadianCheeseDirectory.csv')
        with open(path, 'r', encoding='UTF-8-SIG') as filedata:
            fdata = list(reader(filedata, delimiter=','))
            firstRow = list(fdata)[0]
            reqColumn = [firstRow[x] for x in range(0,len(firstRow)) if firstRow[x][-1]!='r' and firstRow[x][-2]!='F']
            

            return reqColumn                        
    except:
        return "NO_COLUMN_FOUND"