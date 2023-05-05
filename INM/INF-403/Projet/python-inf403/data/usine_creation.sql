

DROP TABLE IF EXISTS Produit;
DROP TABLE IF EXISTS Materiel;
DROP TABLE IF EXISTS Dechet;

DROP TABLE IF EXISTS Contient;
DROP TABLE IF EXISTS TransformeEn;
DROP TABLE IF EXISTS Processus;

/* Processus(id_processus {id}, nom_processus, description_processus, cout_processus, temps_processus, type_processus) */
CREATE TABLE Processus (
   id_processus INTEGER PRIMARY KEY,
   nom_production TEXT,
   description_production TEXT,
   cout_processus REAL,
   temps_processus TEXT,
   type_processus TEXT,

   /* contraint integrite referenciel */
   /* contraint validation */
   CONSTRAINT CK_TYPE_c0 CHECK ( type_processus = 'production' OR type_processus = 'reparation'  OR  type_processus = 'recyclage' ),
   CONSTRAINT val_Proc_c0 CHECK (cout_processus > 0),
   CONSTRAINT val_Proc_c1 CHECK (temps_processus > 0),
   CONSTRAINT val_Proc_c2 CHECK (id_processus NOT NULL)
);

-- Produit(id_produit {id}, nom_produit, description_produit, id_processus_production, id_processus_reparation)

CREATE TABLE Produit (
   id_produit INTEGER PRIMARY KEY NOT NULL,
   nom_produit VARCHAR(10) NOT NULL,
   description_produit VARCHAR (20),
   id_processus_production INTEGER NOT NULL,
   id_processus_reparation INTEGER NOT NULL,
   CONSTRAINT CK_Prod_c0 FOREIGN KEY (id_processus_production)
   REFERENCES Processus(id_processus),
   CONSTRAINT CK_Prod_c1 FOREIGN KEY (id_processus_reparation)
   REFERENCES Processus(id_processus)
);

CREATE TRIGGER tri_Dec_t0
BEFORE INSERT ON Produit
FOR EACH ROW
WHEN NEW.id_processus_production NOT IN (SELECT id_processus FROM Processus WHERE type_processus = 'production')
BEGIN
SELECT RAISE( ABORT, 'Invalid id_processus_production'); END;

CREATE TRIGGER tri_Dec_t1
BEFORE INSERT ON Produit
FOR EACH ROW
WHEN NEW.id_processus_reparation NOT IN (SELECT id_processus FROM Processus WHERE type_processus = 'reparation')
BEGIN
SELECT RAISE(ABORT, 'Invalid id_processus_reparation'); END;

-- Materiel(id_materiel {id}, nom_materiel, description_materiel, proriete_physique, propriete_chimique, id_processus_recyclage) 

CREATE TABLE Materiel (
   id_materiel INTEGER PRIMARY KEY NOT NULL,
   nom_materiel TEXT NOT NULL,
   description_materiel TEXT,
   proriete_physique TEXT,
   propriete_chimique TEXT,
   id_processus_recyclage INTEGER NOT NULL,
   -- contraint integrite referenciel
   CONSTRAINT fk_Mat_c0 FOREIGN KEY (id_processus_recyclage)
   REFERENCES Processus(id_processus) 
);


CREATE TRIGGER tri_Dec_t2
BEFORE INSERT ON Materiel
FOR EACH ROW
WHEN NEW.id_processus_recyclage NOT IN (SELECT id_processus FROM Processus WHERE type_processus = 'recyclage')
BEGIN
SELECT RAISE(ABORT, 'Invalid id_processus_recyclage'); END;
-- Dechet(id_dechet {id}, nom_dechet, description_dechet, lieuCollect, id_processus_production) 
 
-- contraint integrite referenciel (Foreign Key) 
-- Dechet[id_processus_production] = Processus[id_processus]  




CREATE TABLE Dechet (
   id_dechet INTEGER PRIMARY KEY,
   nom_dechet TEXT,
   description_dechet TEXT,
   lieuCollect TEXT,
   id_processus_production INTEGER,

    -- contraint integrite referenciel
   CONSTRAINT FK_Dec_c0 FOREIGN KEY (id_processus_production) 
   REFERENCES Processus(id_processus) 
);



CREATE TRIGGER tri_Dec_t3
BEFORE INSERT ON Dechet
FOR EACH ROW
WHEN NEW.id_processus_production NOT IN (SELECT id_processus FROM Processus WHERE type_processus = 'production')
BEGIN
SELECT RAISE(ABORT, 'Invalid id_processus_production'); END;
-- Contient((id_produit, id_materiel) {id}) 
-- contraint integrite referenciel (Foreign Key) 
-- contient[id_produit] = Produit[id_produit]  
-- contient[id_materiel] = Materiel[id_materiel]  

CREATE TABLE Contient (
   id_produit INTEGER,
   id_materiel INTEGER,
  
    -- contraint unicite 
   CONSTRAINT pk_Cont_c0 PRIMARY KEY (id_produit, id_materiel),
   
    -- contraint integrite referenciel 
   CONSTRAINT fk_Cont_c1 FOREIGN KEY (id_produit)
   REFERENCES Produit(id_produit),
   CONSTRAINT fk_Cont_c2 FOREIGN KEY (id_materiel)
   REFERENCES Materiel(id_materiel)
);

-- TransformeEn((id_materiel, id_dechet) {id}) 

-- contraint integrite referenciel (Foreign Key) 
-- TransformeEn[id_materiel] = Materiel[id_materiel]  
-- TransformeEn[id_dechet] = Dechet[id_dechet]  


CREATE TABLE TransformeEn (
   id_materiel INTEGER,
   id_dechet INTEGER,
   
    -- contraint unicite 
   CONSTRAINT pk_Tran_c0 PRIMARY KEY (id_materiel, id_dechet),
   
    -- contraint integrite referenciel 
   CONSTRAINT fk_Tran_c1 FOREIGN KEY (id_materiel)
   REFERENCES Materiel(id_materiel),
   CONSTRAINT fk_Tran_c2 FOREIGN KEY (id_dechet)
   REFERENCES Dechet(id_dechet)
);

