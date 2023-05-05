#   fn insertion au clavier
#   tab_ins = nom de la table à modifier
#   nb_att = nombre d'attribu à entrer
#   INSERTION = ligne sql à executer prochainement


"""
    print("Produit                      (p)\n")
    print("Materiel                     (m)\n")
    print("dechet                       (d)\n")
    print("Processus                    (ps)\n")
    print("Contient                     (c)\n")
    print("TransformeEn                 (t)\n")
    print("Quitter l'application        (q)\n\n")
"""


def give_your_insert(table):
    verif = "o"
    while verif == "o":
        liste_att = []
        liste_val = []
        if table == "p" :
            # Produit(id_produit {id}, nom_produit, description_produit, id_processus_production, id_processus_reparation)

            nb_att = 5
            liste_att.append("id_produit")
            liste_att.append("nom_produit")
            liste_att.append("description_produit")
            liste_att.append("id_processus_production")
            liste_att.append("id_processus_reparation")
            tab_ins = "Produit"
            INSERTION = "INSERT INTO "+tab_ins+" VALUES(\n          id_produit     (INTEGER NOT NULL),\n          nom_produit     (TEXT NOT NULL),\n          description_produit      (TEXT NOT NULL),\n          id_processus_production         (INTEGER NOT NULL),\n          id_processus_reparation  (INTEGER NOT NULL) )"
            Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION)
            INSERTION = Composition_Ins(liste_val,tab_ins,nb_att)
        """
        elif table == "j" :
            nb_att = 4
            liste_att.append("nom_joueur")
            liste_att.append("prenom_joueur")
            liste_att.append("num_joueur")
            liste_att.append("role_joueur")
            tab_ins = "Joueurs"
            INSERTION = "INSERT INTO "+tab_ins+" VALUES(\n          nom_joueur    (VARCHAR(20) NOT NULL),\n          prenom_joueur (VARCHAR(20) NOT NULL),\n          num_joueur    (NUMBER(2)),\n          role_joueur   (VARCHAR(20) NOT NULL))"
            Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION)
            INSERTION = Composition_Ins(liste_val,tab_ins,nb_att)

        elif table == "m" :
            nb_att = 5
            liste_att.append("date_match")
            liste_att.append("equipe1")
            liste_att.append("equipe2")
            liste_att.append("type_match")
            liste_att.append("mult")
            tab_ins = "Matchs"
            INSERTION = "INSERT INTO "+tab_ins+" VALUES(\n          date_match       (DATE NOT NULL),\n          equipe1          (VARCHAR(20) NOT NULL),\n          equipe2          (VARCHAR(20) NOT NULL),\n          type_match       (VARCHAR(20) NOT NULL),\n          multiplicateur   (NUMBER(1,1) NOT NULL))"
            Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION)
            INSERTION = Composition_Ins(liste_val,tab_ins,nb_att)
            
        elif table == "a" :
            nb_att = 3
            liste_att.append("pseudo")
            liste_att.append("date_naissance")
            liste_att.append("num_tel")
            tab_ins = "Acheteurs"
            INSERTION = "INSERT INTO "+tab_ins+" VALUES(\n          pseudo         (VARCHAR(20) NOT NULL),\n          date_naissance (DATE),\n          num_tel        (NUMBER(10)))"
            Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION)
            INSERTION = Composition_Ins(liste_val,tab_ins,nb_att)
        
        elif table == "p" :#place
            nb_att = 2
            liste_att.append("num_place")
            liste_att.append("categorie")
            tab_ins = "Places"
            INSERTION = "INSERT INTO "+tab_ins+" VALUES(\n                      num_place    (NUMBER(3,2) NOT NULL),\n                      categorie    (VARCHAR(1) NOT NULL))"
            Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION)
            INSERTION = Composition_Ins(liste_val,tab_ins,nb_att)
        
        elif table == "x" :#type_place
            nb_att = 2
            liste_att.append("categorie")
            liste_att.append("prix_place")
            tab_ins = "TypePlaces"
            INSERTION = "INSERT INTO "+tab_ins+" VALUES(\n                      categorie    (VARCHAR(20) NOT NULL),\n                      prix_place   (VARCHAR(20) NOT NULL))"
            Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION)
            INSERTION = Composition_Ins(liste_val,tab_ins,nb_att)

        elif table == "w" :#joueurmatch
            nb_att = 3
            liste_att.append("date_match")
            liste_att.append("nom_joueur")
            liste_att.append("prenom_joueur")
            tab_ins = "JoueursMatchs"
            INSERTION = "INSERT INTO "+tab_ins+" VALUES(\n                      date_match     (NUMBER(2)\n                      nom_joueur     (VARCHAR(20) NOT NULL),\n                      prenom_joueur  (VARCHAR(20) NOT NULL))"
            Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION)
            INSERTION = Composition_Ins(liste_val,tab_ins,nb_att)
        """
        #vérification de l'insertion
        print()
        print(" Votre insertion est : ",INSERTION)
        print("\n")
        verif = input(" Voulez-vous la modifiée?    (o/n)   :   ")
        while verif not in ("on"):
            verif = input(" Voulez-vous la modifiée?    (o/n)   :   ")
            print()
    print("\n\n\n\n")
    return INSERTION

