-- 11-genre_id_all_shows.sql
-- Lists every show with its genre_id (NULL when no genre) ordered by title then genre_id

SELECT tv_shows.title,
       tv_show_genres.genre_id
FROM   tv_shows
LEFT  JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER  BY tv_shows.title,
          tv_show_genres.genre_id;
