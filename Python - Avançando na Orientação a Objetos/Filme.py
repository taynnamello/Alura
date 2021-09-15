class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes +=1
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Likes')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} -  {self._likes} Likes'
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem_playlist(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
      
vingadores = Filme('vingadores- guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
temp = Filme('Todo mundo em pânico', 1999, 99)
dark = Serie('Dark', 2017, 5)
dark.like()
dark.like()
dark.like()
temp.like()
temp.like()
temp.like()
temp.like()
vingadores.like()
vingadores.like()
vingadores.like()
atlanta.like()
atlanta.like()

filmes_e_series = [vingadores, atlanta, dark, temp]
playlist_fds = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da PlayList:{len(playlist_fds.listagem_playlist)}')

for programa in playlist_fds.listagem_playlist:
    print(programa)