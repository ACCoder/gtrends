# gtrends
A command line utility for viewing Github trending repos.

# Requirements
1. Python 3.x
2. BeautifulSoup
3. Click

# Installation

At the moment, the only way to use **gtrends** is to clone this repo and run gtrends.py

## Adding to $PATH 
IN major Linux distributions, you can symlink gtrends.py like:

`user@host:~ ln -s /home/user/gtrends/gtrends/gtrends.py /home/user/bin/gtrends`

Another workaround would be to add this into your ***.bashrc*** and restart the terminal.

`export PATH=$PATH;/home/user/gtrends/gtrends;`

Of course replace **user** with your appropriate user name.

# Upcoming Features

1. Support for displaying repos of particular language.
2. Support for time based fetching like week & month.
