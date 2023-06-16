# model-catalog
Standardized JSON descriptions of newly released Large Language Models (LLMs).

### `catalog.json`

A Github action picks up `.json` files from the `models/` directory and merges them into one `catalog.json` file.
The contents of each JSON file is validated by another Github action using a JSON schema.

### Contibution Process

You're invited to help catalog the models available out there.

1. Clone this repo and create a new development branch.
2. Create a new model JSON file and place it the `models/` directory.
3. Validate your file against the expected JSON schema using the `validate.py` tool or by running `createCatalog.py`.
4. Open a PR with your change.
5. Ensure all Github actions complete successfully.

Note: Do not modify `catalog.json` manually.