import os;
import graphviz;

def convertir_dot_en_image(chemin_dot, chemin_sortie):
    try:
        graphe = graphviz.Source.from_file(chemin_dot)
        graphe.render(chemin_sortie, format='png', cleanup=True)
        print(f"Image générée avec succès : {chemin_sortie}.png")
    except Exception as e:
        print(f"Erreur lors de la conversion de {chemin_dot} : {str(e)}")

def traiter_dossiers(dossier_racine):
    for dossier, sous_dossiers, fichiers in os.walk(dossier_racine):
        for fichier in fichiers:
            if fichier.endswith('.dot'):
                chemin_dot = os.path.join(dossier, fichier)
                dossier_relatif = os.path.relpath(dossier, dossier_racine)
                dossier_sortie = os.path.join('graphFiles', dossier_relatif)
                os.makedirs(dossier_sortie, exist_ok=True)
                nom_fichier_sans_extension = os.path.splitext(fichier)[0]
                chemin_sortie = os.path.join(dossier_sortie, nom_fichier_sans_extension)
                convertir_dot_en_image(chemin_dot, chemin_sortie)

# Utilisation de la fonction
dossier_racine = 'dotFiles'
traiter_dossiers(dossier_racine)
