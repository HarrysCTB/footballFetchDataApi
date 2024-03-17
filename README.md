# Football Fetch Data API ⚽️

Ce projet est une application Python qui utilise l'API Football Data pour récupérer des données sur les matchs de football et les affiche dans une application web Django.

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExODZ1c3lhdzB4YnA5cDEza3RvMmRhNmxwYzRtaDI1c3lkYm5wY3Y5YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yxSjD4SqvTWotmEupF/giphy.gif" />
</p>

## Prérequis 🖥️

- Python 3.6 ou supérieur
- Django
- Bibliothèque `requests`
- Bibliothèque `python-dotenv`

Vous pouvez installer les bibliothèques nécessaires avec pip :

```bash
pip install django requests python-dotenv
```
## Configuration 🔌

Ce projet utilise l'API Football Data. Pour le faire fonctionner localement, vous aurez besoin d'un token d'API.
1. Créez un compte sur Football Data et obtenez un token.
2. Créez un fichier .env à la racine du projet.
3. Ajoutez votre token au fichier .env comme suit :


```bash
X_AUTH_TOKEN=votre_token
```
4. Sauvegardez et fermez le fichier. Le token est maintenant disponible pour l'application.

## Utilisation 💻

Pour exécuter l'application, utilisez la commande suivante dans votre terminal :

```bash
python manage.py runserver
```
Ouvrez votre navigateur et accédez à http://localhost:8000 pour voir l'application en action.

## 🎥 Démonstration

![Imgur](https://imgur.com/WExWnSP.png)

## Contribution 🤝

Les contributions sont les bienvenues. Pour contribuer, veuillez forker le projet, créer une nouvelle branche, puis soumettre une Pull Request.

## Licence 📄

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

