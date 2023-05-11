import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
import argparse

def get_command_line_arguments():
    parser = argparse.ArgumentParser(description='Download PDFs from a website.')
    parser.add_argument('url', type=str, help='The URL to scrape for PDFs.')
    parser.add_argument('dir', type=str, help='The directory to save the PDFs.')
    args = parser.parse_args()
    return args.url, args.dir

def download_pdf(directory, link):
    response = requests.get(link, stream=True)
    file_name = link.split("/")[-1]
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'wb') as pdf:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)

def get_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('a', href=True)

    pdf_links = []
    for tag in tags:
        link = urllib.parse.urljoin(url, tag['href']) # to handle relative links
        if link.endswith('.pdf'):
            pdf_links.append((link, tag.text))

    return pdf_links

def main():
    url, base_dir = get_command_line_arguments()

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    pdf_links = get_pdf_links(url)

    for link, text in pdf_links:
        print(f'Link: {link}, Text: {text}')
        download_pdf(base_dir, link)

if __name__ == "__main__":
    main()
