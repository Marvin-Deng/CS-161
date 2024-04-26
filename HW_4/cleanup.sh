#!/bin/bash

# Find .cnf files and remove them
find . -maxdepth 1 -name "*.cnf" -type f -exec rm {} \;
