##### Country Web Scrapper Microservice 

For assignment 8, CS361, build a microservice for your partner. This microservice uses Wikipedia web pages to fetch update information about countries.  

Wikipedia conditions for autonomous services: https://en.wikipedia.org/wiki/Robots.txt

##### Introduction

This microservice uses files as the mode of communication (see Use/Installation section for details).  The service scrapes information from wikipedia as a method to obtain up to date and relevant information.  This method was use over parsing files due to its ability to obtain recent information.  The microservice in itself uses several functions that were made to fetch specific information for each of the features below (see Features for details).

##### Features

By inputting select strings into the input file, you illicit the following features outputted to the output file:

-'ALL' (all caps, without '') outputs all countries, sovereign states, inhabited dependent territories, and sovereign states. based on ISO 3166-1 (from Wikipedia)

-'*Country' (as a string, without '') This is a string containing the country name.  This will output the Country Name (included), Population, and Flag URL (from Wikipedia).  
    -IF the country name is not specific enough, this will return an Error with all the countries that are contain the inputted country name.

##### Use/Installation

This microservice is intended to run using a CLI (command-line interface) using Python3.  The python version (due to syntax)  should be above 3.10. The program also requires the use of the following packages, which may or may not included in your version of python:
    -requests
    -time
    -json
    -BeautifulSoup4
    -urljoin

The microservice is ran like a 'server' where multiple sequential submissions are allowed.  

The microservice upon startup will create and clear all contents in each respective file. After each submission to the input file, the output file will blank.  Once the output file is populated with contents, another input can be inserted.

FILES:
    -Input: "countryScraper_service.txt"
    -Output: "countryFile.json"

    This can be changed at the top of the file.  The input file must be a .txt file, and the output file must be a .json file.  

Input File Structure:
    -Input file should be a string, 1 not whiteline character word, according to the features section above.

Output File Structure:
    -Source structure: Python dictionary
    -For 'ALL' {
        "Error": *Error,
        "Countries": {'*Country' : '*Population', ...}        
    }
    -For '*Country' (if not specific enough)
    {
        "Error" : "Error: Not specific enough"
        "Countries" : ['*Similar countries',...]
    }
    -For '*Country' (specific)
    {
        "Error" : "None",
        "Country": "*Country",
        "Population" : "*Population",
        "FlagURL" : "*URL"
    }
    -IF error
    {
        "Error" : "*Error"
    }
