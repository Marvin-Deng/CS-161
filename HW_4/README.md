# HW 4
Graph coloring problem conversion to a CNF

## Running
```shell
# Create CNF file
python3 hw4.py

# Building RSAT solver
cd rsat_2.02_release
./build.sh
cd ..

# Running RSAT solver
./rsat_2.02_release/rsat graph1_3.cnf

./rsat_2.02_release/rsat graph1_4.cnf
```

## Clean Up
```shell
# Enable permissions if needed
chmod -x cleanup.sh

# Remove .cnf files
./cleanup.sh
```