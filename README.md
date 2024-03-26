# Hashing script

This repository was created with the main goal of aiding researchers encrypt patient IDs in SHA-512/256. The simple script will add a column with the encrypted IDs in an existing CSV file containing a list of patient IDs.

- Code Language is written in [Python 3.11](https://www.python.org/downloads/release/python-3110/).
- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html) is used to deal with CSV in a simple manner.
- [PyCryptodome](https://pypi.org/project/pycryptodome/) is used to do hashing SHA-512/256 in a simple manner.

## Installation guide
This script was originally intended to be used without Docker. With Docker, the amounts of steps to be taken will be minimized by the creation of a container with the environment prepared for direct use.

### Installation with Docker
First of all, download and install the [Docker engine](https://www.docker.com). You can use [Docker Desktop](https://www.docker.com/products/docker-desktop/) in case of doubt. You will be asked to create an account, but this step can be skipped.

Once installed, clone or download the repository to your computer:
```bash
git clone https://github.com/acabrelles/Hashing-512-256.git
```
To light up the container with the hashing script, execute the next command inside the root folder:
```bash
docker-compose up -d --build
```
After this step, you can follow the instructions to use the script.

### Installation without Docker
The steps are not much more difficult.

First of all, download and install [Python 3.11](https://www.python.org/downloads/release/python-3110/). The latest version of [Python](https://www.python.org/downloads/) should also work. When asked in the installer, make sure the PATH variables creation is checked.

Then, download and install the required libraries. To do so, you can either run this in a terminal containing [requirements.txt](https://github.com/acabrelles/Hashing-512-256/blob/master/requirements.txt):
```bash
pip install -r requirements.txt
```
Or install the latest libraries separately running directly:
```bash
pip install pandas
```
and
```bash
pip install pycryptodome
```
After this step, you can follow the instructions to use the script.

## Instruction Manual
### Setting configuration and csv file
Before the transformation of the CSV file, you will need to change the file existing in [import](https://github.com/acabrelles/Hashing-512-256/tree/master/import). 
It is important to mention that the provided file must be a CSV file, and as the broader audience of this script is made from exports made directly from Excel export files, the CSV must be separated by `;`. If it is too troublesome, you can change the type of separator in lines 20 and 37 of [Hash512-256](https://github.com/acabrelles/Hashing-512-256/blob/master/Hash512-256.py).

After this, you will need to edit the configuration file [conf.py](https://github.com/acabrelles/Hashing-512-256/blob/master/conf/conf.py) that you will find inside [conf](https://github.com/acabrelles/Hashing-512-256/tree/master/conf).

The first two parameters to be found are `importfolder` and `outputfolder`, which should be ignored if using the Docker install. Otherwise, Modify them to contain the folder containing the CSV file to be modified, and the folder where it should be exported.

```bash
importfolder = '/usr/src/app/import'
outputfolder = '/usr/src/app/output'
```

The next two parameters to be found are `importfile` and `outputfile`, which should contain the names of the CSV files to be imported and exported.

```bash
importfile = 'Test.csv'
outputfile = 'TestHash.csv'
```
The next three parameters to be found are `secretkey`, `columnid` and `hashid`. These parameters must be modified to the secret key provided by your institution/group, the column containing the IDs to be hashed, and the name of the column that will contain the hashed IDs respectively.
```bash
secretkey = 'SgkZFJIlWeTJ7rZaeJq8jhRrWqknQSKfOCF99cRMIEg07aBPMkTivFjtn7XE83pu'
columnid = 'PatientID (0010,0020)'
hashid = 'HashedID'
```
Once these parameters have been changed, you are ready to run the script.

### Transforming the CSV file
### With Docker
To transform the original CSV file into a transformed version containing hashed IDs, after having provided with the original CSV file and modified the configuration file, you will need to run the next line in the terminal with the running Docker container:
```bash
docker exec hashing python Hash512-256.py
```
It should not take long for it to finish. Once it is done, you can stop the Docker container via the client, or with the command:
```bash
docker stop hashing
```
Once the hashing is done, and the container is stopped, you can close the terminal.

### Without Docker
Just like before, you will need to provide with the CSV file and modify the configuration file as specified previously. Then, you can run the next line in a terminal containing the repository folder:

```bash
python Hash512-256.py
```
or
```bash
python <path-to-folder>/Hash512-256.py
```
Once the hashing is done, you can close the terminal.
