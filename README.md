> [!WARNING]
> - Do not run as Root/Sudo
<br>

Minimal-fastapi-webserver is a simple linux based example of a traversal webserver and a mini status page using FastAPI.

> ## General summary of contents
> - `public` Stores all files that will be publicly accessable from the internet.
> - `.gitignore` Instructs git to ignore certain files, such as .venv.
> - `README.md` Well you looking at it.
> - `main.py` The main server scriptm, runs the FastAPI instance.
> - `requirements.txt` All the dependanices.
> - `run.sh` Runs main.py via the virtual enviroment.


## How to setup
1. Clone the repo, `git clone https://github.com/haywik/minimal-fastapi-webserver`
2. Go into the repo, `cd minimal-fastapi-webserver`
3. Make a python virutal enviroment, `python3 -m venv .venv`
4. Activate the virutal enviroment, `source .venv/bin/activate` (If source does not works use a `.` instead of source)
5. Intstall the dependancies, `pip install -r requirements.txt`
6. Deactivate the virutal enviroment, `deactivate`
7. Make run.sh executeable, `chmod +x run.sh`
8. Edit run.sh to your mapped ports/IP, `nano run.sh`
9. Run the server, `./run.sh` 
10. Open the server to, http://127.0.0.1:8081 (if using default configs in run.sh)

## Setup explained.

 - 1
It clones the repo, if you arent familar with the git command, its very useful; but simply its used for code managment.
Here you are cloning the public repository within my user space, on github.

- 2
Well here, you are running the `cd` command, this stands for change directory.
Or in basic terms, means move into that folder.

- 3
A python virutal enviroment allows you to install packages, without making them system wide.
The packages and python executeable lives within the .venv folder.

- 4
Activating the virtual enviroment, basicly emulates python.
If you just type `python3` on a new shell, it opens a python terminal.
But activating the virutal enviroment, means it runs all commands within that virutal enviroment, and only saves to that virutal enviroment.

- 5
Dependancies are the packages, explained within step 3.
Basicly the program `main.py` "Depends" on these packages.
Packages are basicly other peoples code, so you dont need to reprogram a whole backend.

- 6
Deactivates that "emulated" python shell, so all python commands now aplly to the user python shell.

- 7
By default in some cases, if you dont give the permission to execute a file, you cant.
`+x` means add a executeable flag (flags decide what permissions a file has).
`+X` removes the executable flag.

- 8
Here we edit the default `127.0.0.1` to any device IP you want, make sure to set it to a `127.x.x.x` IP, otherwise you will work it out the hard way.
`127.0.0.1` Is a perfect IP to leave it on.
We also edit the port 8081, this is the port the server binds to on the IP `127.0.0.1`, so its gonna be `127.0.0.1:8081`.
8081 Is alsoa perfect port to leave it on.

 - 9
This executes the server via the .venv, if you open run.sh, you see it uses a binary (bin) within the .venv to execute.
This means you dont need to activate the "emulated" shell everytime. (Also makes it easier to automate)
Another way to put this is, `/bin/bash` is a binary, a binary is a bit of code in just computer code so 1s and 0s.
This also runs main.py and inputs the IP and port that is placed beside it from run.sh.

- 10
Open the server up on your favorite browser, and connect to it.
If you wish to connect to it from another device on the same LAN, just type the server IP and the port into the browser.


## Why not Root or Sudo
Lets start with SUDO, sudo stands for, `Super user do`, and the super user is Root.
Now lets talk Root, root is the machine owner, it has the higher level of admin out of any user.
No one program can keep this user out.
So thats why we dont give root out to everyone.
Like I would rather not give you my github password, just to access this public repo.
If this webserver is compromised by a bad guy or a rouge AI agent, they now have root access.
They can do whatever they like, side note: This webserver has no know vulubilites at time of writing, but no web server is immune.
So dont run it as root, use a unprivledged user.

## Alternatives to not root
One of the easyiest way would be to use your /home account, if its not root.
Just simply run the `run.sh` and its already a lot safer, but if it is compromised, the hacker can access everything in your home directory.
So just make a new user, and DO NOT add it to the sudo or wheel group.
Done, bam a lot safer already.
Even better you would use something like a LXC, Incus or Docker container, but I first ran it bare metal for neary a year before investing into Incus containers.

## Further Infomation
If you have any questions, check out the contact details on my profile.
There are comments in `main.py` attempting to explain what each line does.
And have fun coding :)
