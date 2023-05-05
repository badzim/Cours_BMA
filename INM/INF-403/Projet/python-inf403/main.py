#!/usr/bin/python3

import os
from utils import db
import NavigationEtMenu
import select_fc
import insert_fc
import update_fc
import delete_fc

def main():


    # Nom de la BD à créer
    
    db_file = "data/BDD_usine_Projet.db"

    # Créer une connexion a la BD
    print("creation de la base de donne %s", db_file)
    conn = db.creer_connexion(db_file)
    print("creation avec success \n")

    # Remplir la BD
    #print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    
    db.mise_a_jour_bd(conn, "./data/usine_creation.sql")
    db.mise_a_jour_bd(conn, "data/usine_inserts_ok.sql")

    
    
    #début app
    i = 1
    stade = r"""                                     
    ##  ##    ####    ######   ##  ##   ######  
    ##  ##   ##         ##     ### ##   ##      
    ##  ##    ####      ##     ######   #####   
    ##  ##       ##     ##     ######   ##      
    ##  ##       ##     ##     ## ###   ##      
    ######    ####    ######   ##  ##   ######  
    """
    NavigationEtMenu.Aff_dynamique(stade)
    navigation = 0
    while navigation == 0:                              #menu / choix de la table OU insertion
        table = NavigationEtMenu.menu()
        navigation = NavigationEtMenu.quitte(table,navigation)
        navigation = NavigationEtMenu.si_i_u(table, navigation)
        while navigation == 1:#_____________________________________________SELECT_____________________________________________
            table = NavigationEtMenu.choix_table()
            navigation = NavigationEtMenu.quitte(table,navigation)
            while navigation == 2:                             #choix requête
                select_fc.choix_table(table)
                navigation = NavigationEtMenu.Ask(navigation)
        
    
        while navigation == 11:#_____________________________________________INSERT_____________________________________________
            table = NavigationEtMenu.choix_table() 
            navigation = NavigationEtMenu.quitte(table,navigation)
            while navigation == 12:                             #choix requête
                INSERTION = insert_fc.give_your_insert(table)  #récupère la commande insert à appliquer
                insert_fc.INSERT(conn, INSERTION)
                conn.commit()
                navigation = NavigationEtMenu.Ask(navigation)
    
        while navigation == 21:#_____________________________________________UPDATE_____________________________________________
            table = NavigationEtMenu.choix_table() 
            navigation = NavigationEtMenu.quitte(table,navigation)
            while navigation == 22:
                UPDATE = update_fc.give_your_update(table)  
                update_fc.UPDA(conn, UPDATE)
                conn.commit()
                navigation = NavigationEtMenu.Ask(navigation)
        
        while navigation == 31:#_____________________________________________DELETE_____________________________________________
            table = NavigationEtMenu.choix_table()
            navigation = NavigationEtMenu.quitte(table,navigation)
            while navigation == 32:                             #choix suppression
                DELETE = delete_fc.give_your_delete(table)  #récupère la commande delete à appliquer
                delete_fc.DELE(conn, DELETE)
                conn.commit()
                navigation = NavigationEtMenu.Ask(navigation)
        

if __name__ == "__main__":
    if os.path.exists("./data/BDD_usine_Projet.db"):
        os.remove("./data/BDD_usine_Projet.db")
    main()
