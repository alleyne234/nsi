SELECT Personnes.nom, Personnes.prenom
FROM Jouer
INNER JOIN Personnes
ON Personnes.idPersonne = Jouer.idActeur
INNER JOIN Films
ON Jouer.idFilm = Films.idFilm
WHERE Films.titre = 'Usual Suspects';