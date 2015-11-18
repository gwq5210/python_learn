#!/bin/bash

./get_img.py 1 50 > 1.log &
./get_img.py 50 100 > 2.log &
./get_img.py 100 150 > 3.log &
./get_img.py 150 200 > 4.log &
./get_img.py 200 250 > 5.log &
