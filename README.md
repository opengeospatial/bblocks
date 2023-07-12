# Building Blocks

Bootstrap page containing an overview of building blocks and a building blocks register.

[See it live here](https://blocks.ogc.org/)

## Local build/test

You need a functioning Docker environment to build the Building Blocks Register locally. 
All the output files will be generated under `build-local`.

1. Clone the repository: `git clone --recurse-submodules`
2. Update submodules: `git submodule update --recursive --remote`
3. Build the Register:
   ```shell
   # Process building blocks
   docker run --pull=always --rm --workdir /workspace -v $(pwd):/workspace --user $UID \
      ghcr.io/opengeospatial/bblocks-postprocess  --clean true \
      --items-dir registereditems/ \
      --generated-docs-path build-local/generateddocs \
      --annotated-path build-local/annotated-schemas \
      --register-file build-local/register.json \
      --test-outputs build-local/tests \
      --base-url https://opengeospatial.github.io/bblocks/ 
    # Build Slate docs
    docker run --pull=always --rm \
      -v "$(pwd)/build-local/generateddocs/slate:/srv/slate/source" \
      -v "$(pwd)/build-local/generateddocs/slate-build:/srv/slate/build" \
      dockerogc/slate build
    ```
4. Run a web server locally, on this folder. For instance: `npx http-server`
5. Access it on a browser: `http://127.0.0.1:8080`.

If you need to rebuild the Register, just run steps 2 and 3.

## License

This code is released under [Apache 2.0](./LICENSE) license.

## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md).