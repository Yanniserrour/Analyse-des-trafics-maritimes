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
        id_bateau = bateau[0] 
        nom = bateau[4] 
        pays = bateau[5]
        position_ext = (bateau[1], bateau[2], bateau[3])
        
        
        result[id_bateau] = [nom , pays, position_ext, None]
        
        
        
    for bateau in abbreviated : 
        id_bateau = bateau[0]
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

        
            
        
        
        
        
