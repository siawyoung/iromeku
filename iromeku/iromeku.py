from __future__ import division
from math import sqrt
from PIL import Image
from collections import namedtuple
MYPY = False
if MYPY:
    from typing import NamedTuple, List, Any


"""
RGB is the public class meant for consumption.
Its RGB values are integers between 0 and 255, inclusive.
"""
RGB = namedtuple(
    "RGB", ["r", "g", "b"]
)  # type: NamedTuple('RGB', [('r', int), ('g', int), ('b', int)])


"""
RGBPoint is an internal class whose values are
normalized to a range between 0 and 1, inclusive.
"""
RGBPoint = namedtuple(
    "RGBPoint", ["r", "g", "b"]
)  # type: NamedTuple('RGBPoint', [('r', float), ('g', float), ('b', float)])


"""
YUVPoint is an internal class used as part of the kernel
for more closely matching Euclidean proximity with colour
perception similarity.
"""
YUVPoint = namedtuple(
    "YUVPoint", ["y", "u", "v"]
)  # type: NamedTuple('YUVPoint', [('y', float), ('u', float), ('v', float)])


ImageClusters = namedtuple(
    "ImageClusters", ["clusters"]
)  # type: NamedTuple('ImageClusters', [('clusters', List[List[RGBPoint]])])


def normalize_n_to_m(val, m, n):
    # type: (float, float, float) -> float
    """
    normalize_n_to_m normalizes a range of [0,m] to [0,n]
    """

    return (val / m) * n


def round_rgb(rgb):
    # type: (RGBPoint) -> RGB
    return RGB(r=round(rgb.r * 255), g=round(rgb.g * 255), b=round(rgb.b * 255))


def rgb_to_yuv(p):
    # type: (RGBPoint) -> YUVPoint
    return YUVPoint(
        y=p.r * 0.299 + p.g * 0.587 + p.b * 0.114,
        u=p.r * -0.147 + p.g * 0.289 + p.b * 0.436,
        v=p.r * 0.615 + p.g * 0.515 + p.b * 0.100,
    )


def colour_distance(p, q):
    # type: (YUVPoint, YUVPoint) -> float
    """
    colour_distance returns the Euclidean distance between 2 3-tuples.
    """

    return sqrt((p[0] - q[0]) ** 2 + (p[1] - p[1]) ** 2 + (p[2] - q[2]) ** 2)


def generate_clusters(pixels, distance_threshold):
    # type: (List[RGBPoint], float) -> ImageClusters
    """
    generate_clusters takes in a list of RGBPoints, and a cluster threshold,
    and returns a list of clusters of RGBPoints.

    All points in a cluster will all be within distance_threshold of the first
    point in the cluster. If no such cluster exists, a point will be
    put in a new cluster.
    """

    clusters = []  # type: List[List[RGBPoint]]
    for p in pixels:
        inserted = False
        # for each point, check if it's close enough to the first element in any existing bucket
        for c in clusters:
            if colour_distance(rgb_to_yuv(c[0]), rgb_to_yuv(p)) <= distance_threshold:
                c.append(p)
                inserted = True
                break
        if not inserted:
            clusters.append([p])
    return ImageClusters(clusters=clusters)


def get_k_largest_lists(lists, k):
    # type: (List[List[Any]], int) -> List[List[Any]]
    """
    get_k_largest_lists takes in a list of lists, and returns
    the k largest lists by length, sorted in descending order by length.

    E.g. get_k_largest_lists([[1,2,3], [1], [1,2]], 2) => [[1,2,3], [1,2]]
    """

    return sorted(lists, key=len, reverse=True)[:k]


def mean_rgb(pixels):
    # type: (List[RGBPoint]) -> RGBPoint
    """
    mean_colour takes a list of points, and returns a new point whose values
    are the arithmetic mean of each band.
    """

    sums = [0, 0, 0]
    for p in pixels:
        sums[0] += p.r
        sums[1] += p.g
        sums[2] += p.b
    return RGBPoint(
        r=sums[0] / len(pixels), g=sums[1] / len(pixels), b=sums[2] / len(pixels)
    )


def load_image(path):
    # type: (str) -> List[RGBPoint]
    """
    load_image takes in an image path and returns an ImageClusters instance,
    which can be used by get_dominant_colour
    """
    im = Image.open(path, "r")
    pixel_values = []  # type: List[RGBPoint]
    for x in im.getdata():
        # the RGB values returned by PIL are in the range [0,255]
        # which we normalize to [0,1] for later conversion to YUV
        rgb_point = RGBPoint(
            r=normalize_n_to_m(x[0], 255, 1),
            g=normalize_n_to_m(x[1], 255, 1),
            b=normalize_n_to_m(x[2], 255, 1),
        )
        pixel_values.append(rgb_point)
    return pixel_values


def get_dominant_colour(clusters):
    # type: (ImageClusters) -> RGB
    """
    get_dominant_colour takes in an ImageClusters instance and returns
    a dominant colour.
    """
    largest_cluster = get_k_largest_lists(clusters.clusters, 1)
    mean = mean_rgb(largest_cluster[0])
    return round_rgb(mean)
