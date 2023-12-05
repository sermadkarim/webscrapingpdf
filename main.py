from Utils.paper_downloader import PaperDownloader

if __name__ == "__main__":
    url = 'https://www.aqa.org.uk/find-past-papers-and-mark-schemes?fbclid=IwAR050K1AJ7ej8hMDKweXl4Th9maH4PUYxgOa7Wf9J-GVUHRzBVm_pgwvZcU'
    downloader = PaperDownloader(url)
    downloader.download_papers()
