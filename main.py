import argparse

from test import run_tests


def parse_args():
    parser = argparse.ArgumentParser(description='Graph colouring algorithms. '
                                                 'Returns table with time spent in calculations, selected algorithm, '
                                                 'number of used colours, information about completion and graph type.')
    parser.add_argument('--seed', '-s', type=int, default=False,
                        help='seed for the random number generator (default: new seed at every run)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='show coloured graphs during calculation')
    parser.add_argument('--path', '-p', default='test_cases.yml',
                        help='path to file describing test cases in YAML format (default: ./test_cases.yml). '
                             'See test_cases.yml for an example file.')

    args = parser.parse_args()
    seed = args.seed
    if not seed:
        seed = None
    return args.path, args.verbose, seed


if __name__ == '__main__':
    path, verbose, seed = parse_args()
    results = run_tests(path, verbose=verbose, seed=seed)
    print(results)
