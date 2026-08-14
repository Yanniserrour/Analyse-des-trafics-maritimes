#====================== IMPORT TIME ======================
import json
from collections import defaultdict
import math

#====================== FUNCTIONS =========================
def index(extended):
    """Crée un dictionnaire indexé par l'ID du bateau"""
    dict_extended = {}
    for bateau in extended:
        id_bateau = bateau[0]
        dict_extended[id_bateau] = bateau
    return dict_extended

def merge(extended, abbreviated):
    """Fusionne les données des deux fichiers"""
    result = {}
    for bateau in extended:
        id_bateau = bateau[0]
        nom = bateau[4]
        pays = bateau[5]
        position_ext = (bateau[1], bateau[2], bateau[3])
        result[id_bateau] = [nom, pays, position_ext, None]
    
    for bateau in abbreviated:
        id_bateau = bateau[0]
        position_abb = (bateau[1], bateau[2], bateau[3])
        if id_bateau in result:
            result[id_bateau][3] = position_abb
    return result

def openfolder(name_folder):
    """Ouvre un fichier JSON"""
    try:
        with open(name_folder, 'r', encoding="UTF-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier : {e}")
        return None

#=============================== MAIN =================================
data_extented = openfolder("./data/marin-e1-ext.json")  
data_abreviated = openfolder("./data/marin-e1-abb.json")

dict_extented = index(data_extented)
dict_abreviated = index(data_abreviated)

# =============================== MISSION 1 ===============================
print("\n" + "="*60)
print("MISSION 1 : EXPLORATION DES DONNEES")
print("="*60)

print(f"1. Nombre total de bateaux dans extended : {len(dict_extented)}")
print(f"2. Nombre total de bateaux dans abbreviated : {len(dict_abreviated)}")

print("\n3. Premier bateau de extended :")
print(f"   {data_extented[0]}")

print("\n4. Premier bateau de abbreviated :")
print(f"   {data_abreviated[0]}")

# =============================== MISSION 2 ===============================
print("\n" + "="*60)
print("MISSION 2 : STATISTIQUES DE BASE")
print("="*60)

# 1. Compter les pays
pays = defaultdict(int)
for bateau in data_extented:
    if bateau[5]:  # Ignorer les pays vides
        pays[bateau[5]] += 1

print(f"1. Nombre de pays différents : {len(pays)}")

# 2. Pays avec le plus de bateaux
big_pays, maxi = max(pays.items(), key=lambda x: x[1])
print(f"2. Pays avec le plus de bateaux : {big_pays} ({maxi} bateaux)")

# 3. Bateaux avec un nom
nombre_bateaux_nom = 0
for bateau in data_extented:
    if bateau[4]:
        nombre_bateaux_nom += 1
print(f"3. Bateaux avec un nom : {nombre_bateaux_nom} sur {len(data_extented)}")

# 4. Nom le plus long
big_nom = ""
longueur_max = 0
for bateau in data_extented:
    nom = bateau[4]
    if nom and len(nom) > longueur_max:
        big_nom = nom
        longueur_max = len(nom)
print(f"4. Nom le plus long : '{big_nom}' ({longueur_max} caractères)")

# =============================== MISSION 3 ===============================
print("\n" + "="*60)
print("MISSION 3 : EXTREMES GEOGRAPHIQUES")
print("="*60)

# 1. Le plus au Nord
bateau_nord = data_extented[0]
for bateau in data_extented:
    if bateau[1] > bateau_nord[1]:
        bateau_nord = bateau

print("\n=== BATEAU LE PLUS AU NORD ===")
print(f"Nom : {bateau_nord[4]}")
print(f"ID : {bateau_nord[0]}")
print(f"Latitude : {bateau_nord[1]}°")
print(f"Longitude : {bateau_nord[2]}°")
print(f"Date : {bateau_nord[3]}")
print(f"Pays : {bateau_nord[5]}")

# 2. Le plus au Sud
bateau_sud = data_extented[0]
for bateau in data_extented:
    if bateau[1] < bateau_sud[1]:
        bateau_sud = bateau

print("\n=== BATEAU LE PLUS AU SUD ===")
print(f"Nom : {bateau_sud[4]}")
print(f"ID : {bateau_sud[0]}")
print(f"Latitude : {bateau_sud[1]}°")
print(f"Longitude : {bateau_sud[2]}°")
print(f"Date : {bateau_sud[3]}")
print(f"Pays : {bateau_sud[5]}")

# 3. Le plus à l'Est
bateau_est = data_extented[0]
for bateau in data_extented:
    if bateau[2] > bateau_est[2]:
        bateau_est = bateau

