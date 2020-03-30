from pathlib import Path
import datetime
import csv
import pickle
import time

import pandas as pd 
import numpy as np 

from sklearn.cluster import KMeans, MiniBatchKMeans

from vis.data.utils import DATADIR

ANALYSIS_DIR = Path(__file__)


def run_kmeans(data, n_clusters):
    """
    test runs
    :param data: cleaned data for clustering
    :param n_clusters int: integer number of target clusters
    :return: tuple(Kmeans, elapsed time (wall clock))
    """
    s = datetime.datetime.now()
    print('runnning kmeans {}'.format(n_clusters))
    kmeans = KMeans(n_clusters=n_clusters, n_jobs=1).fit(data)
    print("done")
    return kmeans, datetime.datetime.now() - s


def group_kmeans(data, n_clusters_array, path):
    """
    :param data: cleaned data for clustering
    :param n_clusters_array list<int>: list of integers for clustering
    :param path pathlib.Path object: 
    """
    timing_data = []
    s = datetime.datetime.now()
    for n_clusters in n_clusters_array:
        file_name = path.joinpath('n_cluster_{}_kmeans.pkl'.format(n_clusters))
        print(n_clusters, " -- {} --".format(file_name))
        kmeans, t = run_kmeans(data, n_clusters)
        timing_data.append([n_clusters, t])
        with file_name.open('wb') as f:
            pickle.dump(kmeans, f)
        print(n_clusters, " elapsed time -- {} --".format(datetime.datetime.now() - s))
    file_name = path.joinpath('kmeans_timing_data.csv')

    headers = ['n', 'time']
    with file_name.open('w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        [writer.writerow(td) for td in timing_data]


if __name__ == "__main__":
    frac = 0.008
    frac_str = 'frac_{}'.format('_'.join(('{}'.format(frac)).split('.')))
    datapkl = "16m_rgb.pkl"

    stamp = str(int(time.time()))
    _path = DATADIR.joinpath('analysis').joinpath('kmeans').joinpath(stamp)
    _path.mkdir(exist_ok=True)
    df = pd.read_pickle(DATADIR.joinpath(datapkl))
    df = df.sample(frac=frac)
    df.to_pickle(_path.joinpath('_'.join([frac_str, datapkl])))
    n_clusters = [3, 8, 16, 32, 64, 128, 256, 512, 1024]

    print(frac, frac_str, len(df))
    group_kmeans(df[['red', 'green', 'blue']], n_clusters, _path)
