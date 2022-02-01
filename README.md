# Fibonacci API project

This project contains a single API endpoint that, for a given integer, returns the closest Fibonacci number and the two Fibonacci numbers adjacent on either side of that number.  

## How to clone the repository

This repository can be cloned with the following command: 
```
git clone https://github.com/alessandromoscato/fibonacci-api.git
```

## How to install dependencies

Dipendencies can be installed by launching the `00_build.sh` bash script.

## How to run the project

The project can be run by launching the `01_run.sh` bash script.

## How to run unit tests

Unit tests for this project can be run by launching the `02_test.sh` bash script.

## Some comments on the algorithm

It is worth noting a couple of things regarding the algorithm:

 - If the input number is 0, there is no Fibonacci number to the left of 0, therefore the API will return `[0, None, 1]`.
 - If the input number is 1, both the second and the third elements of the Fibonacci sequence can be taken into account. The third one has been chosen arbitrarily, therefore the API will return `[1, 1, 2]`.
 - Some input numbers (e.g. 4 and 17) are equally distanced between two Fibonacci numbers. In such cases, the closest Fibonacci number will be considered the previous one. For instance, for input number 17, the closest Fibonacci number will be considered 13, and the API will return `[13, 8, 21]`.
