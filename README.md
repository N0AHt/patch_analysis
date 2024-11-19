# Patch Clamp Analysis

Toolkit for loading and handling patch clamp data recorded via NI-DAQs.  
- Loads patch clamp .csv files, handles voltage, current, stimulation, and metadata information
- Organizes data into dataframe: session->cell->protocol->recording
- Analysis and plotting for common patch clamp investigations

---

## Installation

Clone the github repo and navigate into it 

```bash
$ cd <directory_where_repo_will_be_cloned> # i.e. desktop or github, wherever you want the code to be
$ git clone <repo_url> # download repo
$ cd <repo>
```

Create a new mamba environment and install python

```bash
$ mamba create -n patch_analysis python, ipykernel # env will be called patch_analysis. Add ipykernel if using jupyter notebooks
$ mamba activate patch_analysis
```

Install the package and requirements

```bash
$ pip install -e . # Install in editable mode for now
$ pip install -r requirements.txt
```

---

## Usage