# **Indian-classical-musical-instrument-recognizer**

## Objective

Construction of an image classifier that involves data gathering, cleaning, deep learning model training, deploying, and integrating APIs.
The following ten categories of Indian classical musical instruments can be classified by the model:

1. Harmonium
2. Bansuri
3. Tabla
4. Sitar
5. Sarod
6. Santoor
7. Pakhawaz
8. Tanpura
9. Sarangi
10. Shehnai

## Dataset Preparation

**Data collection :** downloaded images with each category name using the `search_image_ddg()` function which downloads images from the DuckDuckGo search engine. 1455 of 2200+ images remained after cleaning. <br/>

**DataLoader:** Used fastai DataBlock API to set up the DataLoader with 13% validation data. <br/>

**Data Augmentation:** fastai provides default data augmentation which operates in GPU.
Details can be found in `notebooks/data_prep_training_cleaning_and_inference.ipynb`.

**Data Cleaning:** ImageClassifierCleaner() was used to clean the data. Additionally, some photos were added and deleted manually.

## Training and Data Cleaning

**Training:** Fine-tuned a resnet34 model for 3 epochs (3 times) and 2 epoch(2 times) respectively and got upto ~94% accuracy.

![tuning_image](https://github.com/moinul-hossain-dhrubo/Indian-classical-musical-instrument-recognizer/assets/122023969/5cbce310-81d0-4162-a156-a361379bd1f7)

**Data Cleaning:** The majority of the time was spent on this. The photos became noisy as DuckDuckgo, a search engine, was used to gather the data. There were multiple redundant photos as well.(For instance, when I attempted to download the image of the instrument from Santoor, it turned out that there is a company with same name that makes cosmetics. Thus, those kinds of pictures were also downloaded). Using fastai ImageClassifierCleaner, I updated and cleaned the data. I also manually added and removed a few records. With the exception of the last instance, which was the model's final iteration, I cleaned the data after training or fine-tuning each time.

## Model Deployment

I utilized the HuggingFace Spaces Gradio App to deploy the model. The implementation can be found in deployment folder or [here](https://huggingface.co/spaces/mhdhrubo/indian_classical_musical_instrument_recognizer).

![interface_image](https://github.com/moinul-hossain-dhrubo/Indian-classical-musical-instrument-recognizer/assets/122023969/fe676bf9-62aa-4a4e-91cb-5235f2d3b989)

## API Integration with GitHub Pages

The deployed model API is integrated [here](https://moinul-hossain-dhrubo.github.io/Indian-classical-musical-instrument-recognizer/) in GitHub Pages Website. You may find more information about implementation in the documentation folder.

## Real time test

Tested the model several times to check if it predicts correctly in real-time. 

![real_time_test](https://github.com/moinul-hossain-dhrubo/Indian-classical-musical-instrument-recognizer/assets/122023969/a5b1befb-fe16-4b83-b49e-7fbe1ef09407)
