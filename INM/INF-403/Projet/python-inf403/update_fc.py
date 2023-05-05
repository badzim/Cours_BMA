"""
    print("Produit                      (p)\n")
    print("Materiel                     (m)\n")
    print("dechet                       (d)\n")
    print("Processus                    (ps)\n")
    print("Contient                     (c)\n")
    print("TransformeEn                 (t)\n")
    print("Quitter l'application        (q)\n\n")
"""



def give_your_update(table):
    verif = "o"
    while verif == "o":
        if table == "p" :
            tab_ins = "Produit"
            print("Attribus:\n          id_produit     (INTEGER NOT NULL),\n          nom_produit     (TEXT NOT NULL),\n          description_produit      (TEXT NOT NULL),\n          id_processus_production         (INTEGER NOT NULL),\n          id_processus_reparation  (INTEGER NOT NULL) )")
            UPDATE = Aff_update(tab_ins)
        """
        elif table == "j" :
            tab_ins = "Joueurs"
            print(" Attribus:\n          nom_joueur    (VARCHAR(20) NOT NULL),\n          prenom_joueur (VARCHAR(20) NOT NULL),\n          num_joueur    (NUMBER(2)),\n          role_joueur   (VARCHAR(20) NOT NULL))")
            UPDATE = Aff_update(tab_ins)

        elif table == "m" :
            tab_ins = "Matchs"
            print(" Attribus:\n          date_match (DATE NOT NULL),\n          equipe1    (VARCHAR(20) NOT NULL),\n          equipe2    (VARCHAR(20) NOT NULL),\n          type_match (VARCHAR(20) NOT NULL))")
            UPDATE = Aff_update(tab_ins)

        elif table == "a" :
            tab_ins = "Acheteurs"
            print(" Attribus:\n          pseudo         (VARCHAR(20) NOT NULL),\n          date_naissance (DATE),\n          num_tel        (NUMBER(10)))")
            UPDATE = Aff_update(tab_ins)

        elif table == "p" :
            tab_ins = "Places"
            print(" Attribus:\n                      nump_place          NUMBER(5) NOT NULL,\n                      categorie           NUMBER(1) NOT NULL,\n")
            UPDATE = Aff_update(tab_ins)

        elif table == "x" :
            tab_ins = "TypesPlaces"
            print(" Attribus:\n                      categorie          NUMBER(1) NOT NULL,\n                      prix_place         NUMBER(3,2) NOT NULL,")
            UPDATE = Aff_update(tab_ins)
        
        elif table == "w" :
            tab_ins = "JoueurMatch"
            print(" Attribus:\n                    date_match         DATE NOT NULL,\n                    nom_joueur VARCHAR(20) NOT NULL,\n                    prenom_joueur  VARCHAR(20) NOT NULL,")
            UPDATE = Aff_update(tab_ins)

        """
        #vérification de la MaJ
        print("\n")
        verif = input(" Voulez-vous la modifiée?    (o/n)   :   ")
        while verif not in ("on") or verif == "":
            verif = input(" Voulez-vous la modifiée?    (o/n)   :   ")
            print()
    print("\n\n\n\n")
    return UPDATE

def Aff_update(tab_ins):
    UPDATE = "UPDATE "+tab_ins+" SET "
    print("Ecrivez la suite : \n   ",UPDATE,end='')
    UPDATE += input("")
    return UPDATE

def UPDA(conn, UPDATE):
    cur = conn.cursor()
    try:
        cur.execute(UPDATE)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("\n\n    La base de donnée a été mise à jour.\n\n\n\n")
    except:
        print(" Votre mise à jour n'est pas valide. L'imlémentation SQL est incorrect ou ne respect pas les contraintes.\n")