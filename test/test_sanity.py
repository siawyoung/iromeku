#!/usr/bin/env python

import unittest
from iromeku import load_image, generate_clusters, get_dominant_colour, RGB


class SanityTest(unittest.TestCase):
    def test_small_jpg(self):
        rgb_values = load_image("test/small.jpg")
        clusters = generate_clusters(rgb_values, 0.1)
        colour = get_dominant_colour(clusters)
        self.assertEqual(
            colour, RGB(r=72, g=177, b=222)
        )
