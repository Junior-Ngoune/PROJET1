from datetime import date
import argparse
import requests
import json


def analyser_commande():
    parser = argparse.ArgumentParser(description="Création du menu pour aller chercher les symboles et les dates ")
    parser.add_argument('-symbole', metavar='Symboles...', type=str, nargs='+', help="Nom d'un symbole boursier")
    parser.add_argument('-h', '--help', action='help', help="show this help message and exit")
    parser.add_argument('-d', '--date-debut', metavar='DATE', type=date, help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument('-f', '--date-fin', metavar='DATE', type=date, help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument('-v', '--valeur', metavar='Valeur', type=str, choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], default='fermeture', help="La valeur désirée (par défaut: fermeture)")
    return parser.parse_args()


def produire_historique(symbole, date_debut, date_fin, valeur_desiree):
    symbole = 'goog'
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

    params = {
    'début': '2019-02-18',
    'fin': '2019-02-24',
    }
    
    réponse = requests.get(url=url, params=params)

    if response.status_code == 200:
        réponse = json.loads(réponse.text)
        historique = réponse.get('historique',{})  
        resultats = [(date, values[valeur_desiree]) for date, values in historique.items]
        return resultats



   