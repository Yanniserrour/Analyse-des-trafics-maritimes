#====================== IMPORT TIME ======================
import json
from collections import defaultdict





#====================== FUNCTIONS =========================
def index (extended) : 
    """crée un dictionnaire indexé par l'ID du bateau"""
    
    dict_extented = {}
    
    for bateau in extended : #COST O(n)
        id = bateau[0]
        dict_extented[id] = bateau
        
    return dict_extented



def merge (extended, abbreviated) : 
    """fusionner les données des deux fichier pour les bateau en commun"""
    
    
    result = {}
    
    
    for bateau in extended : 
        id_bateau    = bateau[0] 
        nom          = bateau[4] 
        pays         = bateau[5]
        position_ext = (bateau[1], bateau[2], bateau[3])
        
        
        result[id_bateau] = [nom , pays, position_ext, None]
        
        
        
    for bateau in abbreviated : 
        id_bateau    = bateau[0]
        position_abb = (bateau[1], bateau[2], bateau[3])
        
        
        if id_bateau in result : 
            result[id_bateau][3] = position_abb
    
    
    return result 




def openfolder (name_folder) : 
    """
    Ouverture d'un fichier JSON
    """
    try : 
        with open (name_folder, 'r', encoding="UTF-8") as f : 
            data = json.load(f) 
        return data 
    except : 
        print("echec lors de l'ouverture du fichier") 
        return None
        
        
        
        
        
#=============================== MAIN =================================

data_extented   = openfolder("./data/marin-e1-ext.json")
data_abreviated = openfolder("./data/marin-e1-abb.json")

dict_extented = index(data_extented)
dict_abreviated = index(data_abreviated)

# I . MISSION 1

#1.le nombre total de bateaux dans extented 
print("\n")
print("le nombre total de bateau dans extented est : ", len(dict_extented))

#2.le nombre total de bateaux dans abreviated 
print("\n")
print("le nombre total de bateau dans abreviated est : ", len(dict_abreviated))

#3. les premiers bateaux de chaque un 
print("\n")
print("le premier bateau de extented est : ", data_extented[0])
print("\n")
print("le premier bateau de abreviated est : ", data_abreviated[0])

#4. afficher touts les colonnes différents pour ext et abb 




# II. MISSION 2 

#1. compter le nombre de pays différents 
pays = defaultdict(int)
for bateau in data_extented :
    pays[bateau[5]] +=1
print("les pays differents sont : ")
for p in pays.keys(): 
    print(p, end=',')
print("\n")
    
#2. torouver les pays avec le plus de bateaux
pays_items = pays.items()

maxi = 0
big_pays = ""
for p,q in pays_items : 
    if q> maxi : 
        maxi = q
        big_pays = p
print("le pays avec le plus de bateaux est : ", big_pays, " avec ", maxi, " bateaux")

big_pays, maxi = max(pays.items(), key = lambda x: x[1]) #<- retourne un tuple 
# et celui de la plus grande valeurs car le "pays.items()" returne une liste de tuple 
# et nous on s'interesse au nombre de ce tuple d'ou le "x[1]"

#3. compter les bateaux qui ont un nom
nombre_bateaux_nome = 0
for bateau in data_extented :
    if bateau [4]: 
        nombre_bateaux_nome += 1        
print("le nombre de bateaux qui ont un nom est : ", nombre_bateaux_nome)

   

        


    
    
    
    
    






    











        
            
        
        
        
        
