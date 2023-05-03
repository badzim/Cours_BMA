#!/usr/bin/python3

from utils import db


def select_tous_les_bateaux(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Bateaux
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)



def select_tous_les_adherents(conn, condition = "0"):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    if condition == "0":
        cur.execute("""
                    SELECT * 
                    FROM Adherents
                    """)
    else:
        cur.execute(f"""
                    SELECT * 
                    FROM Adherents
                    WHERE {condition}
                    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)




def main():
    # Nom de la BD à créer
    db_file = "data/voile.db"

    # Créer une connexion a la BD
    print("creation de la base de donne %s", db_file)
    conn = db.creer_connexion(db_file)

    # Remplir la BD

    # Creation des tables
    script = "data/voile_creation.sql"
    print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, script)

    # Insertion des données
    script = "data/voile_inserts_ok.sql"
    print("appel au script ")
    db.mise_a_jour_bd(conn, script)

    # Lire la BD
    print("2. Liste de tous les bateaux")
    select_tous_les_bateaux(conn)

    print("3. Liste de tous les adherents")
    condition = str(input("saisir condition : "))
    select_tous_les_adherents(conn, condition)


if __name__ == "__main__":
    main()
