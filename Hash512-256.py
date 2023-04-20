import pandas as pd
from Crypto.Hash import SHA512

#These are examples of the variables to be used. You can use this sytem instead of the input system below.
importpath = 'Import/Test.csv'
importpath = 'Import/EUCANIMAGE_UMU_Subject_Tracker.csv'
secretkey = 'SgkZFJIlWeTJ7rZaeJq8jhRrWqknQSKfOCF99cRMIEg07aBPMkTivFjtn7XE83pu'
columnid = 'PatientID (0010,0020)'
hashid = 'CMRAD Hash'
exportpath = 'Export/TestHash.csv'

#This section can be deleted/hidden in comments if you prefer using the variables above directly instead
#importpath = input('Enter the absolute path of the file containing the IDs to be hashed: ')
#secretkey = input('Enter the secret key to be used for hashing: ')
#columnid = input('Enter the name of the column containing the IDs to be hashed: ')
#hashid = input('Enter the name of the column containing the hashed IDs: ')
#exportpath = input('Enter the absolute path of the file to export the new file with the Hashed IDs: ')

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
df.to_csv(exportpath,index=False,sep=';')
