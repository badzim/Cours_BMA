DROP TABLE IF EXISTS Produit;
DROP TABLE IF EXISTS Materiel;
DROP TABLE IF EXISTS Dechet;

DROP TABLE IF EXISTS Processus;


DROP TABLE IF EXISTS Contient;
DROP TABLE IF EXISTS TransformeEn;

/* Produit(id_produit {id}, nom_produit, description_produit) */

/* Contraintes d'intégrité référentielles : */

/* contient[id_produit] = Produit[id_produit]  */
/* transforme_en[id_matériel] ⊆ Matériel[id_matériel] */
/* est_contenue_dans[id_produit] ⊆ Produit[id_produit]*/
/* est_transformé_en[id_déchet] ⊆ Déchet[id_déchet]*/
/*est_recyclé_par[id_processus_recyclage] ⊆ ProcessusRecyclage[id_processus_recyclage]*/
/*utilise[id_produit] ⊆ Produit[id_produit]*/
/*utilise_[id_déchet] ⊆ Déchet[id_déchet]*/
/*est_réparé_par[id_processus_reparation] ⊆ ProcessusReparation[id_processus_reparation]*/



CREATE TABLE Produit (
   id_produit INTEGER PRIMARY KEY NOT NULL,
   nom_produit TEXT NOT NULL,
   description_produit TEXT,

   /* contraint unicite */
   /* contraint integrite referenciel */

   CONSTRAINT CK_Mod_c0 CHECK (longueur_modele > 0)
);


/* Materiel(id_materiel {id}, nom_materiel, description_materiel, proriete_physique, propriete_chimique) */

CREATE TABLE Materiel (
   id_materiel TEXT PRIMARY KEY NOT NULL,
   nom_materiel TEXT NOT NULL,
   description_materiel TEXT PRIMARY KEY,
   proriete_physique TEXT,
   propriete_chimique TEXT,

   /* contraint unicite */
   /* contraint integrite referenciel */

   CONSTRAINT CK_TEmp_c0 CHECK (longueur_max_type_emplacement > 0),
   CONSTRAINT CK_TEmp_c1 CHECK (prix_type_emplacement > 0),
   CONSTRAINT CK_TEmp_c2 CHECK (
       taille_type_emplacement = 'petit' AND longueur_max_type_emplacement =7 OR
       taille_type_emplacement = 'moyen' AND longueur_max_type_emplacement =12 OR 
       taille_type_emplacement = 'grand' AND longueur_max_type_emplacement =20)
);


/* Dechet(id_dechet {id}, nom_dechet, description_dechet, lieuCollect) */
CREATE TABLE Dechet (
   id_dechet INTEGER PRIMARY KEY,
   nom_dechet TEXT,
   description_dechet TEXT,
   lieuCollect TEXT,

   /* contraint unicite */
   /* contraint integrite referenciel */

   CONSTRAINT FK_Emp_c0 FOREIGN KEY (taille_type_emplacement) 
   REFERENCES TypesEmplacements(taille_type_emplacement),
   CONSTRAINT CK_Emp_c1 CHECK (numero_emplacement > 0)
);



/* Processus(id_processus {id}, nom_processus, description_processus, cout_processus, temps_processus, type_processus) */
CREATE TABLE Processus (
   id_production INTEGER PRIMARY KEY,
   nom_production TEXT,
   description_production TEXT,
   cout_processus REAL,
   temps_processus TEXT,
   type_processus TEXT,


   /* contraint unicite */
   /* contraint integrite referenciel */


   /* contraint validation */
   CONSTRAINT CK_TYPE_c0 CHECK (
        type_processus = 'production' OR
        type_processus = 'reparation'  OR 
        type_processus = 'recyclage' )
);



/* Contient((id_produit, id_materiel) {id}) */
/*  */
CREATE TABLE Contient (
   id_processus INTEGER,
   id_produit INTEGER,

   /* contraint unicite */
   /* contraint integrite referenciel */
   CONSTRAINT CK_Adh_c0 CHECK (numero_adherent > 0)
);

/* ProcessusRecyclage((id_materiel, id_dechet) {id}) */
CREATE TABLE TransformeEn (
   id_processus INTEGER,
   id_materiel INTEGER,


   /* contraint unicite */
   /* contraint integrite referenciel */

   );