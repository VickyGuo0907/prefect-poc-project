import json
import requests
import requests.auth
from prefect import task, get_run_logger


COMPANY_API_URL = "https://api.company.com/"


@task(name="get_company_task", description="get company information", log_prints=True)
def get_company_task(api_token: str, company_id: str) -> dict:
    """
    :param api_token:
    :param company_id:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"Authorization": f"Bearer {api_token}",
                       "content-type": "application/json"}
    try:
        response = requests.get(COMPANY_API_URL, headers=request_headers, params={"company_id": company_id})
        dict_result["status_code"] = response.status_code
        dict_result["result"] = json.loads(response.content)
        if response.status_code != 200:
            logger.warning("failed to get company information, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("get_company_task request failed, error: %s", err)

    return dict_result


@task(name="create_company_task", description="create a new company", log_prints=True)
def create_company_task(api_token: str, company_id: str, company_data: dict) -> dict:
    """
    :param api_token:
    :param company_id:
    :param company_data:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"Authorization": f"Bearer {api_token}",
                       "content-type": "application/json"

                       }
    try:
        response = requests.post(COMPANY_API_URL, headers=request_headers, params={"company_id": company_id}, json=company_data)
        dict_result["status_code"] = response.status_code
        dict_result["result"] = json.loads(response.content)

        if response.status_code != 201:
            logger.warning("failed to create a new company information, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("create_company_task failed, error: %s", err)

    return dict_result


@task(name="update_company_task", description="update a company information", log_prints=True)
def update_company_task(api_token: str, company_id: str, company_data: dict) -> dict:
    """
    :param api_token:
    :param company_id:
    :param company_data:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"Authorization": f"Bearer {api_token}",
                       "content-type": "application/json"

                       }
    try:
        response = requests.patch(COMPANY_API_URL, headers=request_headers, params={"company_id": company_id}, json=company_data)
        dict_result["status_code"] = response.status_code
        dict_result["result"] = json.loads(response.content)

        if response.status_code != 201:
            logger.warning("failed to update the company information, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("update_company_task failed, error: %s", err)
    return dict_result


@task(name="delete_company_task", description="delete the company based on company id", log_prints=True)
def delete_company_task(api_token: str, company_id: str) -> dict:
    """
    :param api_token:
    :param company_id:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_headers = {"Authorization": f"Bearer {api_token}",
                       "content-type": "application/json"}
    try:
        response = requests.delete(COMPANY_API_URL, headers=request_headers, params={"company_id": company_id})
        dict_result["status_code"] = response.status_code
        if response.status_code == 200:
            dict_result["result"] = "Success"
        else:
            dict_result["result"] = json.loads(response.content)
            logger.warning("failed to delete the company, error: %s", response.content)
    except Exception as err:
        dict_result["status_code"] = 502
        dict_result["result"] = str(err)
        logger.error("delete_company_task failed, error: %s", err)

    return dict_result


