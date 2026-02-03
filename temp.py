from metaflow import Flow, Run, namespace

# Optional: reset to default namespace so you see all runs
namespace(None)

# Load a flow by name
flow = Flow("TrainActionableInsightsFlow")

# Get the latest successful run
run = flow.latest_successful_run
print("Run ID:", run.id)
print("Finished at:", run.finished_at)

# Example: access artifacts from a specific step
# Replace 'train_model' and 'model_artifact' with real names from your flow
step = run['train_model']
task = step.task  # or step['task_id'] if there are multiple
model = task.data.model_artifact

print(type(model))