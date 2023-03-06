#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import requests
import binascii
import sys
import os
import subprocess
import pandas as pd
import numpy as np
import logging
import tqdm

logger = logging.getLogger()
logger.setLevel(logging.INFO)

import astropy.time
import pandas as pd
from pathlib import Path
from .config import DATA_DIR, PLOT_DIR  
from . import example

def main():
    parser = argparse.ArgumentParser(description="Template analysis")

    parser.add_argument('n_points', type=int)

    args = parser.parse_args()

    # set file names
    data_filename = os.path.join(DATA_DIR, f"step1_result_{args.n_points}.txt")
    plot_filename = os.path.join(PLOT_DIR, f"step1_result_{args.n_points}.png")

    # run first step of dummy analysis, produce some result .txt
    logger.info("== RUNNING DUMMY ANALYSIS STEP 1 ==")
    example.produce_dummy_data(args.n_points, data_filename)

    # run second step of dummy annalysis
    logger.info("== RUNNING DUMMY ANALYSIS STEP 2 ==")
    example.plot_dummy_data(data_filename, plot_filename)

    logger.info("...done!")

if __name__ == "__main__":
    main()
