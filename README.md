# Pragelato & Turin - Le Quiz

Petite appli web pour decouvrir le village Club Med Pragelato Vialattea et la ville de Turin
entre vendeurs, sous forme de quiz (QCM) et de galerie photo partagee. Pas de compte : chacun
choisit juste un pseudo. Disponible en francais et en hebreu (RTL), avec un bouton FR / עברית
en haut de l'ecran a tout moment.

## Lancer l'application

1. Double-cliquer sur `Lancer l'application.bat`.
2. La fenetre affiche deux adresses :
   - `http://localhost:3000` pour cet ordinateur.
   - `http://<IP>:3000` pour les telephones connectes au **meme wifi**.
3. Chaque personne ouvre l'adresse `http://<IP>:3000` dans son navigateur de telephone,
   choisit un pseudo, et peut jouer.

Laisser la fenetre ouverte pendant toute la session : elle sert l'application a tout le monde.
Fermer la fenetre (ou Ctrl+C) arrete l'appli.

Si Windows demande une autorisation reseau au premier lancement (pare-feu), accepter pour que
les telephones puissent se connecter.

## Modifier les questions du quiz

Toutes les questions sont dans [`data/questions.js`](data/questions.js), avec le format
explique en commentaire en haut du fichier. Chaque question a un texte, des options et une
anecdote en francais (`fr`) et en hebreu (`he`) ; l'ordre des options doit rester identique
dans les deux langues car la bonne reponse (`answerIndex`) est partagee. On peut :
- corriger/completer les questions "village" (infos qui peuvent changer d'une saison a l'autre),
- ajouter de nouvelles questions (copier un bloc, changer l'`id`),
- en supprimer.

Les textes de l'interface (boutons, titres, etc.) sont dans
[`public/i18n.js`](public/i18n.js), aussi en francais et en hebreu.

Redemarrer l'application (fermer puis relancer le `.bat`) pour que les changements soient pris
en compte.

## Fonctionnalites

- **Quiz** : Village, Turin, ou Mix (8 questions aleatoires a chaque partie), avec anecdote
  apres chaque reponse.
- **Classement** : meilleurs scores par categorie, mis a jour en temps reel pour tout le monde.
- **Galerie photo** : chacun peut ajouter une photo (avec legende) depuis son telephone
  (bouton `+`), visible par tous les participants.

## Donnees

Les scores et les photos sont stockes localement sur cet ordinateur, dans `data/store.json`
et `uploads/`. Rien n'est envoye sur internet. Pour repartir de zero avant un nouveau groupe,
on peut vider `data/store.json` (remettre `{"scores": [], "photos": []}`) et vider le dossier
`uploads/`.
