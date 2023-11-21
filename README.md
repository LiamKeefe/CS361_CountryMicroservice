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

FILES can be changed at the top of the file of microservice.  The input file must be a .txt file, and the output file must be a .json file.  

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

##### UML

![image](https://github.com/LiamKeefe/CS361_CountryMicroservice/assets/122354752/52d2555d-0880-4cbf-a135-b195b4d2271c)


##### Communication contract

1.	What is the current status of the microservice you implemented for your partner to use? Hopefully, it’s done!
Initial purpose and objective for the microservice has been completed

2.	If the microservice isn’t done, which parts aren’t done and when will they be done?
Any parts that have not been properly implemented can be done 48hr at time of report.

3.	Where can your partner find instructions for using your microservice? You should have created these instructions as part of a previous assignment
https://github.com/LiamKeefe/CS361_CountryMicroservice/blob/main/README.md

4.	How is your partner going to access your microservice? Should they get your code from GitHub? Should they run your code locally? Is your microservice hosted somewhere? Etc.
Code has been distributed through canvas discussion and GitHub.  Instructions are in the README.  Microservice should be run in a CLI with Python 3.10+, and several packages.


5.	Have you confirmed that you can successfully call YOUR PARTNER’S microservice? If not, do so. By when will you do that?
I have no confirmed to successfully call my partners Microservice.  I’ll complete that by Wednesday 11/22/2023

6.	If your partner cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?
I am available to troubleshoot the microservice with 48hrs of report.  Immediate support may be provided if reported through email/text.  This service is provided up to the final approval (11/27/2023) or at my discretion.  

7.	If your partner cannot access/call your microservice, by when do they need to tell you?
Friday 11/24/2023

8.	Is there anything else your partner needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your partner?
I may not have the best availability during Thanksgiving weekend, but I’ll try to respond as per the agreement listed here.


