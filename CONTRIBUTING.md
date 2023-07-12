# Contributing to the OGC Building Blocks Register

There are two main ways to get your contributions in the Building Blocks Register:

1. Directly on this repository, through 
   [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
2. If you would like to contribute a set of Building Blocks, and especially if several people need to 
   collaborate while developing them, using the [Building Blocks template repository](https://github.com/opengeospatial/bblock-template).

The [Building Blocks template repository](https://github.com/opengeospatial/bblock-template) contains instructions and
information on the general structure of a Building Block and how it is postprocessed and included in the OGC Building
Blocks Register.

## Using Pull Requests

To create or update Building Blocks in this repository, you need to:

1. [Fork](https://github.com/opengeospatial/bblocks/fork) this repository.
2. Add your changes to your fork.
3. [Create a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
   to apply them to the main repository.

The process is very similar to using the Building Blocks template repository, bearing in mind that:

* The [Building Block structure](https://github.com/opengeospatial/bblock-template/blob/master/README.md#building-block-structure)
  (sources) is the same as in the template.
* The sources root directory is `registereditems/`.
* There is no need for submodules or `bblock-config.yaml`, which are only relevant with using external repositories.

## Using the Building Blocks template repository

The template's own [README.md](https://github.com/opengeospatial/bblock-template/blob/master/README.md) has all the
information necessary to start creating Building Blocks, including a step-by-step description of how to add them
to the main Building Block Registry.