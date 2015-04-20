import fresh_tomatoes # this does all the heavy lifting for the web page
import media          # our module with the Movie class in it

# instantiate Movie objects
avatar = media.Movie("Avatar", "a marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
imitation_game = media.Movie("The Imitation Game", "alan turing creates a machine to break german encryption during wwII", "http://www.razorfine.com/wp-content/uploads/2014/12/the-imitation-game-poster-600x849.jpg", "https://www.youtube.com/watch?v=S5CjKEFb-sM")
there_will_be_blood = media.Movie("There Will Be Blood", "the story of an oil tycoon, his son, and his ruin.", "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg", "https://www.youtube.com/watch?v=FeSLPELpMeM")
the_score = media.Movie("The Score", "a team of thieves steals a priceless scepter", "https://upload.wikimedia.org/wikipedia/en/9/97/The_Score_film.jpg", "https://www.youtube.com/watch?v=-h5UgLvoaok")
michael_clayton = media.Movie("Michael Clayton", "a law firm's fixer evens the score when they turn on one of their own.", "https://upload.wikimedia.org/wikipedia/en/a/a8/Michael_clayton.jpg", "https://www.youtube.com/watch?v=5kJRYBhG43Q")
v_for_vendetta = media.Movie("V For Vendetta", "a tale of modern revolution", "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg", "https://www.youtube.com/watch?v=k_13fFIrhPk")

# dump them into a list, so we can iterate through them
movies = [ v_for_vendetta, avatar, imitation_game, there_will_be_blood, the_score, michael_clayton]

# serve up the project 
fresh_tomatoes.open_movies_page(movies)
