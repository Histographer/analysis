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

###Image
TODO

###Ranking
TODO

## Testing
​
###Image
TODO

###Ranking
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
​
TOOD
How and where to add or update documentation (e.g. README.md, API.md, Javadoc)
​
## Style guide
​
All python code in this repository is written to adhere to the PEP 8 style guide. 
Functions contain docstrings following the reStructuredText docstring format.
​
## Versioning
​TODO
State that we use semantic versioning. Explain that version numbers should be updated before pushing to master.