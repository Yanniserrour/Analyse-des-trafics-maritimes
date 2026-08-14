# 🚢 MarineTraffic Data Analysis

## 📋 Description du projet

Ce projet analyse des données de positionnement de bateaux issues de l'API MarineTraffic. Il manipule des fichiers JSON contenant des observations de bateaux en mer, avec leurs coordonnées géographiques et leurs horodatages.

### Objectifs
- Charger et explorer des données maritimes
- Analyser les positions géographiques des bateaux
- Étudier les tendances temporelles
- Mesurer les déplacements entre deux observations

---

## 📁 Structure du projet
projet/
├── data/
│ ├── marine-e1-ext.json # Données étendues
│ └── marine-e1-abb.json # Données abrégées
├── main.py # Code principal
└── README.md # Ce fichier


---

## 🛠️ Technologies utilisées

- **Python 3**
- **Modules :**
  - `json` : Lecture des fichiers JSON
  - `math` : Calculs mathématiques (racine carrée)
  - `collections.defaultdict` : Comptage simplifié

---

## 📊 Fonctionnalités implémentées

### 1️⃣ Exploration des données
- Affichage du nombre total de bateaux
- Visualisation de la structure des données
- Identification des colonnes

### 2️⃣ Statistiques de base
- Nombre de pays différents
- Pays avec le plus de bateaux
- Bateaux avec un nom
- Nom de bateau le plus long

### 3️⃣ Extremes géographiques
- Bateau le plus au **Nord**
- Bateau le plus au **Sud**
- Bateau le plus à l'**Est**
- Bateau le plus à l'**Ouest**

### 4️⃣ Analyse temporelle
- Date la plus ancienne
- Date la plus récente
- Observations par heure
- Heure la plus active

### 5️⃣ Fusion et analyse combinée
- Fusion des données étendues et abrégées
- Calcul des distances parcourues
- Bateau avec le plus grand déplacement
- Bateau avec le plus petit déplacement
- Statistiques des distances

---
