import json
import requests
import requests.auth
from prefect import task, get_run_logger

SAMPLE_USER_API_URL = "https://jsonplaceholder.typicode.com/posts"


@task(name="get_user_task", description="get user information", log_prints=True)
def get_user_task(user_id: str) -> dict:
    """
    :param user_id:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"content-type": "application/json"}
    try:
        response = requests.get(SAMPLE_USER_API_URL + f"/{user_id}", headers=request_headers)
        dict_result["status_code"] = response.status_code
        dict_result["result"] = json.loads(response.content)
        if response.status_code != 200:
            logger.warning("failed to get user information, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("get_user_task request failed, error: %s", err)

    return dict_result


@task(name="create_user_task", description="create a new user", log_prints=True)
def create_user_task(user_data: dict) -> dict:
    """
    :param user_data:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"content-type": "application/json;charset=UTF-8"}
    try:
        response = requests.post(SAMPLE_USER_API_URL, headers=request_headers, json=user_data)
        dict_result["status_code"] = response.status_code
        dict_result["result"] = json.loads(response.content)

        if response.status_code != 201:
            logger.warning("failed to create a new user information, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("create_user_task failed, error: %s", err)

    return dict_result


@task(name="update_user_task", description="update a user information", log_prints=True)
def update_user_task(user_id: str, user_data: dict) -> dict:
    """
    :param user_id:
    :param user_data:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"content-type": "application/json"}
    try:
        response = requests.patch(SAMPLE_USER_API_URL + f"/{user_id}", headers=request_headers, json=user_data)
        dict_result["status_code"] = response.status_code
        dict_result["result"] = json.loads(response.content)

        if response.status_code != 200:
            logger.warning("failed to update the user information, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("update_user_task failed, error: %s", err)
    return dict_result


@task(name="delete_user_task", description="delete the user based on user id", log_prints=True)
def delete_user_task(user_id: str) -> dict:
    """
    :param user_id:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"content-type": "application/json"}
    try:
        response = requests.delete(SAMPLE_USER_API_URL + f"/{user_id}", headers=request_headers)
        dict_result["status_code"] = response.status_code
        if response.status_code == 200:
            dict_result["result"] = "Success"
        else:
            dict_result["result"] = json.loads(response.content)
            logger.warning("failed to delete the user, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("delete_user_task failed, error: %s", err)

    return dict_result


@task(name="import_user_from_csv", description="import users from csv file", log_prints=True)
def import_user_from_csv(api_token: str, import_file_path: str, query_data: str) -> dict:
    """
    :param api_token:
    :param import_file_path:
    :param query_data:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"Authorization": f"Bearer {api_token}",
                       "content-type": "application/json"}
    try:
        import_file = {'file': (import_file_path, open(import_file_path, 'rb'), 'text/csv')}
        response = requests.post(SAMPLE_USER_API_URL + "/import", headers=request_headers, params=query_data,
                                 files=import_file)

        dict_result["status_code"] = response.status_code
        dict_result["result"] = json.loads(response.content)
        if response.status_code != 200:
            logger.warning("failed to import user from csv file, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("import_user_from_csv failed, error: %s", err)

    return dict_result
