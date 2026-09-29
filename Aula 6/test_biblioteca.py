import pytest

from biblioteca import Livro


def test_livro_comeca_disponivel():
    livro = Livro("Dom Casmurro", "Machado de Assis")

    assert livro.disponivel is True


def test_emprestar_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis")

    livro.emprestar()

    assert livro.disponivel is False


def test_devolver_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis")

    livro.emprestar()
    livro.devolver()

    assert livro.disponivel is True


def test_nao_pode_emprestar_livro_indisponivel():
    livro = Livro("Dom Casmurro", "Machado de Assis")

    livro.emprestar()

    with pytest.raises(ValueError):
        livro.emprestar()


def test_nao_pode_devolver_livro_ja_disponivel():
    livro = Livro("Dom Casmurro", "Machado de Assis")

    with pytest.raises(ValueError):
        livro.devolver()


def test_dois_livros_possuem_estados_independentes():
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("O Cortiço", "Aluísio Azevedo")

    livro1.emprestar()

    assert livro1.disponivel is False
    assert livro2.disponivel is True


def test_atributo_de_classe_e_compartilhado():
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("O Cortiço", "Aluísio Azevedo")

    assert livro1.sistema == "Biblioteca Acadêmica"
    assert livro2.sistema == "Biblioteca Acadêmica"
