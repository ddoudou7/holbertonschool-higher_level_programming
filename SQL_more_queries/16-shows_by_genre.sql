-- 16-shows_by_genre.sql
-- Lists every show and its genres (NULL if none) ordered by title then genre

SELECT tv_shows.title,
       tv_genres.name
FROM   tv_shows
LEFT  JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT  JOIN tv_genres      ON tv_genres.id           = tv_show_genres.genre_id
ORDER  BY tv_shows.title,
          tv_genres.name;
