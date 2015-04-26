import fresh_tomatoes # this does all the heavy lifting for the web page
import media          # our module with the Movie class in it

avatar = media.Movie("Avatar",  "12/18/2009", "A Marine travels to an alien planet to battle the native people.", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
imitation_game = media.Movie("The Imitation Game", "12/25/2014", "Alan Turing creates a machine to break German encryption during World War II.", "http://www.razorfine.com/wp-content/uploads/2014/12/the-imitation-game-poster-600x849.jpg", "https://www.youtube.com/watch?v=S5CjKEFb-sM")
there_will_be_blood = media.Movie("There Will Be Blood", "1/25/2008", "The story of an oil tycoon, his greed, and his downfall.", "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg", "https://www.youtube.com/watch?v=FeSLPELpMeM")
the_score = media.Movie("The Score", "7/13/2001", "A team of thieves steals a priceless scepter in this pulse-pounding epic.", "https://upload.wikimedia.org/wikipedia/en/9/97/The_Score_film.jpg", "https://www.youtube.com/watch?v=-h5UgLvoaok")
michael_clayton = media.Movie("Michael Clayton", "10/12/2007", "A law firm's fixer evens the score when they turn on one of their own.", "https://upload.wikimedia.org/wikipedia/en/a/a8/Michael_clayton.jpg", "https://www.youtube.com/watch?v=5kJRYBhG43Q")
v_for_vendetta = media.Movie("V For Vendetta", "3/17/2006", "A tale of modern oppression and revolution.", "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg", "https://www.youtube.com/watch?v=k_13fFIrhPk")

movies = [v_for_vendetta, avatar, imitation_game, there_will_be_blood,
         the_score, michael_clayton]

fresh_tomatoes.open_movies_page(movies)
