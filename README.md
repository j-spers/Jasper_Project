# Emotion Identifier
This Emotion Identifier labels images of human faces based on their emotion.



## The Algorithim
It was made by retraining ResNet-18 with a facial emotion recognition Image dataset, containing the emotions angry, happy, neutral, sad, and surprise. It works by using this training to associate similar groups of images with their respective variables, or in this case, emotions.

## Running This Project
1. Download the dataset via. cURL:
   
   `#!/bin/bash
curl -L -o ~/Downloads/emotion-recognition-dataset.zip\
  https://www.kaggle.com/api/v1/datasets/download/sujaykapadnis/emotion-recognition-dataset`
