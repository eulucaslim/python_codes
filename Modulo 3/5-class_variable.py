class Movie:
    platform = 'OneBitFilmes'
    def __init__(self,name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
        
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("##Dados do Filme##")
        print(f'Plataforma: {Movie.platform}')
        print(f"Nome do filme: {self.name}")
        print(f'Ano de lançamento: {self.yearLaunch}')
        print(f'Está no plano? {self.includedPlan}')
        print(f'Avaliação do filme: {self.totalEvaluation}')
        print(f'Duração do filme: {self.durationMinutes}')
        print(f'Total de Avaliadores: {self.evaluators}\n')

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f'Media do filme {self.name}: {self.totalEvaluation / self.evaluators}')
        
mario = Movie('Super Mario Bros', 2023, False, 135)
avatar = Movie('Avatar', 2023, False, 180)
mario.evaluate(9.5)
mario.evaluate(10.0)
mario.techinal_sheet()
mario.average()

# Modificando a plataforma
Movie.platform = 'OneBitCode Pro'
avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.techinal_sheet()
avatar.average()
