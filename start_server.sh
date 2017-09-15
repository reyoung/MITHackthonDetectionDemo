#!/bin/bash
wget https://s3.us-east-2.amazonaws.com/models.paddlepaddle/SSD/param.tar
wget https://s3.us-east-2.amazonaws.com/models.paddlepaddle/SSD/inference_topology.pkl
nvidia-docker run --name detection_serv -d -v $PWD:/data -p 9000:80 -e WITH_GPU=1 paddlepaddle/book:serve
