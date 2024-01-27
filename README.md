# Prefect POC project 

This is sample project to present how to use Prefect Orchestration tool to do API-Level Testing and End-To-End
integration testing. 

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

## Deployment
* with 'flow.serve' method used in flow code, it will create a deployment right way, 
you could easily run deployment through UI Deployment page. 

* You could run the deployment use CLI
```commandline
prefect deployment run 'user_api_workflow_test/user_api_workflow'
```
**Please check Prefect doc to get more details. [Deployment](https://docs.prefect.io/latest/tutorial/deployments/)**

## Source Code Structure  

Below is detail explain of source code structure (Under construction):
```bash
.
├── flows              # Sample flows folder
│   ├── parallel_flow.py       # Cams related like assets, assets type, catalogs... 
│   ├── user_api_workflow.py   # user API workflow sample    
├── tasks          # Sample tasks folder
│   ├── comapny_api_taks.py       # Sample Company api tasks (API entry points)
│   ├── user_api_workflow.py      # Sample User api tasks (API entry points)
├── test_case         # Test Case scenarios yaml file folder 
│   ├── user_test_case.yaml       # test case configuration file
└── test_data         # Test Data folder
│   ├── new_user_1.json      # test case configuration file
│   ├── ...
├── README.md 
├── requirements.txt      # Python packages
└── utility.py              # Common Utility functions
```
