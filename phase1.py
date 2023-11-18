import datetime
import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description="Création du menu pour aller chercher les symboles et les dates ")
    parser.add_argument('-h', '--aide', metavar='AIDE', action='AIDE', help="Afin de pouvoir obtenir de l'aide",)
    parser.add_argument('-d', '--date-debut', metavar='DATE DE DEBUT', help="Afin de pouvoir préciser une date de début")
    parser.add_argument('-f', '--date-fin', metavar='DATE DE FIN', help="Afin de pouvoir préciser une date de fin")
    parser.add_argument('-v', '--valeur', metavar='Valeur', choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], help="Afin de pouvoir choisir la valeur désirée")

#def produire_historique():



   