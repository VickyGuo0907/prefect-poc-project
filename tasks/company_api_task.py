import json
from utils import request_client
from prefect import task, get_run_logger

COMPANY_BASE_API_URL = "https://api.company.com/"


@task(name="get_company_task", description="get company information", log_prints=True)
def get_company_task(api_token: str, company_id: str) -> dict:
    """
    :param api_token:
    :param company_id:
    :return:
    """
    logger = get_run_logger()
    dict_result = {}
    request_header = {"Authorization": f"Bearer {api_token}",
                      "content-type": "application/json"}
    try:
        get_client = request_client.GetRequest(COMPANY_BASE_API_URL, token=api_token, timeout=10)
        response = get_client.send_request("/", params={"company_id": company_id}, headers=request_header)
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
        post_client = request_client.PostRequest(COMPANY_BASE_API_URL, token=api_token, timeout=10)
        response = post_client.send_request("/", params={
            "company_id": company_id}, headers=request_headers, json=company_data)
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
        patch_client = request_client.PatchRequest(COMPANY_BASE_API_URL, token=api_token, timeout=10)
        response = patch_client.send_request("/", params={"company_id": company_id},headers=request_headers, json=company_data)
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
        delete_client = request_client.DeleteRequest(COMPANY_BASE_API_URL, token=api_token, timeout=10)
        response = delete_client.send_request("/", params={"company_id": company_id}, headers=request_headers)
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
