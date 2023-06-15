# model-catalog
A collection of new &amp; noteworthy LLMs that can be run on consumer hardware

### Contibution Process

1. Clone the repo and create a new development branch
2. Create a new model JSON file and place it in `models/`
3. Validate your file against the JSON schema using the `validate.py` tool
4. Open a PR with your change

### `catalog.json`

A github action compiles all the `.json` files from the `models/` directory into the `catalog.json` file.
Do not modify it manually.