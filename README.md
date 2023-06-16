# model-catalog
Standardized JSON descriptions of newly released Large Language Models (LLMs).

### `catalog.json`

A github action compiles any `.json` file in the `models/` directory and creates the `catalog.json` file.
The contents of each JSON file as well as catalog.json is validated using a json schema.

### Contibution Process

You're invited to help catalog the models available out there.

1. Clone this repo and create a new development branch.
2. Create a new model JSON file and place it in `models/`.
3. Validate your file against the expected JSON schema using the `validate.py` tool or by running `createCatalog.py`.
4. Open a PR with your change.
5. Ensure all github actions completed successfully.

Note: Do not modify `catalog.json` manually, and do not include it in your commits.