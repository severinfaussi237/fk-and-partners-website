# FK and Partners — copie statique autonome

## Démarrer

Depuis ce dossier :

```bash
python -m http.server 8080
```

Ouvrir ensuite `http://localhost:8080`.

## Modifier

- Modifier le contenu dans `site-content.json`.
- Exécuter `python build_site.py` pour régénérer les pages HTML.
- Modifier le design dans `assets/site.css`.
- Modifier les interactions dans `assets/site.js`.
- Configurer un endpoint HTTPS dans `assets/form-config.js` pour l’envoi direct des formulaires. Sans endpoint, les formulaires ouvrent le client e-mail avec un message prérempli.

## Déployer sur GitHub Pages

1. Créer un dépôt GitHub vide, avec une branche par défaut nommée `main`.
2. Ajouter le contenu de ce dossier à la racine du dépôt, y compris `CNAME`, `.nojekyll` et `.github/workflows/deploy-pages.yml`.
3. Dans `Settings` > `Pages`, sélectionner `GitHub Actions` comme source de publication.
4. Le workflow publie automatiquement chaque envoi sur `main`.
5. Dans IONOS, créer pour `www` le CNAME indiqué par GitHub Pages pour ce dépôt. Ajouter les redirections de `worldwideib-redirects.csv` au niveau de l’hébergeur/CDN si nécessaire.
6. Dans `Settings` > `Pages`, confirmer le domaine personnalisé `www.fkandpartners.com` et activer HTTPS après propagation DNS.

Le fichier `CNAME` contient déjà le domaine public choisi. Ne pas le modifier sauf changement de domaine.

## Limites

Cette copie ne contient ni runtime Wix, ni Wix Chat, ni Velo/Wix Data, ni comptes, paiements, automatisations ou données privées. Vérifier les droits de réhébergement de chaque asset dans `asset-manifest.json` avant publication.
