#!/bin/bash

# Check if parameters are provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

VERSION=$1

WORK_POOL_NAME="schedule_pool_"$VERSION
CONFIG_FILE_PATH="./schedule_pool_"$VERSION".yaml"

echo "Running version: $VERSION with config file: $CONFIG_FILE_PATH"

# Run Schedule Pool
prefect work-pool create "$WORK_POOL_NAME" --type process
prefect deploy --profile-file  "$CONFIG_FILE_PATH" --all
prefect worker start --pool "$WORK_POOL_NAME"


