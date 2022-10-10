SELECT Films.titre, Films.annee, Projeter.date, Genres.nom
FROM Films
INNER JOIN Genres
ON Films.idGenre = Genres.idGenre
INNER JOIN Projeter
ON Films.idFilm = Projeter.idFilm
INNER JOIN Cinemas
ON Cinemas.idGenre = Projeter.idCinema
WHERE Cinemas.nom = 'CGR Niort';