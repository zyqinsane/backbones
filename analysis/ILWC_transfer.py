import numpy as np
import pandas
from lib.rerouting_lib import compute_gst_sat_distance
from lib.latency_lib import load_locations
from sklearn.neighbors import BallTree, DistanceMetric
from geopy.distance import EARTH_RADIUS

def ILWC_transfer():
    altitude = 1150
    min_elev = 40
    orbits = 32
    sat_per_orbit = 50
    inclination = 53
    gst_file = "ixp_geolocation.csv"
    src_file = "WUP2018-F22-Cities_Over_300K_Annual.csv"

    # Load geo information
    sat_pos, gst_pos, src_pos = load_locations(altitude, orbits, sat_per_orbit,
                                               inclination, gst_file, src_file,
                                               time=15000)
    sat_tree = BallTree(np.deg2rad(sat_pos),
                        metric=DistanceMetric.get_metric("haversine"))

    sat_gst_ind_ixp, sat_gst_dist_ixp ,sat_gst_elev_ixp,sat_gst_projection_ixp = compute_gst_sat_distance(altitude,
                                                                 min_elev,
                                                                 gst_pos,
                                                                 sat_tree)

    print (sat_gst_dist_ixp)
    print ("========================")
    print (sat_gst_elev_ixp)
    print("========================")
    print(sat_gst_projection_ixp)

if __name__ == "__main__":
    ILWC_transfer()