def Aff_insert(liste_att,liste_val, nb_att, tab_ins, INSERTION):
    print(" Veuillez remplir votre insertion pour la table",tab_ins,"   :\n")
    print(INSERTION,"\n")
    i = 0
    j = 0
    isfloat = False
    boo = True

    non_null_param = ["id_produit", "id_processus", "id_processus_production", "id_processus_reparation", "id_materiel", "nom_materiel"]
    integer_param = ["cout_processus", "temps_processus"]
    type_proc = ['production', 'reparation' , 'recyclage']
    while i < nb_att:
        print(" Donnez la valeur",liste_att[i],"    :   ")
        val = input()
        while ((liste_att[i] in non_null_param) and (val == 'NULL')):  #vérification que se soit un pas NULL
            val = input("\nLa valeur de l'attribu entrée ne peut pas être NULL : ")
        while ((liste_att[i] in integer_param)) and not(val.isdigit()):  #vérification que se soit un chiffre
            val = input("\nLa valeur entrée doit être un chiffre > 0 : ")
        while liste_att[i] == "type_processus" and (val not in type_proc):
            val = input("\nLa valeur entrée ne respect pas la contrainte: att = 1 ou 2 ou 3 ou 4\n\n")
        """    
        while not(isfloat) and liste_att[i] == "mult":
            if len(val)!=3:
                val = input("Entrez votre flottant avec un seul chiffre avant et après la virgule  :  ")
                print("\n")
            else:
                try:
                    isfloat = int(val[0]) >= 0 and val[1] == "." and int(val[2]) >= 0
                except:
                    print("\n   Format accepter : 0 <= float < 10\n\n")
                    isfloat = False
                    val = input("Entrez votre flottant avec un seul chiffre avant et après la virgule  :  ")
                    print("\n")
        
        while liste_att[i] == "role_joueur" and (val != 'attaquant' and val != 'milieu' and val != 'defenseur' and val != 'gardien'):
            val = input("\nLa valeur entrée ne respect pas la contrainte: att = attaquant ou milieu ou defenseur ou gardien\n\n")
        while liste_att[i] == "date_match" and j < len(val) and boo:
            while liste_att[i] == "date_match" and len(val)!=10:
                val = input("\nLa valeur entrée ne respect pas la contrainte: att = date (mm/dd/yyyy ou mm-dd-yyyy)\n\n")
            boo = True
            if j == 0 and boo: # mois
                boo = val[j].isdigit() and val[j+1].isdigit()
                if boo:
                    ens = calcul_jour_mois(val[j],val[j+1])
                    if ens % 2 != 0 and ens < 8:
                        mois = "impair"
                    elif ens % 2 == 0 and ens < 8 and ens != 2:
                        mois = "pair"
                    elif ens == 2:
                        mois = "fevrier"
                    elif ens % 2 != 0 and ens >= 8:
                        mois = "pair"
                    elif ens % 2 == 0 and ens >= 8:
                        mois = "impair"
                    boo =  1 <= ens and ens <= 12
                    if boo:
                        j+=2       
            if j == 3 and boo: # jour
                boo = val[j].isdigit() and val[j+1].isdigit()
                if boo:
                    jou = calcul_jour_mois(val[j], val[j+1])
                    if mois == "impair":
                        boo = 1 <= jou <= 31
                        j+=2  
                    elif mois == "fevrier":
                        boo = 1 <= jou <= 28
                        j+=2  
                    else:
                        boo = 1 <= jou <= 30
                        if boo:
                            j+=2        
            if j == 6 and boo: # année
                boo = val[j].isdigit() and val[j+1].isdigit() and val[j+2].isdigit() and val[j+3].isdigit()
                if boo:                    
                    j += 4    
            elif (j == 2 or j == 5) and boo:
                boo = val[j] == '/' or val[j] == '-'
                if boo:
                    j += 1
            if not(boo):
                val = input("\nLa valeur entrée ne respect pas la contrainte: att = date (mm/dd/yyyy ou mm-dd-yyyy)\n\n")
                boo = True
                j = 0
        """
        liste_val.append(val)
        print()
        i += 1

def Composition_Ins(liste_val,tab_ins,nb_att):
    i = 0
    ins = "INSERT INTO "+tab_ins+" VALUES ("           #composition de l'insertion
    """
    if tab_ins == "Matchs":
        while i < nb_att-1:
            if liste_val[i].isdigit():
                ins += liste_val[i]+","
            else:
                ins += "'"+liste_val[i]+"'"+","
            i += 1
        ins += liste_val[nb_att-1]+");"
    """
    while i < nb_att-1:
        if liste_val[i].isdigit():
            ins += liste_val[i]+","
        else:
            ins += "'"+liste_val[i]+"'"+","
        i += 1
    ins += liste_val[nb_att-1] +");"
    return ins


# Fonction INSERT

def INSERT(conn,INSERTION):
    cur = conn.cursor()
    try:
        cur.execute(INSERTION)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("\n\n    La base de donnée a été mise à jour.\n\n\n\n")
    except:
        print(" Vous ne respectez pas les constraintes d'intégrité entre les tables.\n")