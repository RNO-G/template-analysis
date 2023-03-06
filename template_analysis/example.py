#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, sys

def example():
    print("I am a minimal example doing nothing!")

def produce_dummy_data(n=100, outfile="test_output.txt"):
    # generate a dummy file with n points"
    x = np.linspace(1, 100, n)
    y = np.random.uniform(0, 1, n)

    df = pd.DataFrame({"x": x, "y": y})
    print(f"writing output to {outfile}")
    df.to_csv(outfile)

def plot_dummy_data(infile, outfile):
    # use infile with x,y data to generate plot outfile
    data = pd.read_csv(infile)
    plt.plot(data.x, data.y)
    plt.xlabel("x")
    plt.ylabel("y")
    print(f"writing plot generated from {infile} to {outfile}")
    plt.savefig(outfile)