print("\n=== BATEAU LE PLUS A L'EST ===") 
print(f"Nom : {bateau_est[4]}")
print(f"ID : {bateau_est[0]}")
print(f"Latitude : {bateau_est[1]}°")
print(f"Longitude : {bateau_est[2]}°")
print(f"Date : {bateau_est[3]}")
print(f"Pays : {bateau_est[5]}")

# 4. Le plus à l'Ouest
bateau_ouest = data_extented[0]
for bateau in data_extented:
    if bateau[2] < bateau_ouest[2]:
        bateau_ouest = bateau

print("\n=== BATEAU LE PLUS A L'OUEST ===") 
print(f"Nom : {bateau_ouest[4]}")
print(f"ID : {bateau_ouest[0]}")
print(f"Latitude : {bateau_ouest[1]}°")
print(f"Longitude : {bateau_ouest[2]}°")
print(f"Date : {bateau_ouest[3]}")
print(f"Pays : {bateau_ouest[5]}")

# =============================== MISSION 4 ===============================
print("\n" + "="*60)
print("MISSION 4 : ANALYSE TEMPORELLE")
print("="*60)

# 1. Date la plus ancienne
bateau_ancien = data_extented[0]
for bateau in data_extented:
    if bateau[3] < bateau_ancien[3]:
        bateau_ancien = bateau

print(f"\n1. Date la plus ancienne : {bateau_ancien[3]} (bateau : {bateau_ancien[4]})")

# 2. Date la plus récente
bateau_recent = data_extented[0]
for bateau in data_extented:
    if bateau[3] > bateau_recent[3]:
        bateau_recent = bateau

print(f"\n2. Date la plus récente : {bateau_recent[3]} (bateau : {bateau_recent[4]})")

# 3. Observations par heure
heurs = {}
for bateau in data_extented:
    dateheur = bateau[3]
    if dateheur:
        heur = int(dateheur[11:13])
        heurs[heur] = heurs.get(heur, 0) + 1

print("\n3. Observations par heure :")
for heure in sorted(heurs.keys()):
    print(f"   {heure:2d}h : {heurs[heure]} observations")

# 4. Heure la plus active
if heurs:
    heure_max = max(heurs, key=heurs.get)
    print(f"\n4. Heure la plus active : {heure_max}h ({heurs[heure_max]} observations)")

# =============================== MISSION 5 ===============================
print("\n" + "="*60)
print("MISSION 5 : FUSION ET ANALYSE COMBINÉE")
print("="*60)

# 1. Fusionner les données
dict_merged = merge(data_extented, data_abreviated)

# 2. Extraire les positions
positions = {}
for cle, liste in dict_merged.items():
    positions[cle] = [liste[2], liste[3]]

# 3. Calculer les distances
distances = {}
for cle, liste in positions.items():
    pos1 = liste[0]
    pos2 = liste[1]
    
    if pos1 and pos2:  # Vérifier que les deux positions existent
        lat1, long1, date1 = pos1
        lat2, long2, date2 = pos2
        
        dif_lat = lat1 - lat2
        dif_long = long1 - long2
        
        carre_lat = dif_lat ** 2
        carre_long = dif_long ** 2
        
        somme = carre_lat + carre_long
        distance = math.sqrt(somme)
        
        distances[cle] = {
            'nom': dict_merged[cle][0],
            'pays': dict_merged[cle][1],
            'pos1': pos1,
            'pos2': pos2,
            'distance': distance
        }

# 4. Trouver les extrêmes
if distances:
    id_max = max(distances, key=distances.get)
    id_min = min(distances, key=distances.get)
    
    print("\n=== PLUS GRANDE DISTANCE PARCOURUE ===")
    print(f"Bateau : {distances[id_max]['nom']}")
    print(f"ID : {id_max}")
    print(f"Pays : {distances[id_max]['pays']}")
    print(f"Distance : {distances[id_max]['distance']:.5f}°")
    
    print("\n=== PLUS PETITE DISTANCE PARCOURUE ===")
    print(f"Bateau : {distances[id_min]['nom']}")
    print(f"ID : {id_min}")
    print(f"Pays : {distances[id_min]['pays']}")
    print(f"Distance : {distances[id_min]['distance']:.5f}°")
    
    # Statistiques bonus
    valeurs = [d['distance'] for d in distances.values()]
    print("\n=== STATISTIQUES DES DISTANCES ===")
    print(f"Nombre de bateaux analysés : {len(distances)}")
    print(f"Distance moyenne : {sum(valeurs)/len(valeurs):.5f}°")
    print(f"Distance minimale : {min(valeurs):.5f}°")
    print(f"Distance maximale : {max(valeurs):.5f}°")

print("\n" + "="*60)
print("FIN DU PROJET")
print("="*60)