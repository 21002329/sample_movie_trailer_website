import media
import fresh_tomatoes

# Create a list of movies with static data
movies = [
    media.Movie(
        "Kill Bill Volume 1",
        "2003",
        "The Bride wakens from a four-year coma. The child she"
        " carried in her womb is gone. Now she must wreak veng"
        "eance on the team of assassins who betrayed her - a t"
        "eam she was once part of.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BYTczMGFiOWItMjA3Mi00YTU5LWIwMDgtYTEzNjRkNDkwMTE2XkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=ot6C1ZKyiME"
    ),
    media.Movie(
        "Kill Bill Volume 2",
        "2004",
        "The Bride continues her quest of vengeance against he"
        "r former boss and lover Bill, the reclusive bouncer B"
        "udd and the treacherous, one-eyed Elle.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BNmFiYmJmN2QtNWQwMi00MzliLThiOWMtZjQxNGRhZTQ1MjgyXkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=NSR7xRGBnOE"

    ),
    media.Movie(
        "Django Unchained",
        "2012",
        "With the help of a German bounty hunter, a freed slav"
        "e sets out to rescue his wife from a brutal Mississip"
        "pi plantation owner.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=eUdM9vrCbow"
    )
]

# Boot movies page
fresh_tomatoes.open_movies_page(movies)