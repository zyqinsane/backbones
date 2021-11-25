import os
import pickle
import time
from argparse import ArgumentParser
from multiprocessing import Pool

import numpy as np
from sklearn.neighbors import BallTree
from sklearn.neighbors import DistanceMetric

from lib.latency_lib import src_dst_optimization, LIGHT_IN_FIBER, \
    LIGHT_IN_VACUUM, gsts_optimization, load_locations
from lib.rerouting_lib import compute_src_dst_latency, \
    inactive_to_closest_active, gst_gst_terrestrial_distance, \
    src_nearest_gst_distance, delaunay_pos_graph, compute_gst_sat_distance, \
    compute_sat_sat_distance, add_rerouting_to_inactive
from lib.latency_lib import make_test_constellation
import lib.satellite_topology
import csv

altitude = 1300
min_elev = 40
orbits = 32
sat_per_orbit = 50
inclination = 53
NUM_DEACTIVATE = 20
gst_file = "/ccr-submission-code/data/raw/ixp_geolocation.csv"
src_file = "/ccr-submission-code/data/raw/WUP2018-F22-Cities_Over_300K_Annual.csv"

class Constellation(): # 定义一个星座类
    def __init__(self):
        pass
    def rotate(self): # 定义卫星的旋转属性
        self.sat_pos1,self.gst_pos1,_ = load_locations(altitude, orbits, sat_per_orbit,inclination,gst_file,src_file,time = t)

    def compute_latency(self): # 计算每一个给定时间下静态拓扑下的时延
        pass
    def state_update(self): # 更新地面站的可用状态 state = 0 / 1


    def avalibility(self): # 求解当前拓扑下的组网可用性7





if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("path_control", type=int, default=3,
                        help="path control degree in the experiment.")
    parser.add_argument("inactive_stations", type=str,
                        help="Pickle file containing the lists of inactive GSTs"
                             "due to rainfall. Produced by "
                             "`rainfall_to_inactive_gst.py`")
    parser.add_argument("out", type=str,
                        help="folder of results")
    parser.add_argument("--cores", type=int, default=1,
                        help="Number of cores to use in the computation.")

    args = parser.parse_args()

    with open(args.inactive_stations,'rb') as infile:
        inactive_list = pickle.load(infile)

    for t in range(1000):
        StarA = Constellation()
        a = StarA.rotate()
        while (t % 50 == 0):
            StarA.state_update()
        b = StarA.compute_latency()

    StarA.run(args.path_control,[-1],-1,args.cores,args.out,inactive_list)

