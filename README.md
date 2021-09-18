# Traffic Signal Optimization
Traffic congestion is a recurring problem in almost all major cities in the world and continues to increase with economic growth and population of the city. The existing transportation system is strained by the increasing traffic demand, especially during peak hours. Traffic control is an efficient method to reduce the traffic delay and improve the overall efficiency of a traffic network. Traffic signals are an effective means of controlling the traffic at intersections. However, the traffic signal timings are designed based on methods which do not account for the variability in the traffic conditions and could therefore result in non-optimised signal timings. Non-optimised signal timings result in unnecessary delays, and could contribute to fuel wastage and environmental degradation.

This project is an attempt to improve the efficiency of traffic signal control and reduce traffic delay at intersections by using various optimization algorithms like Ant Colony Optimization algorithm (ACO) and Genetic algorithm (GA). The objective is to optimize signal timings at isolated signals and coordinated signals, such that the traffic network efficiency is improved, and traffic delays are reduced

## Implemented algorithms
* Ant Colony Algorithm
* Genetic Algorithm

## Requirements
* Install [Git](https://git-scm.com/downloads/ "Git Downloads")
* Install [Python3](https://www.python.org/downloads/ "Python Downloads")
* Run `pip install requirements.txt` to install Numpy, Matplotlib, Tkinter

It is better to install the above requirements in a virtual environment

## Create a virtual environment
* Run `pip install virtualenv` to install virtualenv module
* Create a new virtual environment using `virtualenv myenv`
* Use `virtualenv -p /usr/bin/python3 myenv` to specify Python3 as the default interpreter
* Activate the virtual environment with `source myenv/bin/activate`
* Deactivate the virtual environment with `deactivate`

## Usage
* Clone the repository using `git clone https://github.com/Abhirams2020/Traffic-Signal-Optimization.git`
* Run `python3 main.py` to see the results.
