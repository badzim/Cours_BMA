-- Jeux de données NOK (ne doit pas marcher àprès avoir éxécuté le jeux de données NOK)



-- Processus(id_processus {id}, nom_processus, description_processus, cout_processus, temps_processus, type_processus) 


-- Erreur : Processus existant
INSERT INTO Processus VALUES (1, 'Recyclage du papier', 'Processus qui permet de récupérer des fibres de cellulose à partir de vieux papiers', 2000, 5, 'recyclage');
-- Erreur : cout de production négative
INSERT INTO Processus VALUES (10, 'Recyclage du papier', 'Processus qui permet de récupérer des fibres de cellulose à partir de vieux papiers', -1, 5, 'recyclage');
-- Erreur : Type Processus autre que "recyclage", "production", "reparation"
INSERT INTO Processus VALUES (10, 'Recyclage du papier', 'Processus qui permet de récupérer des fibres de cellulose à partir de vieux papiers', 200, -5, 'test');


-- Produit(id_produit {id}, nom_produit, description_produit, id_processus_production, id_processus_reparation)

-- Erreur : Produit avec un id_produit deja existant
INSERT INTO Produit VALUES (1, 'T-shirt', 'T-shirt en coton', 2, 4);
-- Erreur : Produit avec un id_processus_production non existant dans la table Processus de type production
INSERT INTO Produit VALUES (5, 'T-shirt', 'T-shirt en coton', 9, 4);
-- Erreur : Produit avec un id_processus_reparation non existant dans la table Processus de type reparation
INSERT INTO Produit VALUES (5, 'T-shirt', 'T-shirt en coton', 2, 9);
-- Erreur : Produit avec un id_processus_reparation non existant dans la table Processus
INSERT INTO Produit VALUES (100, 'T-shirt', 'T-shirt en coton', 2, 5);
-- Erreur : Produit avec un id_processus_reparation NULL
INSERT INTO Produit VALUES (5, 'T-shirt', 'T-shirt en coton', 2, NULL);
-- Erreur : Produit avec un id_processus_production NULL
INSERT INTO Produit VALUES (5, 'T-shirt', 'T-shirt en coton', NULL, 4);


-- Materiel(id_materiel {id}, nom_materiel, description_materiel, proriete_physique, propriete_chimique, id_processus_recyclage)
--INSERT INTO Materiel VALUES (1, 'Acier', 'Alliage de fer et de carbone', 'Solide', 'Peut rouiller au contact de le eau et de le air', 1);


-- Dechet(id_dechet {id}, nom_dechet, description_dechet, lieuCollect, id_processus_production)  
-- Contient((id_produit, id_materiel) {id})
-- TransformeEn((id_materiel, id_dechet) {id})