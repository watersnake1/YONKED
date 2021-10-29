import gpt_2_simple as gpt2
import os
import requests

# This script will generate tweets based on provided data for Felipe Shah

model_name = "124M"

# make sure the model is downloaded
if not os.path.isdir(os.path.join("models", mode_name)):
    print(f"Downloading {model_name} model..")
    gpt2.download_gpt2(model_name=model_name)

# TODO:
# implement training
# implement generation
# integrate twitter data feeds
