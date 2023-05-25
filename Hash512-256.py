import pandas as pd
from Crypto.Hash import SHA512

#These are examples of the variables to be used. You can use this sytem instead of the input system below.
importpath = 'CSV/EUCANIMAGE_UMU_Subject_Tracker.csv'
secretkey = 'SgkZFJIlWeTJ7rZaeJq8jhRrWqknQSKfOCF99cRMIEg07aBPMkTivFjtn7XE83pu'
columnid = 'PatientID'
hashid = 'CMRAD_Hash'
exportpath = 'Hashed/EUCANIMAGE_UMU_Subject_Tracker_Hashed.csv'

#Convert column of patient IDs into a list
df = pd.read_csv(importpath,sep=';')
patientidlist = df[columnid].values.tolist()

#Create new list of hashed IDs
hashlist = []
for index in range(len(df)):
    patientid = patientidlist[index]
    patientidString = str(patientid).replace("-","")  # Omit '-' characters
    text = str(secretkey)+str(patientidString)
    hashObject = SHA512.new(truncate='256')
    hashObject.update(text.encode('utf-8'))
    digest = hashObject.hexdigest()
    hashlist.append(digest)
    print(patientidString + "  " + digest)

#Add new column of hashed IDs into the data frame
df[hashid] = hashlist

#Export modified data frame into a new csv
df.to_csv(exportpath,index=False,sep=';')
