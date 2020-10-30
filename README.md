**Handwriting Recognition**

Handwritten Text Recognition (HTR) is challenging because of the huge variations in individual writing styles. This project focuses on Offline Handwriting Recognition. We identify the handwritten English text by using Convolutional Neural Network (CNN) for feature extraction and Recurrent Neural Network (RNN) with Connectionist Temporal Classification (CTC) for sequence labeling. Handwritten Text Recognition (HTR) system implemented with TensorFlow (TF) and trained on the IAM off-line HTR dataset. This Neural Network (NN) model recognizes the text contained in the images of segmented words as shown in the illustration below.

**Train Model : IAM Dataset**

The IAM Handwriting Database is structured as follows:

657 writers contributed samples of their handwriting

1,539 pages of scanned text

5,685 isolated and labeled sentences

13,353 isolated and labeled text lines

115,320 isolated and labeled words

We will only be using the labeled words images and words.txt (ASCII) files. After placing the downloaded files inside the data directory, we map each image to its label from the words.txt file for further processing.
