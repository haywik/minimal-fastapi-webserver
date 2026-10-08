> [!WARNING]
> - Avoid running as ROOT or SUDO at all costs
> - Ideally use a container and unprivileged user

min-fastapi-webserver is a very basic example of how to run a web server with fastapi, with directorys.


# How to use this?

- Method 1 is preffered for automatic bash scripting.

- Method 2 is preffered for step by step user interaction.


---

## Pre-Setup
(skip if u understand this stuff)

Go to where you want it to be stored, i use the home directory.

`git clone https://github.com/haywik/minimised-fastapi-webserver`

This makes a folder in the current directory with the repo.

`cd minmised-fastapi-webserver`

Into the folder


# Setup

Create the python virutal enviroment in the venv folder
`python3 -m venv ./venv `



## Method 1
(good for automatic bash scripts)

`$DIR/venv/bin/python -m pip install $DIR/depend.txt`

- Make sure to set $DIR with the directory of the files.
Otherwise this will throw an error.


## Method 2
(good for step by step user interactions)

`cd venv/bin`

`. activate`
This activates the python virutal enviroment

`cd ..`

`cd ..`
This returns you back to the Root of the git repo, we just cloned.

now the venv is activated shown by the (venv) at the begging of the terminal line

`pip install -r depend.txt`

This installs the depended on packages to run fastapi.


# Running the script

## Method 1 
`$DIR/venv/bin/python -m pip install $DIR/web-project-haywik/wsgi.py`

 
- Make sure to set $DIR with the directory of the files.
Otherwise this will throw an error.

## Method 2
(good for step by step user interactions)

I assume we are still in the correct folder.

`python3 wsgi.py`

And it runs interactivley

or do 
`python3 wsgi.py &`

to run in background

# Further infomation

- Within haywik/linux-public/WebServer-setup, there is a full README.md documenting a way to set this up automaticly and with a systemd file that starts on boot.

- You can pair the method 1 with a systemd startup, to run this on boot.
























    
