# Emotion Identifier
This Emotion Identifier labels images of human faces based on their emotion. This could help people who don’t understand emotion due to psychological disorders like Alexithymia by aiding in understanding what emotions look like.

## The Algorithim
It was made by retraining ResNet-18 with a facial emotion recognition Image dataset, containing the emotions angry, happy, neutral, sad, and surprise. It works by using this training to associate similar groups of images with their respective variables, or in this case, emotions.

## Running This Project
1. Download the dataset via. cURL:

    `#!/bin/bash
curl -L -o ~/Downloads/emotion-recognition-dataset.zip\
  https://www.kaggle.com/api/v1/datasets/download/sujaykapadnis/emotion-recognition-dataset`

2. Split the images into test, train, and val folders with split_dataset.py:

   `python3 split_dataset.py`
   
3. Run the Docker container:

      `cd ~/jetson-inference/
./docker/run.sh`

4. Navigate into your classification folder:

      `cd python/training/classification`

5. Save the current model paths:

      `NET=models/testdataset
DATASET=data/testdataset`

6. Load your model and test it with an image:

      `imagenet.py \
        --model=$NET/resnet18.onnx \
        --labels=$DATASET/labels.txt \
        --input_blob=input_0 \
        --output_blob=output_0 \`

## Visual Guide
https://youtu.be/UL_-91YP0WI


