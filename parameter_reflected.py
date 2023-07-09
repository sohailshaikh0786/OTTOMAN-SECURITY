import argparse
import requests
from urllib.parse import urlparse, parse_qs

def find_reflected_params(url):
    response = requests.get(url)
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    reflected_params = []
    for param, values in query_params.items():
        for value in values:
            if value in response.text:
                reflected_params.append((param, value))

    return reflected_params

def check_reflected_params(urls):
    for url in urls:
        reflected_params = find_reflected_params(url)
        if len(reflected_params) > 0:
            print(f"URL: {url}")
            print("Reflected URL parameters:")
            for param, value in reflected_params:
                print(f"Parameter: {param}\tValue: {value}")
            print()
        else:
            print(f"no reflected URL parameters found in: {url}\n")

def main():
    parser = argparse.ArgumentParser(description='Check for reflected URL parameters in the response.')
    parser.add_argument('file', type=str, help='Path to the file containing URLs')
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    check_reflected_params(urls)

if __name__ == '__main__':
    main()
