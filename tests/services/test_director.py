import pytest


class DirectorNotFound(Exception):
    pass


@pytest.mark.parametrize(
    'data',
    (

            {
                "id": 1,
                "name": "test"
            },

    )
)
def test_get_one(director_service, data):
    director_service.dao.get_one.return_value = data

    assert director_service.get_one(data['id']) == data


def test_get_one_with_error(director_service):
    director_service.dao.get_one.side_effect = DirectorNotFound

    with pytest.raises(DirectorNotFound):
        director_service.get_one(0)


@pytest.mark.parametrize(
    'length, data',
    (
            (
                    2,
                    [
                        {
                            "id": 1,
                            "name": "test"
                        },
                        {
                            "id": 2,
                            "name": "test_2"
                        },
                    ],
            ),
    ),
)
def test_get_all(director_service, length, data):
    director_service.dao.get_all.return_value = data

    test_result = director_service.get_all()
    assert isinstance(test_result, list)
    assert len(test_result) == length
    assert test_result == data


@pytest.mark.parametrize(
    'original_data, modified_data',
    (
        (

            {
                "id": 1,
                "name": "test"
            },
            {
                "id": 1,
                "name": "test_upd"
            },
        ),
    )
)
def test_partially_update(director_service, original_data, modified_data):
    director_service.dao.get_one.return_value = original_data
    director_service.partially_update(modified_data)

    director_service.dao.get_one.assert_called_once_with(original_data['id'])
    director_service.dao.update.assert_called_once_with(modified_data)


@pytest.mark.parametrize(
    'original_data, modified_data',
    (
        (

            {
                "id": 1,
                "name": "test"
            },
            {
                "id": 1,
                "not_name": "test_upd"
            },
        ),
    )
)
def test_partially_update_with_wrong_fields(director_service, original_data, modified_data):
    director_service.dao.get_one.return_value = original_data

    director_service.partially_update(modified_data)

    director_service.dao.update.assert_called_once_with(original_data)


def test_delete(director_service):
    director_service.delete(1)
    director_service.dao.delete.assert_called_once_with(1)


def test_update(director_service):
    director_service.update({})
    director_service.dao.update.assert_called_once_with({})
