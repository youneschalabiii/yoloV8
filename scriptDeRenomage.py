import os

def rename_files(directory_path, old_part, new_part):
    """
    Renomme les fichiers dans le répertoire spécifié en remplaçant 'old_part' par 'new_part' dans les noms de fichiers.
    
    Args:
        directory_path (str): Chemin du répertoire contenant les fichiers.
        old_part (str): Partie du nom de fichier à remplacer.
        new_part (str): Nouvelle partie du nom de fichier pour le remplacement.
    """
    # Vérifier si le chemin est un répertoire
    if not os.path.isdir(directory_path):
        print(f"Erreur: {directory_path} n'est pas un répertoire valide.")
        return
    
    # Parcourir tous les fichiers du répertoire
    for filename in os.listdir(directory_path):
        # Chemin complet du fichier
        filepath = os.path.join(directory_path, filename)
        
        # Vérifier si le chemin est un fichier
        if os.path.isfile(filepath):
            # Remplacer la partie du nom du fichier
            new_filename = filename.replace(old_part, new_part)
            
            # Chemin du nouveau nom de fichier
            new_filepath = os.path.join(directory_path, new_filename)
            
            # Renommer le fichier
            os.rename(filepath, new_filepath)
            
            print(f"Renommage: {filename} -> {new_filename}")

# Exemple d'utilisation
directory = r'C:\Users\nsc\Documents\yoloV8\data\labels\val' 
old_part = '_lesion'
new_part = ''

rename_files(directory, old_part, new_part)
