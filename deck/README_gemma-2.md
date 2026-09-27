# Saif presentation artifact

The existing deck remains unchanged. The `_gemma-2` evaluation produces [results_gemma-2.json](../results_gemma-2.json), which can be used to generate a separately named deck when the repository's Node presentation dependency is installed:

```bash
node deck/build_deck.js results_gemma-2.json deck/Team4_Prompt_Optimization_gemma-2.pptx
```

The current environment does not contain `node_modules` or a package manifest for `pptxgenjs`, so the command was not run here. No existing presentation file was overwritten.
