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
