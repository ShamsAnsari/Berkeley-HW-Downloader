# PDF Downloader

This project contains a Python script that scrapes a given website for links to PDF files and downloads them.

## Dependencies

- Python 3.6 or higher
- `requests`
- `beautifulsoup4`

You can install the necessary libraries with pip:

```
pip install requests beautifulsoup4
```

## Usage

To run the script, navigate to the directory containing the script in the command line, then run the script with the target website and output directory as arguments.

```sh
python pdf_downloader.py <target_url> <output_directory>
```

Replace `<target_url>` with the URL of the website you want to scrape, and `<output_directory>` with the name of the directory where you want to save the downloaded PDFs.

For example:

```sh
python pdf_downloader.py https://eecs16b.org/ EECS16B
```

This command would scrape the site at `https://eecs16b.org/` for PDFs, then save them to a directory named `EECS16B`.

## Note

Please ensure you have the necessary rights and permissions to scrape and download content from your target website. Heavy scraping activity can disrupt the operation of a website, and many websites' terms of service disallow this kind of activity. Use this script responsibly.