rm out.json
scrapy crawl pscrape
python jsonInterpret.py > out.txt
nvim out.txt
