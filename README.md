# Prefect POC project 

This is a sample project to present how to use Prefect Orchestration tool to do API-Level Testing and End-To-End
integration testing. 

## Published Medium Story
* [Test and validate data pipelines workflows with Prefect (1) - Development](https://medium.com/@vicky.guo97/test-and-validate-data-pipelines-workflows-with-prefect-cc24bb557571)
* [Test and Validate data pipelines/workflows with Prefect (2)- Deployment Strategy](https://medium.com/@vicky.guo97/test-and-validate-data-pipelines-workflows-with-prefect-cc24bb557571)


## Installation 

1. Install Prefect tools on your local. 
    * [Details installation](https://docs.prefect.io/2.10.13/getting-started/installation/#installing-the-latest-version)
    
2. Create your Python virtual Environment Manager and activate it. 
    * Make sure you install conda or create venv
```
conda create --name {env_name} {python=3.10}
conda activate {env_name}
```

3. Install package
```
pip3 install -r requirements.txt
```

4. Start run Prefect local server:
```
prefect start serve
```
dashboard at [http://127.0.0.1:4200](http://127.0.0.1:4200)

## Prefect Profile Configuration
Prefect  allow you to customize your profile, which could include both local or remote, testing, staging and production.

Please check file `setup_local_env.sh` for more details. 


## Deployment

### Schedule Long Running Pool Deployment

```commandline
podman build -t schedule_prefect_image_base .
podman run --name schedule_pool_container_100 schedule_prefect_image_base -d schedule_prefect_image_base "100"
podman run --name schedule_pool_container_100 schedule_prefect_image_base -d schedule_prefect_image_base "200"
```

### Automation Pool Deployment
```commandline
# Run Automation Pool
prefect work-pool create automation_pool_100 --type process
prefect deploy --profile-file  "./automation_pool_100.yaml" --all
prefect worker start --pool "automation_pool_100"
```

* with 'flow.serve' method used in flow code, it will create a deployment right way, 
you could easily run deployment through UI Deployment page. 

* You could run the deployment use CLI
```commandline
prefect deployment run 'user_api_workflow_test/user_api_workflow'
```
**Please check Prefect doc to get more details. 

[Prefect Deployment Doc](https://docs.prefect.io/latest/tutorial/deployments/)**

## Source Code Structure  

Below is detail explain of source code structure (Under construction):
```bash
.
├── deployments              # Deployment configuration folder
│   ├── prefect-server        # prefect server deployment configuration file
│   │   ├── docker-compose.yml      # prefect server docker compose file
│   │   ├── setup_local_env.sh      # Prefect Profile Configuration
│   ├── automation_pool_100.yaml       # automation Deployment configuration file
│   ├── deployment_schedule.sh       # Deployment configuration file
│   ├── Dockerfile        # Schedule run docker configuration file
│   ├── Jenkinsfile        # Jenkins pipeline file sample
│   ├── schedule_pool_100.yaml       # schedule Deployment configuration file
│   ├── schedule_pool_200.yaml       # schedule Deployment configuration file
│   ├── ...      # schedule Deployment configuration file for more pool
├── flows              # Sample flows folder
│   ├── parallel_flow.py       # Cams related like assets, assets type, catalogs... 
│   ├── user_api_workflow.py   # user API workflow sample    
├── tasks          # Sample tasks folder
│   ├── comapny_api_taks.py       # Sample Company api tasks (API entry points)
│   ├── user_api_workflow.py      # Sample User api tasks (API entry points)
├── test_case         # Test Case scenarios yaml file folder 
│   ├── user_test_case.yaml       # test case configuration file
├── test_data         # Test Data folder
│   ├── new_user_1.json      # test case configuration file
│   ├── ...
├── utils         # Utils folder
│   ├── requests_utils.py      # Common requests utils
│   ├── utility.py      # Common utility functions
├── README.md 
└── requirements.txt      # Python packages
```
