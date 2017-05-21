# Communicates with AWS Rekognition for image label detection
# Author: Ryan Lanese

import boto3

class Rekognition(object):

    def __init__(self):
        self.min_conf = 80
        self.max_labels = 5
        self.hd_label = 'Hot Dog'
        self.uploads_dir = 'static/img/'
        self.client = boto3.client('rekognition')

    def get_bytes(self, file):
        image = open(file, mode='rb')
        return image.read()

    def get_confidence(self, file):
        confidence = 0.0
        response = self.client.detect_labels(
            Image={
                'Bytes': self.get_bytes(self.uploads_dir + file)
            },
            MaxLabels=self.max_labels,
            MinConfidence=self.min_conf
        )
        labels = response['Labels']
        for label in labels:
            if label['Name'] == self.hd_label:
                confidence = label['Confidence']
                confidence = "%.2f" % float(confidence)
                break
        return confidence

