<h3 align="center">
    <img alt="Logo" title="#logo" width="250px" src="/assets/1600429119334_P6.png">
    <br>
</h3>


# OpenClassrooms Projet P7

- [Objectif](#obj)
- [Compétences](#competences)
- [Technologies](#techs)
- [Requirements](#reqs)
- [Architecture](#architecture)
- [Configuration locale](#localconfig)
- [Présentation](#presentation)

<a id="obj"></a>
## Objectif

AlgoInvest&Trade est une société financière spécialisée dans l'investissement. La société cherche à optimiser ses stratégies d'investissement à l'aide d'algorithmes, afin de dégager davantage de bénéfices pour ses clients.
L'objectif de ce projet est de développer, optimiser et backtester un algorithme maximisant le profit et répondant au cachier des charges. 

<a id="competences"></a>
## Compétences acquises
- Déconstruire un problème
- Développer un algorithme pour résoudre un problème

<a id="techs"></a>
## Technologies Utilisées
- [Python3](https://www.python.org/)

<a id="reqs"></a>
## Requirements
- memory_profiler
- matplotlib

<a id="architecture"></a>
## Architecture et répertoires
```
Project
├── core
│   ├── aglorithms : package contenant les algorithmes développés
│   ├── backtesting_results.py
│   ├── model.py : module définissant les dataclass Action et Portfolio
│   ├── performance.py : module permettant de générer les analyses graphiques de résultats
│
├── ressources
│   ├── actions_data : analyses graphiques des résultats
│   ├── backtesting_data : données de backtesting
│
|── requirements.txt
|── documentation
```

<a id="localconfig"></a>
## Configuration locale
## Installation

### 1. Récupération du projet sur votre machine locale

Clonez le repository sur votre machine.

```bash
git clone https://github.com/GDSDC/OpenclassroomsProject-P7.git
```

Accédez au répertoire cloné.
```bash
cd OpenclassroomsProject-P7
```

### 2. Création d'un environnement virtuel 
Créez l'environnement virtuel env.
```bash
python3 -m venv env
```

### 3. Activation et installation de votre environnement virtuel 

Activez votre environnement virtuel env nouvellement créé.
```bash
source env/bin/activate
```

Installez les paquets présents dans la liste requirements.txt
```bash
pip install -r requirements.txt
```

## Utilisation _en ligne de commande_

Lancer simplement le script python `main.py` présent à la racine du dossier de travail en spécifiant le nom de l'algorithm (`bruteforce` ou `optimized`) ainsi que le chemin vers les données.
Le résultat s'affichera directement sur votre console/terminal.
```bash
python3 main.py <algorithm_name> <data_path>
```


<a id="presentation"></a>
### Présentation

[<img alt="presentation" width="480px" src="/assets/presentation.png">](https://docs.google.com/presentation/d/e/2PACX-1vQ89XWH8chN8sBkkz6afuFtUKT9sPhWTcg1P1KxslWi5el5Qk46tGFq0JOxs_1KFmUrn6_g8zQH4sbE/pub?start=true&loop=false&delayms=5000)
