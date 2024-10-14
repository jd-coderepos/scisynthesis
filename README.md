<div align="center">
 <h1>ORKG Synthesis Dataset</h1>
</div>

[//]: # (<h3>Science Synthesis</h3>)

<div align="center">
 <img src="images/llms4synthesis-logo.png" width="800" height="170"/>
</div>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

</div>

<div style="color:red;">This work is accepted for publication at JCDL-2024 conference.</div>

### What is the ORKG Synthesis Dataset?

We develop a methodology to collect and process scientific papers into a format  ready for synthesis using the Open Research Knowledge Graph, a multidisciplinary platform that facilitates the comparison of scientific contributions. Where later, we introduce new synthesis types —-  paper-wise, methodological, and thematic —- that focus on different
aspects of the extracted insights. Utilizing Mistral-7B and GPT4 , we generate a large-scale dataset of these syntheses.  The established nine quality criteria for evaluating these syntheses, assessed by both an automated LLM evaluator (GPT-4) and a human-crowdsourced survey.

### Directories

* `corpus`: Contains ORKG Synthesis dataset for bot GPT-4 and Mistral-7B for three synthesis objectives (paper-wise, methodological, and thematic). Also Prolific Human Survey Results.
* `gpt-4 synthesis-evaluator`: Contains `Evaluation System Prompt` and evaluator script.
* `orkg-comparison-data-gen-scripts`: Synthesis generation scripts.
* `synthesis-generation-prompts`: Synthesis generation prompts for paper-wise, methodological, and thematic objectives.

### Prolific Survey
The [Prolific Survey Participant Demographics](corpus/prolific/README.md) available at Table 1 in the `corpus/prolific` directory.

Also the [average human and automatic (LLM) evaluation](corpus/prolific/README.md) available at Table 2 in the `corpus/prolific` directory, representing average human and LLM evaluation scores by characteristic comparisons. For each domain/characteristic, the human scores are an average of 18 judgements (6 syntheses (2 samples x 3 synthesis types) x 3 participants) while the auto scores are an average of 6 judgements (6 syntheses (2 samples x 3 synthesis types) x 1 LLM evaluation).

### LLMs4Synthesis
The **LLMs4Synthesis** framework on top of this dataset is available at  https://github.com/HamedBabaei/LLMs4Synthesis.


### Citation
Preprint:
```
@misc{giglou2024llms4synthesisleveraginglargelanguage,
      title={LLMs4Synthesis: Leveraging Large Language Models for Scientific Synthesis},
      author={Hamed Babaei Giglou and Jennifer D'Souza and Sören Auer},
      year={2024},
      eprint={2409.18812},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.18812},
}
```
