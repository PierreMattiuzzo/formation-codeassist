# Exercices — à suivre pas à pas

Prérequis : app installée et lancée (voir `README.md`). Pas de licence Code Assist → binôme.
À chaque exercice, le formateur montre un exemple et la correction.

---

## Exercice 1 — Zero-shot vs Few-shot vs CoT  *(dans le chat)*

Objectif : reclasser les tickets de `donnees.json` (donne-lui le fichier en contexte : `@donnees.json` ou glisse-le dans le chat) en ne modifiant **que** leur catégorie, choisie uniquement parmi celles déjà disponibles (ne pas en inventer) :
`Connexion` · `Paiement` · `Bug` · `Performance` · `Demande` · `Sécurité`

**1.1** Ouvre un nouveau chat et copie ce prompt zero-shot (volontairement pauvre) pour voir la limite :
```
classe les tickets
```
Observe : sans catégories imposées ni exemples, le résultat est vague / incohérent.

**1.2** Ouvre un nouveau chat. Écris un prompt few-shot (donne toi-même 2-3 exemples « ticket → catégorie ») qui reclasse les tickets de `donnees.json`, en ne changeant que la catégorie parmi la liste ci-dessus.

**1.3** Ouvre encore un nouveau chat (contexte propre). Reclasse les tickets de la même façon, mais demande à l'IA de raisonner étape par étape (*CoT*), surtout sur les cas ambigus. Compare avec 1.2.

👉 1 chat = 1 context window : on repart d'un chat neuf pour ne pas polluer le contexte.

---

## Exercice 2 — Prompt : avant / après  *(dans le chat)*

**2.1** Copie ce prompt très basique dans le chat et regarde ce que ça donne :
```
résume les tickets
```

**2.2** Objectif : obtenir un résumé pour remplir un tableau de suivi. Réécris un prompt structuré — rôle + objectif + le fichier `donnees.json` en contexte (`@donnees.json` ou glisse-le dans le chat) + format de sortie imposé — puis compare avec 2.1.

Format attendu :

| Client | Priorité | Résumé | Action |
|--------|----------|--------|--------|
| …      | …        | …      | …      |

---

## Exercice 3 — Confidentialité : exclure & anonymiser

Contexte : l'app affiche `donnees.json`. Les vraies données sensibles sont dans `confidentiel/donnees_reels.json` (mêmes champs, mais vrais clients / e-mails) — l'app ne les lit jamais.

**3.1** Ouvre `confidentiel/donnees_reels.json` : ce sont des données sensibles. Crée un fichier `.aiexclude` à la racine, contenant `confidentiel/`, pour que l'assistant ne les lise jamais.

**3.2** Renomme `donnees.json` en `donnees_old.json` (sauvegarde), puis — en partant uniquement de la structure (les noms de champs), sans jamais montrer les vraies données à l'IA — demande-lui de générer un nouveau `donnees.json` fictif au même format.

**3.3** Relance l'app et vérifie qu'elle fonctionne (bonnes colonnes) et qu'aucune donnée réelle (noms, e-mails…) n'apparaît.

👉 Confidentialité = empêcher l'outil de lire (`.aiexclude`) et ne partager qu'une structure, jamais les vraies données.

---

## Exercice 4 — GEMINI.md & première feature  *(dans l'IDE)*

**4.1** Crée un fichier `GEMINI.md` à la racine avec 3-4 consignes de style de ton choix (ex. : réponds en français, code Python typé, noms de variables explicites).

**4.2** Demande à l'assistant d'ajouter une petite feature à l'app : un filtre par statut (Ouvert / En cours / Résolu) dans la barre latérale. Vérifie que le code produit suit ton style.

**4.3** Relance l'app pour voir le nouveau filtre.

👉 On garde cette feature : on va la documenter et la tester à l'exercice suivant.

---

## Exercice 5 — Documenter, tester… puis automatiser  *(dans l'IDE)*

**5.1** Demande la documentation de la fonction de filtrage — en incluant le nouveau filtre par statut ajouté à l'exo 4.

**5.2** Demande de générer des tests unitaires pour cette fonction (priorité, recherche, statut). Lance-les avec pytest, puis relis-les.

**5.3** Ajoute dans `GEMINI.md` une règle : « documenter et tester systématiquement toute nouvelle fonctionnalité ».

**5.4** Demande une nouvelle feature (ex. un filtre par client) → observe qu'elle arrive déjà documentée et testée, sans avoir à le redemander.

👉 `GEMINI.md` transforme une bonne pratique en réflexe automatique. Tu restes responsable : relis toujours les tests.

---

## Exercice 6 — Mode agent  *(dans l'IDE)*

**6.1** Passe l'assistant en mode agent.

**6.2** Donne-lui d'abord la méthode à suivre à partir de maintenant : toujours poser des questions de clarification, puis proposer un plan, avant de coder. Tu peux l'inscrire dans `GEMINI.md` pour que ce soit permanent.

**6.3** Demande une feature multi-fichiers : ajouter une page « Statistiques » (nombre de tickets par catégorie et par statut, avec un graphique). L'agent doit commencer par ses questions puis son plan → valide le plan avant qu'il code.

**6.4** Demande-lui de faire des choses que lui seul peut faire : lancer les tests (`pytest`) pour vérifier que rien n'est cassé, et corriger si un test échoue.

**6.5** Valide chaque action (Human in the loop), puis relance l'app toi-même pour voir le résultat.

👉 Bonne méthode agent : questions → plan → action → vérification. Un serveur comme Streamlit tourne en continu → c'est en général toi qui relances l'app.

---

## Bonus — Spécifier en amont, réaliser en mode agent  *(dans l'IDE)*

**B.1** En chat (sans écrire de code), demande à l'assistant de rédiger une courte spec d'une évolution de ton choix (ex. : « assigner un ticket à un agent et pouvoir filtrer par agent »), enregistrée dans `SPEC.md`.

**B.2** Relis la spec et ajuste-la : c'est toi qui décides du périmètre.

**B.3** Passe en mode agent, donne `SPEC.md` en contexte et demande de la réaliser. Valide le plan, puis laisse-le coder et lancer les tests.

**B.4** Relance l'app et vérifie le résultat.

👉 Spécifier d'abord, coder ensuite : on maîtrise le « quoi » avant le « comment ».