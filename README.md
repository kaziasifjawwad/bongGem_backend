# bongGem web app

This is the app of our system developed by flask. This app allows us
to chat with our language model. In this project, we loaded the pre-trained weight
that was trained with our custom gpt-2 model. The specific requirements of this project
and the installation process is given below in detail.


### Prerequisites

- Python 3.x installed on your system
- If you want a fast training speed you might need cuda supported GPU.

### Installation process

#### For Windows execute the commands below to activate the virtual terminal:

1. `python -m venv bongGem_venv`
2. `.\bongGem_venv\Scripts\activate`

#### For Linux execute the commands below to activate the virtual terminal:

1. `python3 -m venv bongGem_venv`
2. `source ./bongGem_venv/bin/activate`
After executing the above two commands a virtual environment will be activated.
For this project we need some requirements. We can install all the requirements
using the own command.

Now execute the following command to install all the dependencies.
`pip3 install -r requirement.txt`

Now we have successfully created our virtual environment for the project.
To run the flask, we need to load the pre-trained model. As the model size
is very large, we did not add it with the project. Rather, we build a script to
download it from a colab file and extract it in the respective directory.

### Downloading pre-trained model
* Run the **download.py** file
* This will download a file named **weight.zip** in the project directory
* unzip the file and extract it in a folder named **inference/trained_weight**

After completing the above steps we are ready to use our system.

To run the project, run the command below:

`python3 app.py`
