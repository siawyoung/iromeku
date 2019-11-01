# Iromeku

This is a Python 3 implementation of the Stack Overflow answer here: ![How does
the algorithm to color the song list in iTunes 11
work?](https://stackoverflow.com/questions/13637892/how-does-the-algorithm-to-color-the-song-list-in-itunes-11-work#answer-13675803)

This is a general purpose library to extract the dominant and complimentary
colours from a given image.

The way it works is by clustering similar colours together, based on the
Euclidean distances of the pixel's value in the YUV colour space, which more
closely approximates colour perception.

## Getting Started

``` python
from iromeku import load_image, generate_clusters, get_dominant_colour

rgb_values = load_image("test.jpg")
# experiment with different threshold values for better/worse results
clusters = generate_clusters(rgb_values, 0.1)
colour = get_dominant_colour(clusters)
print(colour.r, colour.g, colour.b)
```

## TODO

- [] Add support for generating complimentary colours
- [] Add support for selective sampling (e.g borders + center)
- [] Improve clustering algorithm
