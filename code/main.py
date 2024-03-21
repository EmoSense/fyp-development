import os
import subprocess
import shutil
import logging
import data_loading
import config

from sklearn.model_selection import train_test_split
from data_loading import load_data, create_dir, move_files
from data_splitting import split_data
from data_augmentation import augment_wav_data_pipeline,augment_spectrogram_data_pipeline
from spectrogram_conversion import convert_to_spectrogram

logging.basicConfig(filename="example.log", level=logging.INFO)
logger = logging.getLogger(__name__)

PROCESSED_DIR = config.PROCESSED_DIR
RAW_DIR = config.ROOT_DIR_PATH



def install_dependencies():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("Error occurred while installing dependencies.")


def main():
    """ Main function """
    
    #file_paths, labels = load_data(RAW_DIR)
    
    #train_dir, val_dir, test_dir = create_dir()
    #print("Directories created.", train_dir, val_dir, test_dir) # for debugging
    
    #split_data(file_paths, labels, train_dir, val_dir, test_dir)
    #print("Data splitting complete.") # for debugging

    #augment_wav_data_pipeline(train_dir)
    #print("Data augmentation complete.") # for debugging

    #convert_to_spectrogram(config.TRAIN_DIR)
    print("Spectrogram conversion complete.") # for debugging

    augment_spectrogram_data_pipeline(config.TRAIN_DIR + '/spectrograms')
    print("Spectrogram augmentation complete.") # for debugging

if __name__ == "__main__":
    #install_dependencies()
    main()
