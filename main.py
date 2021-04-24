from test import run_tests


if __name__ == '__main__':
    test_cases_path = 'test_cases.yml'
    results = run_tests(test_cases_path, verbose=True, seed=42)
    print(results)
