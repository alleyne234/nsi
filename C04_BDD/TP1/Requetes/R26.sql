SELECT Films.titre, MAX(Films.annee)
FROM Films
INNER JOIN Genres
ON Films.idGenre = Genres.idGenre
WHERE Genres.nom = 'Comédie';
