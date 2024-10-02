[![Python Application Test with Github Actions by Peter](https://github.com/cpyang123/DE-W4/actions/workflows/test.yml/badge.svg)](https://github.com/cpyang123/DE-W4/actions/workflows/test.yml)


# DE-W4
This is mini project 4 of the IDS 706 class, we're generating a preliminary analysis of a sample housing price data. 

This project is different from W2, with additional CI/CD process to test for different python versions.

See the report.md file for the generated report. [Report](./report.md)

Project Structure:
- Makefile: Contains commands to build, test, deploy and generates the report in the project
- main.py contains the main analysis that creates the figures and analysis
- requirements.txt contains the main libraries requirements
- test_main.py contains the tests for the main functions
- train.csv is the main data we're using here
- .devcontainer contains the Dockerfile and the devcontainer.json file for container environment
