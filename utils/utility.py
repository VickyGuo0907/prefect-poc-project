import json
import yaml
from prefect.artifacts import create_table_artifact, create_markdown_artifact
from pathlib import Path


def get_test_case_config_info(test_case_file_path: str) -> dict:
    """
    This is common function to get test case configuration info
    :param test_case_file_path:
    :return:
    """
    dict_test_config_info = {}
    try:
        with open(test_case_file_path, 'r'):
            dict_test_config_info = yaml.safe_load(Path(test_case_file_path).read_text())
    except Exception as err:
        print(f"failed to get test configuration info, detail error: ", err)
    return dict_test_config_info


def get_json_data(file_path: str):
    """
    This is common function to get json file data
    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'r') as file_json:
            temp_data = file_json.read()
            json_data = json.loads(temp_data)
    except Exception as err:
        print(f"failed to json file data, detail error: ", err)
    return json_data


def create_result_artifact_table(workflow_title: str, test_case_id: str, result_data: list):
    create_table_artifact(
        key="test-result-report",
        table=result_data,
        description=f"#{workflow_title} test result: {test_case_id}"
    )
