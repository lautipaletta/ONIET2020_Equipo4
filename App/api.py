import requests
import datetime
import json

def pedirDatosUlt(slug):
    url = "https://api.covid19api.com/summary"
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    todos = json.loads(response.text)
    paises = todos.get("Countries")
    for pais in paises:
        if pais.get("Slug") == slug:
            return pais

def pedirDatosDias(slug):
    variable_to = datetime.datetime.now() 
    variable_from = variable_to - datetime.timedelta(days = 11)
    variable_to = str(variable_to).replace(" ", "T")
    variable_from = str(variable_from).replace(" ", "T")
    variable_to = variable_to.split('.')
    variable_from= variable_from.split('.')

    url = "https://api.covid19api.com/country/{}?from={}Z&to={}Z".format(slug, variable_from[0], variable_to[0])
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    dias = json.loads(response.text)
    return dias

def pedirPaises():
    url = "https://api.covid19api.com/https://api.covid19api.com/countriescountries"
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    paises = json.loads(response.text)
    return paises

