# Tickets de support — projet de formation

Petite application **Streamlit** qui liste et filtre des tickets de support.
Elle sert de fil rouge à tous les exercices de la formation.

> ℹ️ **`python` ou `py` ?** Selon les postes, la commande Python s'appelle `python` **ou** `py`.
> Si une commande commençant par `python` renvoie une erreur, réessaie en remplaçant `python`
> par `py` (ex. `py -m streamlit run app.py`). Utilise celle qui marche sur ta machine.

---

## 1. Installer Python (si ce n'est pas déjà fait)

Vérifiez d'abord si Python est présent — dans un terminal (PowerShell) :

```powershell
python --version
```

Si une version **3.10 ou plus** s'affiche, passez à l'étape 2. Sinon, installez Python :

- **Le plus simple (Windows)** — dans PowerShell :
  ```powershell
  winget install Python.Python.3.12
  ```
- **Ou** via le **Microsoft Store** : cherchez « Python 3.12 » puis *Installer*.
- **Ou** téléchargez-le sur https://www.python.org/downloads/ et **cochez « Add python.exe to PATH »** pendant l'installation.

Fermez puis rouvrez le terminal, et revérifiez avec `python --version`.

---

## 2. Installer l'application

Dans le dossier du projet :

```powershell
python -m pip install -r requirements.txt
```

---

## 3. Lancer l'application

```powershell
python -m streamlit run app.py
```

L'application s'ouvre automatiquement dans votre navigateur (sinon, ouvrez l'adresse
affichée, en général http://localhost:8501). Pour l'arrêter : `Ctrl + C` dans le terminal.

> Astuce : on utilise `python -m streamlit …` (et non `streamlit …`) car, sur beaucoup de
> postes Windows, le dossier `Scripts\` de Python n'est pas dans le PATH — la commande
> `streamlit` seule renvoie alors « n'est pas reconnu ». `python -m` évite ce problème.

---

> Pas de licence Code Assist ? Mettez-vous **en binôme** avec quelqu'un qui en a une.
> Les exercices à suivre pas à pas sont dans **`EXERCICES.md`**.
> Données : l'app affiche toujours `donnees.json`. `confidentiel/donnees_reels.json` = fausses « vraies »
> données sensibles, jamais lues par l'app (on les exclut de l'IA via `.aiexclude` à l'exercice 3).
