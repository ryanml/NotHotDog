# NotHotDog

NotHotDog is a Flask/AWS Rekognition implementation of Silicon Valley's 'Not Hot Dog' app.

### Building locally

NotHotDog runs on Python 2.7.*

First install setuptools if you don't have it, get it by running (pip): 
`pip install setuptools`

Clone the Repo:  
`git clone https://github.com/ryanml/nothotdog`

Navigate to the project root, and run:  
`python setup.py install`

As the label detection relies on AWS' Rekognition service, you'll need to have the aws cli client installed. You may see install information [here](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)

Once that is installed, you'll enter your AWS IAM creds after running:  
`aws configure`

The project will serve locally on port 5000 after running:  
`python -m nothotdog`

This is a work in progress, front-end contributions welcome! 

Demo: 
[http://nothotdog.ryanlane.se](http://nothotdog.ryanlane.se)