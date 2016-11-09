#!/usr/bin/python3

from urllib.request import urlopen
from enum import Enum

try:
        from bs4 import BeautifulSoup
        import click
except(ImportError):
        click.echo("Error importing dependencies. Please make sure BeautifulSoup and click are installed.")
        exit(-1)

# gTrends version
VERSION="0.0.1"

# Note: class_ attribute is set acc. to page source

# Enum helps!
class URLS(Enum):
        base =  "https://github.com/"
        trending =  "trending/"


@click.command()
@click.version_option(version=VERSION,message="version %(version)s" )
def main():
        ''' This script displays a list of trending Github repos. '''
        click.echo("Fetching data...")

        # make a GET request and read it's content
        a=urlopen(URLS.base.value + URLS.trending.value).read()

        # serve the above markup to BS
        b=BeautifulSoup(a,"html.parser")

        # Acc. to Source code, the repo list start from 'ol' with class 'repo-list'
        c=b.find("ol",class_="repo-list") 

        click.echo("Parsing..")

        # Next, we find all the children elements to 'ol'
        d=c.findAll("li",class_="col-12 d-block width-full py-4 border-bottom")

        click.echo("Found "+str(len(d))+" repos" )

        # Iterate this list and print required data
        for x in d:
        
                # Get the name of the repo
                name=x.contents[1].find("a").text.strip()

                # Get the description of the repo
                descr = x.contents[5].text.strip()

                # Split this command into multiple parts to understand it properly
                url=str(base_url+x.contents[1].find("a").attrs.get("href"))[1:]

                # Get the programming language used for the repo
                prog_lang=x.contents[7].find("span",class_="mr-3")

                # There are a few cases where a project has no specific
                # programming language. Hence show it when available
                if(type(prog_lang) != type(None)):
                        prog_lang=prog_lang.text.strip()

        
        
                # Finally print the details
                click.echo("\n")
                click.echo("Repo name   : "+name)
                click.echo("Repo desc   : "+descr)
                click.echo("Repo URL    : "+url)
        
                # Check if programming language exists for current repo
                if(type(prog_lang) != type(None)):
                   click.echo("Repo Lang.  : "+prog_lang)
                else:
                   click.echo("Repo Lang.  : --")


if(__name__ == "__main__"):
        main()
