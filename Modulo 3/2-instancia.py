class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0
    
# Primeiro Filme #
movie = Movie()
movie.name = "Super Mario Bros"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130

# Segundo Filme #
movie2 = Movie()
movie2.name = 'Cegonhas'
movie2.yearLaunch = 2021
movie2.includedPlan = True
movie2.note = 7.0
movie.durationMinutes = 150

print("##Dados do Filme##")
print(f"Nome do filme: {movie.name} \nAno de Lançamento: {movie.yearLaunch} ")
print(f"Nome do filme: {movie2.name} \nAno de Lançamento: {movie2.yearLaunch} ")
