SELECT annee, titre
FROM Films
ORDER BY annee DESC
LIMIT 1;

SELECT MAX(annee), titre
FROM Films;