**hyperparameter_parser** performs basic hyperparameter parsing from Python source code.

The workflow is as follows:
1. Read the source code and find where `fit` or `fit_transform` methods were used. Get names for variables that store fitted models and line numbers where the models are fitted.
2. Search for initialization of the found models and parse their hyperparameters (the process can be optimized a bit by only considering the latest initialization before fitting a model).
3. Save the results in a DataFrame for more convenient analysis. Filter `XGBRegressor` and output its descriptive statistics.

For more information see the notebook.
