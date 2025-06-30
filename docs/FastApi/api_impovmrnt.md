# fastapi

- all model file should in model folder
- should have one requirements.txt file `pip freeze> requirements.txt`
- add field validator @field_validator('city)
- home url should have acert to inform that tell us that assert is there for you company - human readable
- Sould have a  `/heath` end points (machine readable like aws and othere clould services)

    ```sh
    MODEL_VERSION = '1.0.0` # extract from ml flow
    {
        "status": "Ok",
        "version":MODEL_VERSION,
        model_loaded": model is not None
    }
    ```

- Clean the code like sepration of conserns
  - Pynatic model in different file we can all it schema
  - ml flow
  - constant and othere lofic
- should have try except
- Use of Response model

## Response Model

a response model defines the structure of the data that your api enpoint will return. It helps in:

1. Generating clean API docs (/docs)
2. Validating output (so ypur API does not return malformed response).
3. Filtering unnecessary data from the response.
