# Déroulé animateur — prompts prêts à l'emploi

---

## Exercice 1 — Zero-shot vs Few-shot vs CoT

**Chat 1 — zero-shot (volontairement nul) :**
```
classe les tickets
```
→ Attendu : vague, catégories inventées, format instable. C'est le point de départ.

**Chat 2 — few-shot :**
```
Reclasse chaque ticket de donnees.json (fourni en contexte) en ne changeant QUE la catégorie,
choisie uniquement parmi : Connexion, Paiement, Bug, Performance, Demande, Sécurité.
Exemples :
"Impossible de se connecter, mot de passe invalide" -> Connexion
"Un client a été débité deux fois" -> Paiement
"L'application est très lente le matin" -> Performance
```

**Chat 3 — CoT :**
```
Reclasse chaque ticket de donnees.json (fourni en contexte) dans une catégorie parmi :
Connexion, Paiement, Bug, Performance, Demande, Sécurité. Ne change que la catégorie.
Raisonne étape par étape sur les cas ambigus avant de conclure.
Si tu hésites entre deux catégories, pose moi la question afin que je tranche.
```

---

## Exercice 2 — Prompt : avant / après

**2.1 — prompt « nul » :**
```
résume les tickets
```

**2.2 — prompt structuré (sortie en tableau) :**
```
Agis en tant que responsable du support client. 
Ton objectif est de synthétiser les tickets de support en attente pour m'aider à prioriser les actions.

Voici les tickets à traiter : @donnees.json

Pour chaque ticket, lis la description et déduis-en le niveau d'agacement probable du client (ex: Faible, Modéré, Élevé, Très élevé) en te basant sur le type de problème rencontré. 

Génère un tableau Markdown respectant strictement ce format et ces colonnes :
| Client | Priorité | Résumé | Agacement estimé (IA) | Action |
```
> Donne le fichier en **contexte** (`@donnees.json` ou glisse-le dans le chat) plutôt que de coller son contenu.
**Attendu :** un tableau `Client | Priorité | Résumé | Agacement estimé (IA) | Action`, trié, sans blabla autour.
**Point clé :** Rôle + Objectif + Contexte (l'extrait) + Format (le tableau) rendent la sortie exploitable.

---

## Exercice 3 — Confidentialité : exclure & anonymiser
*Fichiers : `donnees.json` = lu par l'app ; `confidentiel/donnees_reels.json` = vraies données sensibles, jamais lues.*

**3.1 — créer `.aiexclude` à la racine :**
```
confidentiel/
```
Vérifier ensuite que l'assistant ignore le contenu de `confidentiel/`.

**3.2 — renommer, puis régénérer.** Dans le terminal :
```
Génère un jeu de tickets de support FICTIFS au format JSON, enregistré dans donnees.json,
avec exactement ces champs : id, date, client, email, priorite, categorie, description, statut.
15 tickets, entreprises et personnes inventées, aucune donnée réelle.
priorite parmi Basse/Moyenne/Haute/Critique ; statut parmi Ouvert/En cours/Résolu ;
categorie parmi Connexion/Paiement/Bug/Performance/Demande/Sécurité.
```

**3.3 :** relancer l'app (`python -m streamlit run app.py`) → elle doit fonctionner, avec des données
100 % fictives. Aucun client/e-mail de `donnees_reels.json` ne doit apparaître.
**Point clé :** on partage une **structure**, jamais les **valeurs** réelles ; le `.aiexclude` empêche l'outil de lire le fichier sensible.

---

## Exercice 4 — GEMINI.md & première feature

**4.1 — exemple de `GEMINI.md` (à la racine) :**
```markdown
# Consignes projet
- Réponds toujours en français.
- Code Python typé (type hints), noms de variables explicites.
- Pas de commentaires inutiles.
```

**4.2 — prompt de la feature (filtre par statut) :**
```
Agis en tant que développeur Python expert en Streamlit. 
Je souhaite ajouter un nouveau filtre par "statut" dans la barre latérale de mon application.
```
**Point clé :** le code produit suit le style du `GEMINI.md`.

---

## Exercice 5 — Documenter, tester… puis automatiser

**5.1 — documenter :**
```
Agis en tant que développeur expert. Analyse le code de notre application (fichiers app.py et data.py) et rédige une documentation fonctionnelle claire et structurée au format Markdown. La documentation doit comprendre : une brève description de l'objectif de l'outil, la liste des fonctionnalités offertes à l'utilisateur, et l'explication des filtres actuellement disponibles.
```
**5.2 — tester :**
```
En tant qu'ingénieur QA, génère des tests unitaires avec le framework pytest pour la fonction filtrer_tickets du fichier data.py. Concentre-toi spécifiquement sur la logique de filtrage par statut. Je souhaite que tu rédiges au moins deux tests : un cas nominal (filtrage sur un statut spécifique comme 'Ouvert') et un cas de contournement (comportement quand le statut est 'Tous'). N'oublie pas d'ajouter pytest au fichier requirements.txt et de me donner la commande pour l'installer.
```
Puis lancer :
```powershell
python -m pytest test_data.py
python -m pytest
```

**5.3 — règle à ajouter dans `GEMINI.md` :**
```
Mets à jour le fichier GEMINI.md de mon projet en y ajoutant cette nouvelle règle absolue : '- Documenter et tester systématiquement toute nouvelle fonctionnalité (génération de docstrings et de tests unitaires pytest) sans que j'aie besoin de le demander explicitement'
```
**5.4 — nouvelle feature :**
```
Ajoute un bandeau de 3 KPIs en haut de la page principale (app.py) qui se met à jour dynamiquement en fonction des filtres actifs. Je veux : le nombre total de tickets, le nombre de tickets 'Ouverts', et le client ayant le plus de tickets (Client le plus impacté). Assure-toi de placer la logique de calcul de ces KPIs dans de nouvelles fonctions dédiées dans data.py. Applique strictement les règles de projet définies dans mon fichier de contexte.
```

---

## Exercice 6 — Mode agent

**6.2 — méthode à imposer** (à dire, ou à ajouter dans `GEMINI.md`) :
```
Ajoute dans le GEMINI.md 'toujours poser des questions de clarification, puis proposer un plan, avant d'écrire du code. Attendre ma validation du plan.'
```

**6.3 — prompt de la feature (multi-fichiers) :**
```
Ajoute une page "Statistiques" affichant le nombre de tickets par catégorie et par statut,
avec un graphique. Mets à jour app.py et data.py si besoin.
```
L'agent doit d'abord **poser 1-2 questions** puis **dérouler un plan** → tu le valides avant qu'il code.

**6.4 — action « agent-only » :**
```
Lance les tests (pytest) et corrige si l'un échoue.
```

**6.6 — refacto :**
```
Agis en tant qu'architecte logiciel Python. Ton objectif est de nettoyer et d'optimiser le code de cette application.

Voici tes missions :
1. Analyse l'ensemble des fichiers du projet.
2. Identifie le code dupliqué et factorise-le (principe DRY).
3. Réorganise l'architecture du dépôt pour la rendre plus propre, modulaire et maintenable (ex: séparation de l'interface, de la logique métier et de la donnée).

Contraintes :
- Le comportement et les fonctionnalités de l'application doivent rester strictement identiques.

Méthode :
Avant de modifier le moindre fichier, pose-moi les questions de clarification nécessaires, puis propose-moi un plan d'action étape par étape. Attends ma validation expresse sur ce plan avant de commencer à coder.
```

---

# Bonus (si on a le temps)

## Bonus — Spécifier puis réaliser

**B.1 — écrire la spec (en chat, sans coder) :**
```
Sans écrire de code, rédige une spec courte pour cette évolution : "assigner un ticket à un agent
(nouveau champ) et pouvoir filtrer les tickets par agent". Décris : champs à ajouter, impacts sur
l'app, critères d'acceptation. Enregistre le tout dans SPEC.md.
```

**B.3 — réaliser (mode agent, `SPEC.md` en contexte) :**
```
Réalise l'évolution décrite dans SPEC.md (fourni en contexte). Commence par un plan que je valide,
puis implémente, ajoute les tests et lance-les.
```
**Attendu :** un `SPEC.md` clair, puis un plan validé, un champ « agent » ajouté aux données + un filtre,
des tests. **Point clé :** on cadre le « quoi » (spec) avant le « comment » (code).