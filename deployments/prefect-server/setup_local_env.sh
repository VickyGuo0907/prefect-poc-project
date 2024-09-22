prefect profile create local --from default
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
prefect config set PREFECT_LOGGING_LEVEL='INFO'

prefect profile create remote --from local
prefect profile use remote
prefect config use PREFECT_API_URL=http://XX.XX.XX.XX:4200/api # Remote VM/server IP

prefect profile use local