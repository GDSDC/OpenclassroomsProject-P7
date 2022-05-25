# Openclassrooms Project-P7

OpenClassRooms Project-P7 est un projet Python ayant un but d'apprentissage dans le cadre de la formation OpenClassRooms Développeur d'Application Python.

Thème du projet : Résolvez des problèmes en utilisant des algorithmes en Python.

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

Lancer simplement le script python **_main.py_** présent à la racine du dossier de travail en spécifiant le nom de l'algorithm (_**bruteforce**_ ou _**optimized**_) ainsi que le chemin vers les données.
Le résultat s'affichera directement sur votre console/terminal.
```python
python3 main.py algorithm_name data_path
```

