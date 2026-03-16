# fragmentation-esnm

Code repository accompanying the publication entitled "Hierarchical fragmentation of regular islands in a discontinuous nontwist map".

This project contains the code to generate and plot all the data from all figures.

## Requirements

All the data in this paper have been generated using the [pynamicalsys](https://pynamicalsys.readthedocs.io/en/latest/index.html) package, a Python toolkit for the analysis of dynamical systems. Install the required Python packages with

    pip install -r requirements.txt


## Generating the data

All the data will be stored in a directory called `data/` that is automatically created by the Python scripts.

### Figures 1 and 2

The data for Figs. 1 and 2 are generated in the `Plots.ipynb` notebook (cells labeled *Fig. 1* and *Fig. 2*).  

These datasets are not stored in the repository and are produced when the notebook is executed.

### Figure 3

To generate the escape time data from Fig. 3, run the script `escape_times.py`:

    python escape_times.py

*Note*: This simulation takes hours to finish.

Similarly, to generate the SALI data, run

    python grid_sali.py

*Note*: This simulation takes hours to finish.

### Figure 4

To generate the data from Fig. 4, run the script `cgbd_sali.py`:

    python cgbd_sali.py

*Note*: This simulation takes hours to finish.

### Figure 5

To generate the data from Fig. 5, run the script `lle_history.py`:

    python lle_history.py

*Note*: This simulation takes days to finish.

### Figure 6

The data for Fig. 6 is generated in the `Plots.ipynb` notebook (cell labeled *Fig. 6*).

These datasets are not stored in the repository and are produced when the notebook is executed.

### Figure 7

To generate the data from Fig. 5, run the script `finite_time_rte.py`:

    python finite_time_rte.py

*Note*: This simulation takes days to finish.

### Figure 8

The data for Fig. 8 is generated in the `Plots.ipynb` notebook (cell labeled *Fig. 8*).

These datasets are not stored in the repository and are produced when the notebook is executed.

## Plotting the figures

After generating all required datasets, run the cells in the Jupyter notebook `Plots.ipynb` to reproduce the figures from the paper.

The figures will be saved in a directory called `figures/`, which is created automatically by the notebook.



## Contact

For questions or feedback, feel free to [email me](mailto:rolim.sales.m@gmail.com).

## Acknowledments

This project was financed, in part, by the São Paulo Research Foundation (FAPESP, Brazil), under process number 2023/08698-9.

## Disclaimer

As opiniões, hipóteses e conclusões ou recomendações expressas neste material são de responsabilidade do(s) autor(es) e não necessariamente refletem a visão da Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP, Brasil).

The opinions, hypotheses, and conclusions or recommendations expressed in this material are the sole responsibility of the author(s) and do not necessarily reflect the views of the São Paulo Research Foundation (FAPESP, Brazil).
