-- 10-genre_id_by_show.sql
-- Lists shows with at least one genre (title - genre_id) ordered by title then genre_id

SELECT tv_shows.title,
       tv_show_genres.genre_id
FROM   tv_shows
JOIN   tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER  BY tv_shows.title,
          tv_show_genres.genre_id;
