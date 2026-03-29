gcloud compute instance-groups managed set-autoscaling my-group \
  --max-num-replicas=3 \
  --target-cpu-utilization=0.75 \
  --zone=us-central1-a
