# Indian-classical-musical-instrument-recognizer

Building of an image classifier that involves data collection, cleaning, model training, deployment and API integration.
The model can classify 10 different types of indian classical musical instruments, that are :

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

Data collection : Downloaded from DuckDuckGo using each category name
DataLoader: Used fastai DataBlock API to set up the DataLoader.
Data Augmentation: fastai provides default data augmentation which operates in GPU.
Details can be found in 

# Training and Data Cleaning

Training: Fine-tuned a resnet34 model for 2 epochs (5 times) and got upto ~95% accuracy.

Data Cleaning: This part took the highest time. Since the data was collected using a search engine(DuckDuckgo), the images became noisy. Also, there were several redundant images.(e.g. I tried to download image the instrument santoor but it appears that santoor is also a beauty product company. So those types of images were also been downloaded) . I cleaned and updated data using fastai ImageClassifierCleaner, also some of them were manually added and deleted . I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model.

# Model Deployment

I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in deployment folder or [here].

# API integration with GitHub Pages

The deployed model API is integrated [here](https://moinul-hossain-dhrubo.github.io/Indian-classical-musical-instrument-recognizer/) in GitHub Pages Website. Implementation and other details can be found in docs folder.