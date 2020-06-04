# PyDamp
> Python-based data addition and managment of PSQL repostories


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Version 0.0.11


PyDamp is a python packages used to streamline the product addition process of the Oregon State University Design Repository. This package allows useres to fill out a simple YAML text file that automatically is added to the PSQL-based OSU design repository.  PyDamp has intergrated checking funtionalilty to ensure that new products meet the data shema standards set forth though literature. 

The future of PyDamp will be focused on improving the functionality of the package including pulling, editing, and modifying exsisting data in the repository; along with pulling data directly to be used in python-based machine learning packages.  Beyond that, PyDamp will be expanded to serve gernalized needs of PSQL management within python. This goal ensures that PyDamp will be useful beyond managment of the OSU Design repository. 


## Installation

Pip:

```sh
pip install pydamp
```

Clone:

```sh
Clone the package onto your local machine. PyDamp is runnable through local directory module running.
```

## Usage
To use Pydamp, the user needs to fill out the provided Product.yaml and server.yaml files. (download from github)

Pip:
```sh
python -m PyDamp.PyDamp_Run [product.yaml] [server.yaml]
```
Clone:
```sh
python PyDamp_Run.py [product.yaml] [server.yaml]
```


## Example
There is an embedded example to test PyDamp on your machine. The example adds a simple vacuum product to your local OSU design repository.
Important: You need the 'Example_Product_input.yaml' and 'PyDamp_Server.yaml' files in the directory that you run the command line execution. (download these files from github)
To run the example - 
Pip:
```sh
python -m PyDamp.PyDamp_Run
```
Clone:
```sh
python PyDamp_Run.py
```
It is also possible to run the example using the usage guidelines and the example YAML files provided
## YAML notes

Be sure to follow the explicit examples and directions in provided YAML files. The required product functions, flows, materials, and type are index by provided and required standized terms. These terms are available as a csv in the PyDamp package in data schema index file. Please ensure you use the index numbers that corresponds to the best fit for describing the product.



## Program Dependencies 

PyDamp requires PSQL and PgAdmin. These programs are required for PyDamp to connect to the local copy of the OSU repository. Basic instructions for installation are found below.

To install the OSU design repository for local access:

1. Install PostgreSQL  (<https://www.postgresql.org/download/>)

2. Add postgres to the system path (if needed)
- Windows:
```sh
	In Search, search for and then select: System (Control Panel)
    Click the Advanced system settings link.
	Click Environment Variables. In the section System Variables, find the PATH environment variable and select it. 
	Click Edit. 
    In the Edit System Variable (or New System Variable) window, specify the value of the PATH environment variable:
    C:\Program Files\PostgreSQL\11\bin (or where ever PostgreSQL/#/bin is located)
    Click OK. 
    Close all remaining windows by clicking OK.
```
- Mac:
```sh
In a terminal window, run:
touch ~/.bash_profile; open ~/.bash_profile
In the textedit document that opens, enter (verify your version and location):
export PATH=${PATH}:/Library/PostgreSQL/11/bin
export PATH=${PATH}:/bin:/usr/bin
Save and close that document
```



3.	Create a database in pgAdmin
	On the left sidebar of pgAdmin, open the dropdowns for “Servers” and “Databases”
    Right click “Databases” and choose “Create -> Database”
    Name the database something intuitive like “design_repository.” The default owner should be “postgres.” Leave all other settings default.
 

3.	In a terminal window, navigate to the folder with the PyDamp OSU repository backup input
```sh
psql -f <filename> -U postgres -d <database>
```
Example, if database created in pgAdmin is called “design_repository” and backup file is called “repobackup”:

```sh
psql -f repobackup -U postgres -d design_repository
```

4.	In pgAdmin, right click the database you created and click “Refresh.” The OSU Design Repository should be now on your machine. 
5.	Find the information needed for the Server.yaml file
```sh
Go to PgAdmin
right click on PostgreSQL12 under the server pull down on the left side
Click Properties 
navigate to connection
the username and port can be copied to the server.yaml
the password is whatever you set for the user during installation
if the connection preferences says 'localhost' the host is 127.0.0.1
the database name is whatever you named the local copy of the OSU design repository
```


## Release History
* 0.0.5
    * Work in progress

## Meta

Vincenzo Ferrero -  Ferrerov@oregonstate.edu

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/VincenzoFerrero/PyDamp](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch 
3. Commit your changes 
4. Push to the branch 
5. Create a new Pull Request


