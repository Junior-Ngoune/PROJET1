import datetime
import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description="Créationggg du menu pour aller chercher les symboles et les dates ")
    parser.add_argument('-symbole', metavar='Symboles...', type=str, nargs='+', help="Nom d'un symbole boursier")
    parser.add_argument('-h', '--help', action='help', help="show this help message and exit")
    parser.add_argument('-d', '--date-debut', metavar='DATE', type=datetime, help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument('-f', '--date-fin', metavar='DATE', type=datetime, help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument('-v', '--valeur', metavar='Valeur', type=str, choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], default='fermeture', help="La valeur désirée (par défaut: fermeture)")
    return parser.parse_args()
#def produire_historique():



   