
import pytest   
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# This test prediction will confirm the following:
# Output from predict script not null
# Output from predict script is str data type
# The output is Y for an example data 

# Fixtures = ensure the single prediction is run before other testsls
@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(file_name=config.TEST_FILE)
    single_row = test_dataset[0:1]
    result = generate_predictions(single_row)
    return result

# Check if the output is not None
def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None


# Check if the output is of type string
def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('prediction')[0], str)


# Check if the output is Y
def test_single_pred_validate(single_prediction):
    assert single_prediction.get('prediction')[0] == 'Y'