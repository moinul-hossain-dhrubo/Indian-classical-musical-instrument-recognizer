# Indian-classical-musical-instrument-recognizer

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

# Dataset Preparation

**Data collection :** downloaded images with each category name using the `search_image_ddg()` function from the DuckDuckGo search engine. <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader with 13% validation data. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU.
Details can be found in `notebooks/data_prep_training_cleaning_and_inference.ipynb`.

# Training and Data Cleaning

**Training:** Fine-tuned a resnet34 model for 3 epochs (3 times) and 2 epoch(2 times) respectively and got upto ~95% accuracy.

**Data Cleaning:** The majority of the time was spent on this. The photos became noisy as DuckDuckgo, a search engine, was used to gather the data. There were multiple redundant photos as well.(For instance, when I attempted to download the image of the instrument from Santoor, it turned out that there is a company with same name that makes cosmetics. Thus, those kinds of pictures were also downloaded). Using fastai ImageClassifierCleaner, I updated and cleaned the data. I also manually added and removed a few records. With the exception of the last instance, which was the model's final iteration, I cleaned the data after training or fine-tuning each time.

# Model Deployment

I utilized the HuggingFace Spaces Gradio App to deploy the model. The implementation can be found in deployment folder or [here].

# API integration with GitHub Pages

The deployed model API is integrated [here](https://moinul-hossain-dhrubo.github.io/Indian-classical-musical-instrument-recognizer/) in GitHub Pages Website. You may find more information about implementation in the documentation folder.