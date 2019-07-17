# Pict2Audio : Towards a musical composition aid tool using Deep Learning
Github created in the context of End of Studies internship. Creation of an interface
 that identify features in images drawn by a composer in order to play associated sounds. 
 Use of Neural Networks, coded in Python with Keras and Tensorflow.

## Description of the internship
This project consists in associating a sound with one or more characteristics 
defined by audio descriptors with a picture drawn by a composer. The long-term goal is to 
allow the composer to develop his own composition language in order to associate it with 
sounds from some effects banks.

In this study, I'm interested into pitch, volume and tone color features.
First, I propose as input to three Convolutional Neural Networks trained for classification 
a database composed of :
- images drawn by the composer,
- three labels for each pictures, corresponding to the features in the labels associated to 
sound features.
Then, the same work is done with three Convolutional Neural Networks trained with :
- sounds from the composer's sound bank,
- three labels for each sounds, corresponding to the features in the labels associated to 
image features.

After the training of the neural networks, an algorithm is run to obtain a sound from the 
composer's sound bank for a given image drawn by the composer.
An interface is developed to let the composer draw whatever he wants and run the algorithm.

## Organisation of the project

The folder is organised in the following way :

- **doc** is a folder containing all the definitions, link and description of articles that 
are read and studied for this project. it contains the following documents :
  - **articles** : contains the resume of the articles that has been read.
  - **definitions** : contains a few definitions about key words.
  - **references** : list all the references used in this project.
  
- **data** contains a few data necessary to train and test the different neural networks.
  - **img** : is divided in **train**, **validation**, **testgen** and **test** folders. 
  The three first folders are empty and filled by running pict2audio_img.ipynb/py. 
  **Test** contains some already drawn pictures to test the neural networks.
  - **snd** : contains sounds provided by the nsynth dataset developed by Magenta, the
   Google Team of Research and Development in Artificial Intelligence for music and sounds. 
   These sounds are divided in **train**, **validation** and **test** datasets.

- **src** contains the code implemented to answer the principal problematic of this project.
  - **interface** : contains the main files to implement a paint interface and its links with
   the neural networks.
  - **networks**, is divided in two parts :
     - **googlecolab** contains the code to run under Google Colab for every test with 
     the GPU from Google. The performances are great but the architecture of the code is not clean.
     - **local** contains a clean code to run on your computer, but your hardware might not be
     efficient enough to obtain great performances.
     Each folder is divided in two folders : **img** contains the code of the neural networks 
     that aim to recognize features in the pictures and **snd** contains the code of the neural 
     networks that aim to recognize features in sounds. 

## How to run the code
- To install all the libraries
    - run : pip install -r requirements.txt
    or install all the required libraries in a virtual environment with Anaconda

- To train the networks : 
    - In *src/networks/local/snd*, run *pict2audio_snd.py* for sounds networks
    - In *src/networks/local/img*, run *pict2audio_img.py* for images networks : this will also 
    create and load the images necessary to train the neural networks in *data/bdd_img/*.
    
    The models are saved in the same folder than these files. To run the interface, you must create 
    in audiosynthesis_dl/ a folder named models/ and move the neural networks in this folder. This 
    folder will be added soon with my own already-trained architectures. 
    
    You can also train the networks by running under Google Colab *pict2audio_img.ipynb* and 
    *pict2audio_snd.ipynb* in *src/networks/googlecolab/* .
    
- To display the interface :
    - run *paint.py*
    
    You can then use the tools to draw on the canvas. Use **pen** to draw a line, **color** to choose 
    the color of your pen, **eraser** to erase the line (still has to be improve yet), **clear** to 
    clear the whole picture and the volume bar to change the thickness of your pen.
    
    You can save your drawing by writing the name of your drawing (without the extension!) and click 
    on **save**. Click on **GET SOUND** to obtain the sound corresponding to your drawing according to
    the neural networks.
    
