SELECT Cinemas.nom, Cinemas.adresse, Projeter.date
FROM Cinemas
INNER JOIN Projeter
ON Cinemas.idCinema = Projeter.idCinema
INNER JOIN Films
ON Projeter.idFilm = Films.idFilm
WHERE Films.titre = 'Seven';