# ML_template
Template for Machine Learning model development. Designed for simpler model development use-case in mind (not DL).

## How to use it the template:

- The entry point for model training is **main.py**
- Implement custom metrics in **model/metrics**, custom models in **model/models**
- Implement custom data loading as an ETL pipeline in **model/etl**
   - Extractors are responsible for reading data (E.g. from disc or remote database) and converting into pythonic format such as numpy array or pandas datarame. Implement custom extractors in **model/etl/extract**
   - Transformers are lambdas that are applied to each case (could be also filters). Implement custom transforms in **model/etl/transform**
   - ETL consists of extrctor(s), a list of transforms and the loader component, which transforms the output of transformer chain to model-friendly format
- Use **config.yaml** to configure model training
- Add experimentation jupyter notebooks in **notebooks/**
- Add unit tests in **tests/** with file prefix unittest_*.py
- Add workflow automation using GitHub Actions in **.github/workfows/**

Testing workflow and branch protection rules are designed with simple gitflow brancing strategy in mind. When implementing a new feature branch out, commit new code, push new branch and merge it to main when the code is finalized and new unit tests are created.
