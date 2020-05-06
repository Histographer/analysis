# Contributing
​
This file contains information that you should familiarize yourself with before making changes to this repository. 
It is primarily intended to help a potential future team get started with development, rather than to help outsiders make contributions.

See also [README.md](https://github.com/histographer/histographer-analysis/blob/master/README.md)
​
​
## Useful information
​
`histographer-analysis` is divided into two main services: `image` and `ranking`

### Image
`image` is a collection of statistic analysis functions that can be run on masked images. Along with this, there are
fetching methods for getting information from a Cytomine server, and handling data.

In the image analysis pipeline, images histological images are first segmented into parts, using functions in `segment`.
Then, the segments are treated as masks to analyse color features, using `color` and `analysis`.

Images can be fetched directly from a Cytomine server, using methods in `fetch`. Arranging this data in an `ImageData`
object allows alternative representations to be generated only when needed, and cached for later use. Since images take
up a lot of memory, `ImageData` objects should be deleted after use, only keeping one in memory at a time.

### Ranking
TODO

## Testing
​
### Image
Run tests by fetching images (locally or from a server) and running them through the algorithms using functions in
`high_level`. This can mostly be done by running `__main__` clauses in the relevant files. Since there's no measure of
performance, use some common sense and possibly independent results to verify that the algorithms are working properly.

### Ranking
​`ranking` contains a handful of functions for evaluating the performance of ranking algorithms.
Firstly, `mock.py` contains the functions `generate_mock_comparisons` and `generate_mock_comparisons_btl` which generate
`n_comparisons` comparisons with either a flat `error_rate` or according to the Bradley-Terry-Luce model, sampled from
a population [1, 2, ..., `n_objects`]. 

A general performance measure of a given algorithm is how well it is able to
reconstruct the original order of the objects from these comparisons. Repeated simulations, along with plots of the
results, of this testing can be performed by running `e_vs_n_comparisons` found in `error.py`. The function repeatedly
generates a variable number of comparisons, calculates a ranking based on the comparisons using every algorithm given in
`algorithms`. The errors for these rankings are plotted against the number of comparisons supplied to the algorithms.
The comparisons are generated according to the BTL model, but this can be changed to a flat error-rate method simply by
changing the function call on the 7th line of the function implementation from `generate_mock_comparisons_btl` to 
`generate_mock_comparisons` and specifying an `error_rate`.

## Documentation
Documentation is found in `README.md` and in this file only.​
​
## Style guide
All python code in this repository is written to adhere to the PEP 8 style guide. 
Functions contain docstrings following the reStructuredText docstring format.
​
## Versioning
`histographer-analysis` uses semantic versioning. See guidelines [here](https://semver.org/).
