from urllib.request import urlopen
from bs4 import BeautifulSoup

VERSION="0.0.1"

# Note: class_ attribute is to be supplied acc. to page source

# the base url
base_url = "https://github.com"
print("Fetching data...")

# make a GET request and read it's content
a=urlopen(base_url+"/trending").read()

print("Preparing parser...")

# serve the above markup to BS
b=BeautifulSoup(a,"html.parser")

# Acc. to Source code, the repo list start from 'ol' with class 'repo-list'
c=b.find("ol",class_="repo-list") 

print("Parsing..")

# Next, we find all the children elements to 'ol'
d=c.findAll("li",class_="col-12 d-block width-full py-4 border-bottom")

# Iterate this list and print required data
for x in d:
        
        # Get the name of the repo
        name=x.contents[1].find("a").text.strip()

        # Get the description of the repo
        descr = x.contents[5].text.strip()

        # Split this command into multiple parts to understand it properly
        url=base_url+x.contents[1].find("a").attrs.get("href")

        # Get the programming language used for the repo
        prog_lang=x.contents[7].find("span",class_="mr-3")

        # There are a few cases where a project has no specific
        # programming language. Hence show it when available
        if(type(prog_lang) != type(None)):
                prog_lang=prog_lang.text.strip()

        
        
        # Finally print the details
        print("\n")
        print("Repo name   : "+name)
        print("Repo desc   : "+descr)
        print("Repo URL    : "+url)
        
        # Check if programming language exists
        if(type(prog_lang) != type(None)):
           print("Repo Lang.  : "+prog_lang)
        else:
                print("Repo Lang.  : --")
