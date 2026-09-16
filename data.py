"""Chargement et traitement des tickets de support."""
from pathlib import Path
import pandas as pd

CHEMIN_DONNEES = Path(__file__).parent / "donnees.json"


def charger_tickets(chemin=CHEMIN_DONNEES):
    """Charge les tickets depuis donnees.json et renvoie un DataFrame."""
    return pd.read_json(chemin)


# Fonction volontairement peu documentee : sert de support a l'Exercice 5
# (generer une documentation + des tests unitaires avec l'assistant, puis les relire).
def filtrer_tickets(df, priorite=None, recherche=None):
    resultat = df
    if priorite and priorite != "Toutes":
        resultat = resultat[resultat["priorite"] == priorite]
    if recherche:
        masque = resultat["description"].str.contains(recherche, case=False, na=False)
        resultat = resultat[masque]
    return resultat


def stats_par_priorite(df):
    """Renvoie le nombre de tickets par priorite."""
    return df["priorite"].value_counts()
