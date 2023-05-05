
import time
#Fonction menu/départ et fonction générale

def menu():
    print(r"""                             
        #    # ###### #    # #    # 
        ##  ## #      ##   # #    # 
        # ## # #####  # #  # #    # 
        #    # #      #  # # #    # 
        #    # #      #   ## #    # 
        #    # ###### #    #  ####  
        
        """)
    print("Insertion                    (i)\n")
    print("Mise à jour                  (m)\n")
    print("Voir les tables              (t)\n")
    print("Suppression de ligne         (s)\n")
    print("Quitter l'application        (q)\n\n")
    lettre = input("En attente d'une reponse : ")
    while lettre not in "imtsq" or lettre == "":
        lettre = input("Veuillez faire un choix correct : i, m, t, s ou q    :")
        print("")
    print("\n\n\n")
    return lettre

def Aff_dynamique(phrase):
    for elm in phrase:
        print(elm,end="")
        time.sleep(0.005)

#questions/conditions pour la navigation dans les menus

def Ask(navigation):
    print("  Retourner au menu               (m)")
    print("  Retourner au choix des tables   (t)")
    print("  Retourner au choix précédent    (r)")
    print("  Quitter l'application           (q)\n")
    choix = input("En attente d'une reponse :")
    while choix not in "mtrq" or choix == "":
        choix = input("Veuillez faire un choix correct : m, t, r ou q    :")
    if choix == "m":
        navigation = 0
    if choix == "t":
        navigation -= 1
    elif choix == "q":

        navigation = -1
    print("\n\n\n")
    return navigation

def choix_table():
    print("Produit                      (p)\n")
    print("Materiel                     (m)\n")
    print("dechet                       (d)\n")
    print("Processus                    (ps)\n")
    print("Contient                     (c)\n")
    print("TransformeEn                 (t)\n")
    print("Quitter l'application        (q)\n\n")
    lettre = input("En attente d'une reponse : ")
    while lettre not in "pmdpsctq" or lettre == "":
        lettre = input("Veuillez faire un choix correct : p, m, d, ps, c, t, ou q    :")
        print("")
    print("\n\n\n")
    return lettre

def quitte(table,navigation):
    if table == "q":
        navigation = -1
    else:
        navigation += 1
    return navigation


# entré dans le choix insertion ou mise a jour d'une donnée

def si_i_u(table, navigation):
    if table == "i" :
        navigation = 11
    elif table == "m":
        navigation = 21
    elif table == "s":
        navigation = 31
    return navigation