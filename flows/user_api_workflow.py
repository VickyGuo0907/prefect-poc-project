from prefect import flow, task, serve
from prefect.task_runners import SequentialTaskRunner
import utility
from tasks import user_api_task

TEST_RESULTS = []
TEST_CASE_FILE_PATH = "../test_case/user_test_case.yaml"


@flow(
    name="user_api_workflow_test", log_prints=True, task_runner=SequentialTaskRunner()
)
def user_api_workflow_test():
    print("Start test user API workflow ")
    # Read test case configuration file
    dict_test_case = utility.get_test_case_config_info(TEST_CASE_FILE_PATH)

    # Go through each test case
    for test_case_id in dict_test_case:
        print("Task 1: Get Existing user")
        exist_user_id = dict_test_case[test_case_id]["user_id"]
        dict_result = user_api_task.get_user_task(exist_user_id)
        if dict_result["status_code"] == 200:
            print("Test Passed! This user info : ", dict_result["result"])
            case_result = "Passed"
        else:
            print("Test Failed! Failed to create a new user")
            case_result = "Failed"

        TEST_RESULTS.append(
            {
                "Test Case ID": test_case_id,
                "Test Task Description": "Task 1: Get Existing user",
                "Test Result": case_result,
            }
        )
        new_user_id = ""
        print("Task 2: Create a new user")
        new_user_info = utility.get_json_data(
            dict_test_case[test_case_id]["new_user_json_path"]
        )
        dict_result = user_api_task.create_user_task(new_user_info)
        if dict_result["status_code"] == 201:
            print("Test Passed! New User info : ", dict_result["result"])
            new_user_id = dict_result["result"]["user_id"]
            case_result = "Passed"
        else:
            print("Test Failed! Failed to create a new user")
            case_result = "Failed"

        TEST_RESULTS.append(
            {
                "Test Case ID": test_case_id,
                "Test Task Description": "Task 2: Create a new user",
                "Test Result": case_result,
            }
        )

        print("Task 3: Update existing user")
        update_user_info = utility.get_json_data(
            dict_test_case[test_case_id]["update_user_json_path"]
        )
        dict_result = user_api_task.update_user_task(new_user_id, update_user_info)
        if dict_result["status_code"] == 200:
            print("Test Passed! Success update user info")
            case_result = "Passed"
        else:
            print("Test Failed! Failed to Update the user")
            case_result = "Failed"

        TEST_RESULTS.append(
            {
                "Test Case ID": test_case_id,
                "Test Task Description": "Task 3: Update existing user",
                "Test Result": case_result,
            }
        )

        print("Task 4: Delete existing user")
        dict_result = user_api_task.delete_user_task(new_user_id)
        if dict_result["status_code"] == 200:
            print(f"Test Passed! User {new_user_id} have been deleted")
            case_result = "Passed"
        else:
            print("Test Failed! Failed to delete the user")
            case_result = "Failed"

        TEST_RESULTS.append(
            {
                "Test Case ID": test_case_id,
                "Test Task Description": "Task 4: Delete existing user",
                "Test Result": case_result,
            }
        )

        utility.create_result_artifact_table(
            "user api workflow", test_case_id, TEST_RESULTS
        )

    print("Finish test User API workflow")


if __name__ == "__main__":
    user_api_workflow_test.serve(name="user_api_workflow")
