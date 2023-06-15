# model-catalog
A collection of new &amp; noteworthy LLMs that can be run on consumer hardware

### `catalog.json`

A github action compiles all the `.json` files from the `models/` directory and creates the `catalog.json` file.
Do not modify it manually, and do not include it in your commits.

### Contibution Process

1. Clone this repo and create a new development branch.
2. Create a new model JSON file and place it in `models/`.
3. Validate your file against the JSON schema using the `validate.py` tool or by running `createCatalog.py`.
4. Open a PR with your change.
5. Ensure all github actions completed successfully.
