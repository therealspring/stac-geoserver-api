#!/bin/bash -x
# Authenticate the gcloud SDK so it can read from buckets
/usr/local/gcloud-sdk/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file=${BUCKET_READ_SERVICE_ACCOUNT_KEYFILE}

echo "launching app"
waitress-serve --expose-tracebacks --listen=0.0.0.0:${API_HOST_PORT} --call stac_api:create_app 2>&1
