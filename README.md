# audiosynthesis_dl
Github created in the context of End of Studies internship about Sound synthesis and Sound modification using Deep Learning.

## Description of the internship

This internship is about doing a state of the art about the various methods of music synthesis, based on neural networks. Then, new methods will be proposed to synthesize or transform sounds. The applications will be synthesis or transformation of instrumental sound, aiming to help for musical composition.

This project especially consists in associating a sound with one or more characteristics defined by audio descriptors with a picture drawn by a composer. The long-term goal is to allow the composer to develop his own composition language in order to associate it with sounds from some effects banks.

In this study, I'm interested into pitch, volume and tone color features, and I will propose as input to a Convolutional Neural Network trained for classification a database composed of :
- images drawn by the composer,
- three labels for each pictures, corresponding to the features in the labels associated to sound features.
After the training of the neural network, we want to obtain a sound for a given image at the input of the network.


## Organisation of the project

The folder is organised in the following way :

- **doc** is a folder containing all the definitions, link and description of articles that are read and studied for this project. it contains the following documents :
  - **articles** : contains the resume of the articles that has been read.
  - **definitions** : contains a few definitions about key words.
  - **references** : list all the references used in this project.
  
- **data** contains a few data necessary to train and test the differents neural networks.
  - **img** : is divided in **train**, **validation**, **testgen** and **test** folders. The three first folders are empty and filled by running Pict2Audio_multineural.ipynb. **test** contains some already drawn pictures to test the neural networks.
  - **snd** : contains sounds provided by the nsynth dataset developped by Magenta, the Google Team of Research and Developpment in Artificial Intelligence for music and sounds. These sounds are divided in **train**, **validation** and **test** datasets.

- **src** contains the code implemented to answer the principal problematic of this project.
  - **interface** : contains the main files to implement a paint interface and to link it with the neural networks
  - **networks** : contains in **img** the code of the neural networks that aim to recognize features in the pictures, contains in **snd** the code of the neural networks that aim to recognize features in sounds? 
