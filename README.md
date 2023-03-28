Simple script that adds a column with a hashed ID (in SHA-512/256) to an existing CSV.

### Requirements:
- [Python](https://www.python.org): I usually go for the last version.
- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html): Pandas makes dealing with CSV a lot easier, among other useful utilities.
- [PyCryptodome](https://pypi.org/project/pycryptodome/): This library has a system to do hashing in SHA-512/256 rather quickly.

To install these last two libraries, you may need to install [pip](https://pip.pypa.io/en/stable/installation/).

### Script
There are two ways to run the provided script.
- The first one is just as is. Once you run the script, in the console you will have to provide, in order:
    - The absolute path of the csv, including the name of the file. ("path"/NameOfFile.csv)
    - The Secret Key. It is important to mention this code will be run locally, so there is no way we will see this key.
    - The name of the column containing the IDs to be hashed
    - The absolute path of the csv to be exported, including the name of the file ("path"/NameOfExport.csv)
- The second one is by modifying the code. In comments there's the instructions inside. You can un-comment the variables at the top and comment the input methods below it instead. Then, change the variables to the correct paths, keys and names.

Once the hashing is done, you can close the program.