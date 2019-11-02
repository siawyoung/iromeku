# Iromeku

Iromeku is a library to extract a colour palette from a given image.

The implementation is heavily inspired by the Stack Overflow answer here: ![How does
the algorithm to color the song list in iTunes 11
work?](https://stackoverflow.com/questions/13637892/how-does-the-algorithm-to-color-the-song-list-in-itunes-11-work#answer-13675803)

The way it works is by clustering similar colours together, based on the
Euclidean distances of the pixel's value in the YUV colour space, which more
closely approximates colour perception.

## Getting Started

``` shell
$ pip install iromeku
```

``` python
from iromeku import load_image, generate_clusters, get_dominant_colour

rgb_values = load_image("test.jpg")
# experiment with different threshold values for better/worse results
clusters = generate_clusters(rgb_values, 0.1)
colour = get_dominant_colour(clusters)
print(colour.r, colour.g, colour.b)
```

## TODO

- [ ] Add example images
- [ ] Add support for generating complimentary colours
- [ ] Add support for selective sampling (e.g borders + center)
- [ ] Improve clustering algorithm
