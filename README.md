![version](https://img.shields.io/badge/version-0.0.1-blue)

# model-catalog

A collection of standardized JSON descriptors for Large Language Model (LLM) model files.

#### `<model_name>.json`

A single JSON file describes a model, its authors, additional resources (such as an academic paper) as well as available model files and their providers.

Version `0.0.1` of this format attempts to capture an informative set of factors including:
- model size (e.g. `7B`, `13B`, `30B`, etc.)
- model architecture (such as `Llama`, `MPT`, `Pythia`, etc.)
- model file format (e.g. `ggml`) as well as quantization format (e.g. `q4_0`, `q4_K_M`, etc.)

See examples: [`guanaco-7b.json`](models/guanaco-7b.json), [`samantha-1.1-llama-7b.json`](models/samantha-1.1-llama-7b.json), [`Nous-Hermes-13b.json`](models/Nous-Hermes-13b.json).

#### `catalog.json`

A Github action picks up `.json` files from the `models/` directory and merges them into one `catalog.json` file.
The contents of each JSON file is validated by another Github action using a JSON schema.

## Contribution Process

You're invited to help catalog models and improve upon this description format.

1. Fork this repo and create a new development branch.
2. Create a new model JSON file and place it the `models/` directory.
3. Validate your file against the expected JSON schema using the `validate.py` tool or by running `createCatalog.py`.
4. Open a PR with your change.
5. Ensure all Github actions complete successfully.

Note: Do not modify `catalog.json` manually.
