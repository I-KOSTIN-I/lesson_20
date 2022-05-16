from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from service.director import DirectorService

from dao.genre import GenreDAO
from service.genre import GenreService

from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def director_service(director_dao):
    return DirectorService(dao=director_dao)


@pytest.fixture
def genre_dao():
    dao = GenreDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def genre_service(genre_dao):
    return GenreService(dao=genre_dao)


@pytest.fixture
def movie_dao():
    dao = GenreDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def movie_service(movie_dao):
    return MovieService(dao=movie_dao)
