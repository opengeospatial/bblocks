# Building Blocks

OGC Building Blocks - register of OGC specification elements packaged as FAIR resources.

OGC Building Blocks and a building blocks register.
For more information [read the docs](https://ogcincubator.github.io/bblocks-docs/)

[See it live here](https://blocks.ogc.org/register)

## Validation Reports
[Summary](https://opengeospatial.github.io/bblocks/tests/report.html)

## Local build/test

You need a functioning Docker environment to build the Building Blocks Register locally. 
All the output files will be generated under `build-local`.

1. Clone the repository: `git clone https://github.com/opengeospatial/bblocks.git --recurse-submodules`
2. Change into the repository folder: `cd bblocks` 
3. Update submodules: `git submodule update --recursive --remote`
4. Build the Register:
   ```shell
   # Process building blocks
   docker run --pull=always --rm --workdir /workspace -v $(pwd):/workspace --user $UID \
      ghcr.io/opengeospatial/bblocks-postprocess  --clean true \
      --items-dir registereditems/ \
      --base-url https://opengeospatial.github.io/bblocks/ 
    # Build Slate docs
    docker run --pull=always --rm --user $UID \
      -v "$(pwd)/build-local/generateddocs/slate:/srv/slate/source" \
      -v "$(pwd)/build-local/generateddocs/slate-build:/srv/slate/build" \
      dockerogc/slate build
    ```
5. Run a web server locally, on this folder. For instance: `npx http-server`
6. Access it on a browser: `http://127.0.0.1:8080`.

If you need to rebuild the Register, just run steps 2 and 3.

## License

This code is released under [Apache 2.0](./LICENSE) license.

## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md).
