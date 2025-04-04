## Setting Up a Virtual Environment and Running Python Scripts

### 1. Create a Virtual Environment
```sh
python -m venv mlops_env
```

### 2. Activate the Virtual Environment
```sh
mlops_env\Scripts\activate
```

### 3. Move to E:\ Drive (Where the Project Exists)
```sh
E:
```

### 4. Navigate to the Project Directory
```sh
cd E:\edux_mlops_dir\ML_MODEL\packaging-ml-model\prediction_model
```

### 5. Execute `training_pipeline.py`
```sh
python training_pipeline.py
```

### 6. Handling Dependency Errors
If you encounter dependency errors, create a `requirements.txt` file in the same directory as the `prediction_model` package.

#### Content of `requirements.txt`
```
numpy==2.0.2
pandas==2.2.2
joblib==1.4.2
scikit-learn==1.6.1
scipy==1.14.1
wheel==0.45.1
```

### 7. Install Dependencies
Navigate to the location where `requirements.txt` exists and install dependencies within the virtual environment.
```sh
pip install -r requirements.txt
```

### 8. Run `training_pipeline.py` and `predict.py`
Now that the virtual environment has all required dependencies, execute the scripts:
```sh
python training_pipeline.py
python predict.py
```
This time, you should not encounter any dependency errors.




## Pytest

"In MLOps, we deal with pipelines, models, APIs, and complex workflows. If any step in this pipeline fails, it can disrupt the entire process. For instance:

    * A data preprocessing script might generate incorrect outputs due to faulty logic.
    * A machine learning model’s predictions might be misaligned because of a change in the data format.

To catch these issues, we use testing frameworks like pytest, which are lightweight, flexible, and easy to integrate."

# Why Testing is Critical in MLOps:

    * In MLOps, continuous integration and deployment (CI/CD) pipelines are the backbone. Automated testing ensures that:
        * Every change in the codebase is validated.
        * New features or updates don’t break existing functionality.
        * Models and scripts produce accurate results after deployment.

# Example in MLOps:

    * Imagine you’re deploying a model API that predicts house prices.
        * What if your API fails to handle negative values?
        * Or the preprocessing step mistakenly normalizes categorical data?
        With pytest, you can write test cases to catch such issues.


 # Install prediction model from git

 * pip install git+https://github.com/bipulshahi/edux_mlops.git@main#subdirectory=ML_MODEL/packaging-ml-model

# if setupy.py is not within any sub-directory like packaging-ml-model over here then -

   * pip install git+https://github.com/bipulshahi/edux_mlops.git


calculator/
├── main.py
├── test_add.py
└── setup.py

