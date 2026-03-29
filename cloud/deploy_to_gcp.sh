#!/bin/bash
echo "Deploying to GCP..."

gcloud compute instance-groups managed resize my-group \
  --size=2 \
  --zone=us-central1-a

echo "Scale-out triggered!"
