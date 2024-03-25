import pandas as pd
from Crypto.Hash import SHA512
import conf.conf as conf

#Configuring input path
importfolder = conf.importfolder
importfile = conf.importfile
importpath = importfolder+'/'+importfile
#Configuring output path
outputfolder = conf.outputfolder
outputfile = conf.outputfile
outputpath = outputfolder+'/'+outputfile

#Calling on config variables
secretkey = conf.secretkey
columnid = conf.columnid
hashid = conf.hashid

#Convert column of patient IDs into a list
df = pd.read_csv(importpath,sep=';')
patientidlist = df[columnid].values.tolist()

#Create new list of hashed IDs
hashlist = []
for index in range(len(df)):
    patientid = patientidlist[index]
    text = str(secretkey)+str(patientid)
    hashObject = SHA512.new(truncate='256')
    hashObject.update(text.encode('utf-8'))
    digest = hashObject.hexdigest()
    hashlist.append(digest)

#Add new column of hashed IDs into the data frame
df[hashid] = hashlist

#Export modified data frame into a new csv
df.to_csv(outputpath,index=False,sep=';')