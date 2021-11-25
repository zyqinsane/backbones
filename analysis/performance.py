# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import numpy as np
# from sklearn.neighbors  import DistanceMetric
from lib.analysis_util import load_all_runs, plotmetric
from lib.latency_lib import LIGHT_IN_FIBER, LIGHT_IN_VACUUM, \
    FIBER_PATH_STRETCH, haversine_to_km, load_locations


sys.path.append('lib/latency_lib')

sys.path.append('lib/analysis_util')

# sys.path.append('/lib/latency_lib.py')

def avalibility():
    # Load pre-processed data for path control
    # data3, paco_hist3, rero_hist3, pc3 = load_all_runs(rerouting_experiment)
    # Load geo information
    altitude = 1300
    min_elev = 40
    orbits = 32
    sat_per_orbit = 50
    inclination = 53
    GST_FILE = "data/raw/ixp_geolocation.csv"
    SRC_FILE = "data/raw/WUP2018-F22-Cities_Over_300K_Annual.csv"

    for t in range(1000):
        sat_pos, gst_pos, src_pos =  load_locations(altitude, orbits, sat_per_orbit,
                                               inclination, GST_FILE, SRC_FILE,time = t)
        all_inactive = []
        hashmap = {}
        for idx,gst in enumerate(gst_pos.shape[0]):
            state = np.random.rand()
            hashmap[gst] = state
            if(state < 0.5):
                all_inactive.append(idx)

        print(all_inactive)




        '''
        cur_inactive = np.random.choice(params['indexes'],
                                        size=num_deactivate,
                                        replace=False)
        all_inactive.append(cur_inactive)
        # Distance between cities
        pairwise_src = DistanceMetric.pairwise(
            DistanceMetric.get_metric("haversine"),
            src_pos, src_pos)
        pairwise_src = haversine_to_km(pairwise_src)

        terr_only = pairwise_src * FIBER_PATH_STRETCH / LIGHT_IN_FIBER  # 计算地面时延
        gclatency = pairwise_src / LIGHT_IN_FIBER
        gcbound = pairwise_src / LIGHT_IN_VACUUM
        while (t%50==0):
            inactive_list.update()



    gc_hist, buckets = np.histogram(gclatency * 1000, bins=100, range=(0, 120)) # （0，120）区间内，小区间间隔为1.2
    gcb_hist, _ = np.histogram(gcbound * 1000, bins=100, range=(0, 120))
    terr_hist, _ = np.histogram(terr_only * 1000, bins=100, range=(0, 120))

    plt.figure(figsize=(8, 6))
    plt.plot(buckets[1:],np.,":",markersize=4,markevery=[50],label="Avalibility",linewidth=3)

    plt.xlabel("One-way latency (ms)")

    plt.ylabel("Avalibility(%)")

    x_axis = data3[10]['paco']['hist'][0][1][:-1] * 1000

    paco_avg = np.asarray(paco_hist3)
    paco_avg = np.average(paco_avg, axis=0)
    rero_avg = np.asarray(rero_hist3)
    rero_avg = np.average(rero_avg, axis=0)

    plt.plot(x_axis, np.cumsum(paco_avg) / np.sum(paco_avg), '-', markersize=4,
             markevery=[40], label="PaCo avg.", linewidth=3)

    plt.plot(x_axis, np.cumsum(rero_avg) / np.sum(rero_avg), '-.', markersize=4,
             markevery=[30], label="ReRo avg.", linewidth=3)

    plt.legend()
    plt.xlim(0, 120)
    plt.ylim(0, 100)

    # Save figure
    plt.savefig("figures/avalibility.png")

    '''
if __name__ == "__main__":
    avalibility()

