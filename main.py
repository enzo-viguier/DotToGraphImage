import os
import graphviz
import subprocess
import sys

def verifier_installations():
    with open('requirement.txt', 'r') as fichier:
        packages = fichier.read().splitlines()
    
    packages_manquants = []
    
    for package in packages:
        try:
            __import__(package.split('==')[0])
        except ImportError:
            packages_manquants.append(package)
    
    if packages_manquants:
        print("Les packages suivants ne sont pas installés :")
        for package in packages_manquants:
            print(f"- {package}")
        
        reponse = input("Voulez-vous les installer maintenant ? (o/n) : ")
        if reponse.lower() == 'o':
            for package in packages_manquants:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print("Tous les packages ont été installés avec succès.")
        else:
            print("Veuillez installer les packages manquants manuellement.")
    else:
        print("Tous les packages requis sont déjà installés.")


def convertir_dot_en_image(chemin_dot, chemin_sortie):
    try:
        graphe = graphviz.Source.from_file(chemin_dot)
        graphe.render(chemin_sortie, format='png', cleanup=True)
        print(f"Image générée avec succès : {chemin_sortie}.png")
    except Exception as e:
        print(f"Erreur lors de la conversion de {chemin_dot} : {str(e)}")

def traiter_dossiers_cfg(dossier_racine):
    dossier_cfg = os.path.join(dossier_racine, 'ControlFlowGraph')
    for dossier, sous_dossiers, fichiers in os.walk(dossier_cfg):
        for fichier in fichiers:
            if fichier.endswith('.dot'):
                chemin_dot = os.path.join(dossier, fichier)
                dossier_relatif = os.path.relpath(dossier, dossier_cfg)
                dossier_sortie = os.path.join('graphFiles', 'ControlFlowGraph', dossier_relatif)
                os.makedirs(dossier_sortie, exist_ok=True)
                nom_fichier_sans_extension = os.path.splitext(fichier)[0]
                chemin_sortie = os.path.join(dossier_sortie, nom_fichier_sans_extension)
                convertir_dot_en_image(chemin_dot, chemin_sortie)
                
                
def traiter_dossiers_cg(dossier_racine):
    dossier_cg = os.path.join(dossier_racine, 'CallGraph')
    for dossier, sous_dossiers, fichiers in os.walk(dossier_cg):
        for fichier in fichiers:
            if fichier.endswith('.dot'):
                chemin_dot = os.path.join(dossier, fichier)
                dossier_relatif = os.path.relpath(dossier, dossier_cg)
                dossier_sortie = os.path.join('graphFiles', 'CallGraph', dossier_relatif)
                os.makedirs(dossier_sortie, exist_ok=True)
                nom_fichier_sans_extension = os.path.splitext(fichier)[0]
                chemin_sortie = os.path.join(dossier_sortie, nom_fichier_sans_extension)
                convertir_dot_en_image(chemin_dot, chemin_sortie)


def main():
    # verifier les installations des packages
    verifier_installations()

    # Utilisation de la fonction
    dossier_racine = 'dotFiles'
    
    print("Que souhaitez-vous générer ?")
    print("1. Uniquement les images Control Flow Graph")
    print("2. Uniquement les images Call Graph")
    print("3. Les deux types d'images")
    
    choix = input("Entrez votre choix (1, 2 ou 3) : ")
    
    if choix == '1':
        print("============================================")
        print("Control Flow Graph")
        print("============================================")
        traiter_dossiers_cfg(dossier_racine)
    elif choix == '2':
        print("============================================")
        print("Call Graph")
        print("============================================")
        traiter_dossiers_cg(dossier_racine)
    elif choix == '3':
        print("============================================")
        print("Control Flow Graph")
        print("============================================")
        traiter_dossiers_cfg(dossier_racine)
        print("============================================")
        print("Call Graph")
        print("============================================")
        traiter_dossiers_cg(dossier_racine)
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

if __name__ == "__main__":
    main()