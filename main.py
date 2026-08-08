#====================== IMPORT TIME ======================
import json





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

data_extented   = openfolder("data/marin-e1-ext.json")
data_abreviated = openfolder("data/marin-e1-abb.json")

dict_extented = index(data_extented)
dict_abreviated = index(data_abreviated)

# I . MISSION 1

#1.le nombre total de bateaux dans extented 
print("le nombre total de bateau dans extented est : ", len(dict_extented))

#2.le nombre total de bateaux dans abreviated 
print("le nombre total de bateau dans abreviated est : ", len(dict_abreviated))

#3. les premiers bateaux de chaque un 
print("le premier bateau de extented est : ", data_extented[0])
print("le premier bateau de abreviated est : ", data_abreviated[0])

#4. afficher tout les noms des colonnes 
colonne_abreviated = []
for nom_colonne in dict_abreviated.keys() :  #<- cost : O(n)
    colonne_abreviated.append(nom_colonne)   
print("la colonnes de abreviated est : ",colonne_abreviated)

colonne_extented = []
for nom_colonne in dict_extented.keys() : #<- cost : O(n)
    colonne_extented.append(nom_colonne)
print("la colonne de extented est : ",colonne_extented)







    











        
            
        
        
        
        
