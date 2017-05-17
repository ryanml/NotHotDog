# Communicates with AWS Rekognition for image label detection
# Author: Ryan Lanese

import io
import boto3

class Rekognition(object):

    def __init__(self):
        self.min_conf = 90
        self.max_labels = 5
        self.hd_label = 'Hot Dog'
        self.client = boto3.client('rekognition')

    def get_bytes(self, file):
        image = open(file, mode='rb')
        return image.read()

    def is_hot_dog(self, file):
        is_hot_dog = False
        response = self.client.detect_labels(
            Image={
                'Bytes': self.get_bytes(file)
            },
            MaxLabels=5,
            MinConfidence=self.min_conf
        )
        labels = response['Labels']
        for label in labels:
            if label['Name'] == self.hd_label:
                is_hot_dog = True
                break
        return is_hot_dog 


