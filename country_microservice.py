"""
Name: Liam Keefe
Course: CS361 Assignment 8
Due Date: 11/20/2023
Description: For the countries information microservice.  Uses wikipedia scrapping to get information. Takes in information from a text file. Returns information to a json file.

For more info, see the README provided.
"""
import requests
import time
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

inputFile = "countryScraper_service.txt"
outputFile = "countryFile.json"

def getAllCountries()->dict:
    """
    Function web scrapes (URL) using BS4 for country name and population.
    Input: None
    Output: struct dictionary with "Country" : "Population" or Error
    """

    tabulated = {}
    country = None
    population = None


    URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    page = requests.get(URL)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find("table", {"class":"wikitable"})

        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(["td", "td"])
            for cell in cells:
                if len(cell.text.strip()) == 0:
                    continue
                
                elif "world" in cell.text.lower():
                    break
                
                elif cell.find('span'):
                    if cell.find('a'):
                        if cell.text.strip().replace(',','').isdigit():
                            population = cell.text.strip().replace(',','')
                        else:
                            country = cell.text.strip()
                    else:
                        continue
                    
                elif cell.find("sup", {"class": "reference"}):
                    continue
                
                else:
                    if cell.text.strip().replace(',','').isdigit():
                        population = cell.text.strip().replace(',','')
                    else:
                        country = cell.text.strip()
                        
            if country is not None and population is not None:
                tabulated[country] = population 
                
        return tabulated
    else:
        return {"Error": "Error: Cannot connect to Wiki to scrape."}
        
    
def getSpecificCountry(countryName:str)->list:
    """
    Function web scrapes (URL) using a specifc country with BS4 for country name.
    Input: countryName:str
    Output: struct list countryName containing countries or Error
    """
    
    tabulated = []
    URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    page = requests.get(URL)
    
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find("table", {"class":"wikitable"})

        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(["td", "td"])
            for cell in cells:
                if countryName.lower() not in cell.text.strip().lower():
                    break
                elif cell.find('span'):
                    if cell.find('a'):        
                        tabulated.append(cell.text.strip())     
                    else:
                        continue
                               
    else:
        tabulated.append("Error: Cannot connect to Wiki to scrape.")
    if len(tabulated) == 0:
        tabulated.append("Error: No results found")
    
    return tabulated
    
    
def getPopulationCountry(countryName:str) -> str:
    """
    Function web scrapes (URL) using a specifc country with BS4 for population.  To be used subsequently after getSpecificCountry
    Input: countryName:str
    Output: string countryName population or Error
    """
    

    marker = False
   
    URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    page = requests.get(URL)
    
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find("table", {"class":"wikitable"})

        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(["td", "td"])
            for cell in cells:
                if marker:
                    marker = False
                elif countryName.lower() not in cell.text.strip().lower():
                    break
                else:
                    marker = True
                    continue
                
                if cell.text.strip().replace(',','').isdigit():        
                    return cell.text.strip()     
                else:
                    break
        
        return "Error: No results found."
                                
    else:
        return "Error: Cannot connect to Wiki to scrape."
        
    
    
    
def getFlagCountry(countryName:str)->str:
    """
    Function web scrapes (URL) using a specifc country with BS4 for country flag's wiki URL.  To be used after getSpecificCountry().
    Input: countryName:str
    Output: string which contents are the URL
    """
   
    URL = "https://en.wikipedia.org/wiki/" + countryName.replace(' ', '_')
    page = requests.get(URL)
    
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find("table", {"class":"infobox"})

        if table:
            flag = table.find('img')
            
            if flag:
                return urljoin(URL, flag['src'])
                
            else:
                return "Error: Flag image not found"
        else:
            return "Error: Incompatible page type (Infobox)"
                                
    else:
        return "Error: Cannot connect to Wiki to scrape."


def outputAll(allCountries: dict) -> None:
    """
    Function makes a consistent output to json file according to README.
    Input: allcountries (dict)
    Output: None, outputs to output file(json)
    """
    output = {
        "Error" : "None",
        "Countries" : allCountries
    }
    
    returnJson(output)

def outputCountryNonSpecific(country: list) -> None:
    """
    Function makes a consistent output to json file according to README.
    Input: error (string), country (list)
    Output: None, outputs to output file(json)
    """
    output = {
        "Error" : "Error: Not specific enough",
        "Countries" : country 
    }
    returnJson(output)

def outputCountrySpecific(country: str, population: str, flag:str) -> None:
    """
    Function makes a consistent output to json file according to README.
    Input: country (string), population (string), flag (string)
    Output: None, outputs to output file(json)
    """
    output = {
        "Error" : "None",
        "Country": country,
        "Population": population,
        "FlagURL": flag
    }
    returnJson(output)
    
def outputError(error: str) -> None:
    """
    Function makes a consistent output to json file according to README.
    Input: error (string)
    Output: None, outputs to output file(json)
    """
    output = {
        "Error": error
    }
    returnJson(output)



def returnJson(object: dict | list | str)->None:
    """
    Function that outputs to JSON file.
    Input: object which is dict, list, or str
    Output: None
    """
    json_object = json.dumps(object)

    with open (outputFile, "w") as outfile:
        outfile.write(json_object)

    


def main():
    """
    Main in this case, is the 'server' side of the microservice.  
    Input: File (countryScraper_service.txt)
    Output: File (countryFile.json)
    """
    with open(inputFile, "w") as openfile:
        openfile.write('')
    with open(outputFile,"w") as openfile:
        openfile.write('')
        
    while(1):
        with open(inputFile, 'r')  as openfile:
            input = openfile.readline()
            input = input.strip()

        
        if len(input) == 0:
            time.sleep(1)
            continue
        else:
            with open(inputFile, "w") as openfile:
                openfile.write('') 
            with open(outputFile,"w") as openfile:
                openfile.write('')  
                
        if "ALL" in input:
            allCountries = getAllCountries()
            if "Error" in allCountries.keys():
                outputError(allCountries)
            else:
                outputAll(allCountries)
                
        else:
            output = getSpecificCountry(str(input))
            if len(output) > 1:
                if "Error" in output:
                    outputError(output)
                else:
                    outputCountryNonSpecific(output)
                    
            elif len(output) == 1:
                country = output[0]
                population = getPopulationCountry(input)
                flagURL = getFlagCountry(input)
                if "Error" in population:
                    outputError(population)
                elif "Error" in flagURL:
                    outputError(flagURL)
                else:
                    outputCountrySpecific(country, population, flagURL)
                
        
    
if __name__ == '__main__':
    main()