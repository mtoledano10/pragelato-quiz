# Pragelato & Turin - Le Quiz

Petite appli web (Streamlit) pour decouvrir le village Club Med Pragelato Vialattea et la
ville de Turin entre vendeurs, sous forme de quiz (QCM) et de galerie photo partagee. Pas de
compte : chacun choisit juste un pseudo. Disponible en francais et en hebreu (RTL), avec un
bouton FR / עברית en haut de l'ecran.

## Deploiement (lien internet permanent)

L'appli est concue pour tourner sur [Streamlit Community Cloud](https://streamlit.io/cloud)
(gratuit) : une fois deployee, elle a un lien fixe du type
`https://pragelato-quiz.streamlit.app`, accessible depuis n'importe quel telephone avec
internet, sans dependre du wifi ni d'un ordinateur allume.

Voir les instructions de deploiement fournies separement (creation du depot GitHub + connexion
sur share.streamlit.io).

## Lancer en local (optionnel, pour tester)

1. Installer Python 3.11+ si necessaire.
2. `pip install -r requirements.txt`
3. Double-cliquer sur `Lancer l'application.bat` (ou lancer `streamlit run app.py`).
4. L'appli s'ouvre dans le navigateur, generalement sur `http://localhost:8501`.

## Modifier les questions du quiz

Toutes les questions sont dans [`data/questions.py`](data/questions.py), avec le format
explique en commentaire en haut du fichier. Chaque question a un texte, des options et une
anecdote en francais (`fr`) et en hebreu (`he`) ; l'ordre des options doit rester identique
dans les deux langues car la bonne reponse (`answer_index`) est partagee. On peut :
- corriger/completer les questions "village" (infos qui peuvent changer d'une saison a l'autre),
- ajouter de nouvelles questions (copier un bloc, changer l'`id`),
- en supprimer.

Les textes de l'interface (boutons, titres, etc.) sont dans
[`data/i18n.py`](data/i18n.py), aussi en francais et en hebreu.

Sur Streamlit Cloud, l'appli redemarre automatiquement apres chaque modification poussee sur
GitHub (quelques dizaines de secondes).

## Fonctionnalites

- **Quiz** : Village, Turin, ou Mix (8 questions aleatoires a chaque partie), avec anecdote
  apres chaque reponse.
- **Classement** : meilleurs scores par categorie, partages entre tous les joueurs.
- **Galerie photo** : chacun peut ajouter une photo (avec legende) depuis son telephone,
  visible par tous les participants.

## Donnees

Les scores sont stockes dans `data/store.db` (SQLite) et les photos dans `uploads/`, sur le
serveur qui heberge l'appli. Sur le plan gratuit de Streamlit Cloud, ce stockage n'est pas
garanti permanent au-dela d'un redemarrage de l'appli (par exemple apres une longue periode
d'inactivite) : il tiendra tout le sejour tant que l'appli n'est pas redeployee, mais ce n'est
pas un stockage a long terme.
