from metaflow.client.core import namespace, Run, Flow

def main():
    # Set namespace if you need a specific one, or None for default
    namespace(None)

    flow = Flow("TrainActionableInsightsFlow")
    run = Run("TrainActionableInsightsFlow/223287")  # note: 'Flow' capitalization
    surrogate_model = run.data.surrogate_model
    fit_params_xgb = surrogate_model.get_params()["fit_params_xgb"]
    print(fit_params_xgb)

if __name__ == "__main__":
    main()