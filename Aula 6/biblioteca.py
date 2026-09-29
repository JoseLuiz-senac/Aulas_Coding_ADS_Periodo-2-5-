class Livro:
    sistema = "Biblioteca Acadêmica"

    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self._disponivel = disponivel

    def emprestar(self):
        if not self._disponivel:
            raise ValueError("livro não está disponível para empréstimo")

        self._disponivel = False

    def devolver(self):
        if self._disponivel:
            raise ValueError("livro já está disponível")

        self._disponivel = True

    @property
    def disponivel(self):
        return self._disponivel
