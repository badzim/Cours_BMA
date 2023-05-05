-- Jeux de données OK (ça doit marcher)

-- Processus(id_processus {id}, nom_processus, description_processus, cout_processus, temps_processus, type_processus) 
INSERT INTO Processus VALUES (1, 'Recyclage du papier', 'Processus qui permet de récupérer des fibres de cellulose à partir de vieux papiers', 2000, 5, 'recyclage');
INSERT INTO Processus VALUES (2, 'Extrusion de plastique', 'Processus qui permet de transformer des granulés de plastique en objets en plastique', 5000, 10, 'production');
INSERT INTO Processus VALUES (3, 'Fusion du verre', 'Processus qui permet de faire fondre du verre pour le transformer en objets en verre', 8000, 15, 'production');
INSERT INTO Processus VALUES (4, 'reparation', 'Processus qui permet de faire fondre du verre pour le transformer en objets en verre', 8000, 15, 'reparation');


-- Produit(id_produit {id}, nom_produit, description_produit, id_processus_production, id_processus_reparation)
INSERT INTO Produit VALUES (1, 'T-shirt', 'T-shirt en coton', 2, 4);
INSERT INTO Produit VALUES (2, 'Pantalon', 'Pantalon en jean', 2, 4);
INSERT INTO Produit VALUES (3, 'Chaussures', 'Chaussures de sport', 2, 4);


-- Materiel(id_materiel {id}, nom_materiel, description_materiel, proriete_physique, propriete_chimique, id_processus_recyclage)
INSERT INTO Materiel VALUES (1, 'Acier', 'Alliage de fer et de carbone', 'Solide', 'Peut rouiller au contact de le eau et de le air', 1);
INSERT INTO Materiel VALUES (2, 'Plastique', 'Polymère synthétique', 'Souple', 'Peut fondre à haute température', 1);
INSERT INTO Materiel VALUES (3, 'Verre', 'Matériau transparent et fragile', 'Dur et cassant', 'Résistant aux acides et aux bases', 1);


-- Dechet(id_dechet {id}, nom_dechet, description_dechet, lieuCollect, id_processus_production)  
INSERT INTO Dechet VALUES (1, 'Carton', 'Matériau recyclable issu de la cellulose des végétaux', 'Déchèterie', 2);
INSERT INTO Dechet VALUES (2, 'Plastique', 'Matériau synthétique issu de la pétrochimie', 'Bac jaune', 2);
INSERT INTO Dechet VALUES (3, 'Verre', 'Matériau transparent et cassant', 'Bac vert', 3);

-- Contient((id_produit, id_materiel) {id})
INSERT INTO Contient VALUES (1, 1);
INSERT INTO Contient VALUES (1, 2);
INSERT INTO Contient VALUES (2, 1);
INSERT INTO Contient VALUES (3, 3);

-- TransformeEn((id_materiel, id_dechet) {id})
INSERT INTO TransformeEn VALUES (1, 2);
INSERT INTO TransformeEn VALUES (2, 2);
INSERT INTO TransformeEn VALUES (3, 3);