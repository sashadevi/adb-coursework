# adb-coursework

This application compares crime data during January 2021 for the West Midlands and Cambridge. 

## Prerequisites

To run the application PostgreSQL and Python need to be installed.

## Installation

Use Python's package manager [pip](https://pip.pypa.io/en/stable/) (or pip3 depending on Python version) to install the package [psycopg2](https://pypi.org/project/psycopg2/)

```bash
pip3 install psycopg2-binary
```

## Setting up a database and importing datasets into a table

Navigate to the root directory of the project and run the file setup.py. This creates and connects to the database, and creates a table.
The police datasets for the West Midlands and Cambridge are then imported into the table.

```bash
python3 setup.py
```

Note: You may need to specify the user, password, host and port number to establish a connection to the database, by editing the setup.py file as follows:

```python
user=<username>, password=<password>, host=<hostname>, port=<portnumber>
```
## Starting the application

To start the application, run the following command in the root directory of the project:

```python
python3 main.py
```
## Using the application

Once running, the commands below can be used to interact with the application: <br/>

``` h ``` to view all possible query options <br/>
``` 1 ``` view all crime types <br/>
``` 2 ``` view crimes by crime type <br/>
``` 3 ``` view crimes by location <br/>
``` 4 ``` view crimes by LSOA name <br/>
``` 5 ``` view crimes by outcome <br/>
``` 6 ``` view crimes by crime type and location <br/>
``` 7 ``` view crimes by crime type and outcome <br/>
``` 8 ``` view crimes by location and outcome <br/>
``` 9 ``` view crimes by LSOA name and outcome <br/>
``` 10 ``` view crimes by crime type, location and LSOA name <br/>
``` 11 ``` view crimes by crime type, location and outcome <br/>
``` 12 ``` view crimes by crime type, LSOA name and outcome <br/>
``` 13 ``` view crimes by location, LSOA name and outcome <br/>
``` 14 ``` view crimes by crime type, location, LSOA name and outcome <br/>

Commands 2 - 9 provide the option to enter input fields to filter the data, or to leave this empty and retrieve all data. <br/>

## Stopping the application

To quit the application, press ``` q ```.
