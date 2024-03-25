#These are examples of the variables to be used.
#Everything will be run locally, so there are no privacy issues for putting sensitive information here.

#SKIP THESE TWO PARAMETERS UNLESS YOU NEED TO. Modify these two parameters if you are going to run the script without Docker.
#importfolder = Provide with the path of the folder containing the CSV file to be modified
importfolder = '/usr/src/app/import'
#outputfolder = Provide with the path of the folder that will contain the modified CSV file
outputfolder = '/usr/src/app/output'

#Input and Output parameters. Change the name to the files you will use for the script, and the name you want for the hashed one.
importfile = 'Test.csv'
outputfile = 'TestHash.csv'

#Secret key, Column ID and Hashed ID parameters.
#secretkey = Provide the secret key for your institution.
secretkey = 'SgkZFJIlWeTJ7rZaeJq8jhRrWqknQSKfOCF99cRMIEg07aBPMkTivFjtn7XE83pu'
#columnid = Provide the name of the column containing the ID's to be hashed.
columnid = 'PatientID (0010,0020)'
#hashid = Provide the name of the desired name containing the final hashed ID's
hashid = 'CMRAD Hash'