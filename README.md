# Iromeku

[![Build Status](https://travis-ci.com/carousell/DataAccessLayer.svg?token=EF9qHkSmyt2BrPXZdP6q&branch=master)](https://travis-ci.com/carousell/DataAccessLayer)

> 色めく (hiragana いろめく, rōmaji iromeku) 1. to become lively 2. to become roused 3. to look arousing

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
clusters = generate_clusters(rgb_values, 0.1)
colour = get_dominant_colour(clusters)
print(colour.r, colour.g, colour.b)
```

`0.1` in the second argument of `generate_clusters` refers to the threshold under which we consider two colours to be similar. Try adjusting the threshold for different results.

## Contributing

The library is type hinted using the comment-based syntax for backward compatibility with Python 2. Tests are run using tox.

## TODO

- [ ] Add example images
- [ ] Add support for generating complimentary colours
- [ ] Add support for selective sampling (e.g borders + center)
- [ ] Improve clustering algorithm

## License

MIT License
