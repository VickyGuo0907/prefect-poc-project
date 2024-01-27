from prefect import flow, task
from prefect_dask import DaskTaskRunner


@task(name="square_calculator", description="square calculator", log_prints=True)
def square_calculator(input_data_1: int):
    square = input_data_1 ** 2
    print(square)


@flow(name="workflow_with_parallel_tasks", task_runner=DaskTaskRunner())
def workflow_with_parallel_tasks(data_list: list):
    for data_item in data_list:
        square_calculator.submit(data_item)


if __name__ == "__main__":
    input_list = [10, 15, 20, 25]
    workflow_with_parallel_tasks(input_list)
