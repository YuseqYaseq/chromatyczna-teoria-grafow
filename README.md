# Chromatyczna teoria grafów
Chromatic graph theory - graph colouring algorithms.

## Usage
usage:
```
> python main.py [-h] [--seed SEED] [--verbose] [--path PATH]
```
Graph colouring algorithms. Returns table with time spent in calculations,
selected algorithm, number of used colours, information about completion and
graph type.

optional arguments: \
 -h, --help            show this help message and exit \
 --seed SEED, -s SEED  seed for the random number generator (default: new
                        seed at every run) \
 --verbose, -v         show coloured graphs during calculation \
 --path PATH, -p PATH  path to file describing test cases in YAML format
                        (default: ./test_cases.yml). See test_cases.yml for an
                        example file.

