import pytest


class MovieNotFound(Exception):
    pass


@pytest.mark.parametrize(
    'data',
    (

            {
                "id": 1,
                "title": "test_t",
                "description": "test_d",
                "trailer": "test_tr",
                "year": "test_y",
                "rating": "test_r",
                "genre_id": "test_gi",
                "director_id": "test_di"
            },

    )
)
def test_get_one(movie_service, data):
    movie_service.dao.get_one.return_value = data

    assert movie_service.get_one(data['id']) == data


def test_get_one_with_error(movie_service):
    movie_service.dao.get_one.side_effect = MovieNotFound

    with pytest.raises(MovieNotFound):
        movie_service.get_one(0)


@pytest.mark.parametrize(
    'length, data',
    (
            (
                    2,
                    [
                        {
                            "id": 1,
                            "title": "test_t",
                            "description": "test_d",
                            "trailer": "test_tr",
                            "year": "test_y",
                            "rating": "test_r",
                            "genre_id": "test_gi",
                            "director_id": "test_di"
                        },
                        {
                            "id": 2,
                            "title": "test_t",
                            "description": "test_d",
                            "trailer": "test_tr",
                            "year": "test_y",
                            "rating": "test_r",
                            "genre_id": "test_gi",
                            "director_id": "test_di"
                        },
                    ],
            ),
    ),
)
def test_get_all(movie_service, length, data):
    movie_service.dao.get_all.return_value = data

    test_result = movie_service.get_all()
    assert isinstance(test_result, list)
    assert len(test_result) == length
    assert test_result == data


@pytest.mark.parametrize(
    'original_data, modified_data',
    (
        (

            {
                "id": 1,
                "title": "test_t",
                "description": "test_d",
                "trailer": "test_tr",
                "year": "test_y",
                "rating": "test_r",
                "genre_id": "test_gi",
                "director_id": "test_di"
            },
            {
                "id": 1,
                "title": "test_t",
                "description": "test_d",
                "trailer": "test_tr_upd",
                "year": "test_y",
                "rating": "test_r_upd",
                "genre_id": "test_gi",
                "director_id": "test_di"
            },
        ),
    )
)
def test_partially_update(movie_service, original_data, modified_data):
    print(movie_service)
    print(modified_data)
    movie_service.dao.get_one.return_value = original_data
    movie_service.partially_update(modified_data)

    movie_service.dao.get_one.assert_called_once_with(original_data['id'])
    movie_service.dao.update.assert_called_once_with(modified_data)


@pytest.mark.parametrize(
    'original_data, modified_data',
    (
        (

            {
                "id": 1,
                "title": "test_t",
                "description": "test_d",
                "trailer": "test_tr",
                "year": "test_y",
                "rating": "test_r",
                "genre_id": "test_gi",
                "director_id": "test_di"
            },
            {
                "id": 1,
                "title": "test_t",
                "description_wrong": "test_d",
                "trailer": "test_tr",
                "year": "test_y",
                "rating_wrong": "test_r",
                "genre_id": "test_gi",
                "director_id": "test_di"
            },
        ),
    )
)
def test_partially_update_with_wrong_fields(movie_service, original_data, modified_data):
    movie_service.dao.get_one.return_value = original_data

    movie_service.partially_update(modified_data)

    movie_service.dao.update.assert_called_once_with(original_data)


def test_delete(movie_service):
    movie_service.delete(1)
    movie_service.dao.delete.assert_called_once_with(1)


def test_update(movie_service):
    movie_service.update({})
    movie_service.dao.update.assert_called_once_with({})
