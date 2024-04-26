# HW 4
Graph coloring problem conversion to a CNF

## Running
```shell
# Create CNF files
python3 hw4.py

# Building RSAT solver
cd rsat_2.02_release
./build.sh
cd ..

# Running RSAT solver for questions 1 - 3
./rsat_2.02_release/rsat graph1_3.cnf

./rsat_2.02_release/rsat graph1_4.cnf

# Running RSAT solver for questions 4
./rsat_2.02_release/rsat graph2.cnf
```

## Clean Up
```shell
# Enable permissions if needed
chmod -x cleanup.sh

# Remove .cnf files
./cleanup.sh
```