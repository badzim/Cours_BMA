from utils import db
db_file = "data/BDD_usine_Projet.db"
conn = db.creer_connexion(db_file)

#################################################################################################

"""
    print("Produit                      (p)\n")
    print("Materiel                     (m)\n")
    print("dechet                       (d)\n")
    print("Processus                    (ps)\n")
    print("Contient                     (c)\n")
    print("TransformeEn                 (t)\n")
    print("Quitter l'application        (q)\n\n")
"""

def choix_table(table):
    if table == "p":
        choix_req_prod()
    if table == "m":
        choix_req_mat()
    if table == "d":
        choix_req_dech()
    if table == "ps" :
        choix_req_proc()
    if table == "c":
        choix_req_cont()
    if table == "t":
        choix_req_trans()
    else:
        print("autre choix non gerer \n")



def choix_req_proc():
    #demande à l'utilisateur une lettre pour choisir la requête à effectuer
    print("Tous les processus disponible (a)\n")
    print("tout les processus de recyclage (b)\n")
    print("tout les processus de production (c)\n")
    print("tout les processus de reparation (d)\n")
    lettre = input("En attente d'une reponse : ")
    while lettre not in "abcd":
        lettre = input("Veuillez faire un choix correct : a, b, c, d:")
        print("")
    print("")
    #choix réalisé
    if lettre == "a" :
        select_tout_les_processus(conn)
    elif lettre == "b" :
        select_tout_les_processus_recyclage(conn)
    elif lettre == "c" :
        select_tout_les_processus_production(conn)
    elif lettre == "d" :
        select_tout_les_processus_reparation(conn)
    print("\n\n\n")

#Fonction SELECT / requête

def select_tout_les_processus(conn):#tous les joueurs
    cur = conn.cursor()
    cur.execute("SELECT * FROM Processus;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_tout_les_processus_recyclage(conn):#tous les joueurs
    cur = conn.cursor()
    cur.execute("SELECT * FROM Processus WHERE type_processus = 'recyclage';")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_tout_les_processus_production(conn):#tous les joueurs
    cur = conn.cursor()
    cur.execute("SELECT * FROM Processus WHERE type_processus = 'production';")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_tout_les_processus_reparation(conn):#tous les joueurs
    cur = conn.cursor()
    cur.execute("SELECT * FROM Processus WHERE type_processus = 'reparation';")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def choix_req_prod():
    #demande à l'utilisateur une lettre pour choisir la requête à effectuer
    print("Tous les produit disponible (a)\n")

    lettre = input("En attente d'une reponse : ")
    while lettre not in "a":
        lettre = input("Veuillez faire un choix correct : a:")
        print("")
    print("")
    #choix réalisé
    if lettre == "a" :
        select_tous_les_produit(conn)
    print("\n\n\n")


def select_tous_les_produit(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM produit;")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def choix_req_dech():
    #demande à l'utilisateur une lettre pour choisir la requête à effectuer
    print("Tous les dechet collecte (a)\n")
    
    lettre = input("En attente d'une reponse : ")
    while lettre not in "a":
        lettre = input("Veuillez faire un choix correct : a:")
        print("")
    print("")
    #choix réalisé
    if lettre == "a" :
        select_tout_les_dechet(conn)
    print("\n\n\n")

def select_tout_les_dechet(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Dechet;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def choix_req_mat():
    #demande à l'utilisateur une lettre pour choisir la requête à effectuer
    print("Tous le materiel disponible (a)\n")
    
    lettre = input("En attente d'une reponse : ")
    while lettre not in "a":
        lettre = input("Veuillez faire un choix correct : a:")
        print("")
    print("")
    #choix réalisé
    if lettre == "a" :
        select_tout_les_materiel(conn)
    print("\n\n\n")

def select_tout_les_materiel(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Materiel;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def choix_req_cont():
    #demande à l'utilisateur une lettre pour choisir la requête à effectuer
    print("Tous la table contenu (a)\n")
    
    lettre = input("En attente d'une reponse : ")
    while lettre not in "a":
        lettre = input("Veuillez faire un choix correct : a:")
        print("")
    print("")
    #choix réalisé
    if lettre == "a" :
        select_tout_contenu_produit(conn)
    print("\n\n\n")

def select_tout_contenu_produit(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Contient;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def choix_req_trans():
    #demande à l'utilisateur une lettre pour choisir la requête à effectuer
    print("Tous la table transforme (a)\n")
    
    lettre = input("En attente d'une reponse : ")
    while lettre not in "a":
        lettre = input("Veuillez faire un choix correct : a:")
        print("")
    print("")
    #choix réalisé
    if lettre == "a" :
        select_tout_transformation_materiel(conn)
    print("\n\n\n")
    
def select_tout_transformation_materiel(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM TransformeEn;")
    rows = cur.fetchall()
    for row in rows:
        print(row)