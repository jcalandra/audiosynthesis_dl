# audiosynthesis_dl
Github created in the context of End of Studies internship about Sound synthesis and Sound modification using Deep Learning.

## Description of the internship

This internship is about doing a state of the art about the various methods of music synthesis, based on neural networks. Then, new methods will be proposed to synthesize or transform sounds. The applications will be synthesis or transformation of instrumental sound, aiming to help for musical composition.

This project especially consists in associating a sound with one or more characteristics defined by audio descriptors with a picture drawn by a composer. The long-term goal is to allow the composer to develop his own composition language in order to associate it with sounds from some effects banks.

I am first interested in pitch, and I will propose as input to a Convolutional Neural Network trained for classification a database of couples:
- an image drawn by the composer,
- the label of the sound extract corresponding to the associated note pitch. 
After training, we want to obtain a sound for a given image at the input of the network.
Validation tests will be conducted by verifying that the sounds obtained correspond to the desired descriptors.


## Organisation of the project

The folder is organised in the following way :

- **doc** is a folder containing all the definitions, link and description of articles that are read and studied for this project. it contains the following documents :
  - **articles** : contains the resume of the articles that has been read.
  - **definitions** : contains a few definitions about key words.
  - **references** : list all the references used in this project.
  
- **test** contains the already existing code that has been tested.
  
- **data** contains a few data necessary to test the different neural networks.

- **src** contains the code implemented to answer the principal problematic of this project.
