# DUTDPr-repo
Repository for Deep Uncertainty in TD Prioritisation

# Directory Structure

Directories in this project are based on activities which introduced corresponding artefacts:

"1 - Mining": This directory is related to data mining and aggregation. Sanitised data mined from version 1.01 and version 2.00 of The Technical Debt Dataset (https://github.com/clowee/The-Technical-Debt-Dataset) can be found in a CSV file. The mining query can be found in an SQL file.

"2 - MOEA": This directory is related to MOEA, which is an algorithm runner, a defined JMetal problem, and its dependencies can be found in this directory. An algorithm runner and a defined problem are intended to be used with JMetalPy version 1.5.5.

"3 - Generated Solutions": This directory keep generated solutions from MOEA and Procedural Generation, which can store in corresponding subdirectories. A suffix "_VARs" on files indicates that files store the population's solution variables. A suffix "_FUN" on files indicates that files store objective functions of the population. Additionally, a NashPy script for verifying Nash Equilibria in examples in the publication is included in this directory. The NashPy script is intended to be utilised with NashPy 0.0.28.

"4 - Statistical Analysis": This directory stores scripts to calculate Improvability and Jaccard similarity of the population with "improvCalculator.py" and "JaccardCalculator.py", respectively. Statistical tests (Spearman R/Sapiro-Wilk/U-Mann Whitney) scripts utilised to produce evaluation results are uploaded here. 
