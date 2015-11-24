import fresh_tomatoes
import media
blade_runner = media.Movie("Blade Runner", "Androids trying to live as humans",
			"https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
			"https://www.youtube.com/watch?v=BbKSr3vb32U")
#print (blade_runner.storyline)
blade_runner.show_trailer()


alien = media.Movie ("Alien", "An alien xenomorph loose on a cargo ship",
			"https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
			"https://www.youtube.com/watch?v=LjLamj-b0I8")
#print(alien.storyline)
alien.show_trailer()


wizard_of_oz = media.Movie("The Wizard of Oz", "Dorothy Gail is not in Kansas anymore",
            "https://upload.wikimedia.org/wikipedia/commons/c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",
            "https://www.youtube.com/watch?v=H_3T4DGw10U")
#print (wizard_of_oz.storyline)
wizard_of_oz.show_trailer()


legend = media.Movie("Legend", "The Devil falls in love",
            "https://upload.wikimedia.org/wikipedia/en/9/98/Legendposter.jpg",
            "https://www.youtube.com/watch?v=als5pGB3Tfg")
#print (legend.storyline)
legend.show_trailer()


girl_with_dragon_tattoo = media.Movie("The Girl with the Dragon Tattoo", "Swedish murder mystery",
            "https://upload.wikimedia.org/wikipedia/en/8/80/The_Girl_with_the_Dragon_Tattoo_Poster.jpg",
            "https://www.youtube.com/watch?v=WVLvMg62RPA")
#print (girl_with_dragon_tattoo.storyline)
girl_with_dragon_tattoo.show_trailer()


incredibles = media.Movie("The Incredibles", "Family of Supers first adventure",
            "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
            "https://www.youtube.com/watch?v=eZbzbC9285I")
#print (incredibles.storyline)
incredibles.show_trailer()


movies = [blade_runner, alien, wizard_of_oz, legend, girl_with_dragon_tattoo, incredibles]
fresh_tomatoes.open_movies_page(movies)
