import os


def genREADME():
    head = [
        '# jkcrawler',
        '',
        '使用 Scrapy 写成的 JK 爬虫，图片源自哔哩哔哩、Tumblr、Instagram，以及微博、Twitter (待完成)',
        '',
        '启动爬虫：',
        '',
        '在 Windows 上，需要在 PowerShell 中执行以下命令',
        '',
        '```shell script',
    ]

    if os.path.exists('data/update.md'):
        with open('data/update.md') as f:
            update = f.read().rstrip()
        head.insert(1, update)
        head.insert(1, '')

    if not os.path.exists('data/'):
        os.mkdir('data')
    os.system('scrapy list > data/scrapylist.txt')
    with open('data/scrapylist.txt') as f:
        spiders = f.read().splitlines()
    lines = ['scrapy crawl {spider} -o data/{spider}.jsonlines'.format(spider=spider) for
             spider in spiders]

    tail = [
        '```',
        '',
        '若要在下一次启动爬虫时恢复工作进度，则需要在命令后面加上 `-s JOBDIR=crawls/{spider_name}`',
        '',
    ]

    with open('README.md', 'w') as f:
        f.write('\n'.join(head + lines + tail))


if __name__ == '__main__':
    genREADME()