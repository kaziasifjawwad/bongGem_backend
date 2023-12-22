import gdown


def download():
    file_id = '18rKvgf2-NRusGyW5QkpzgE0ZVgDtLNYd'
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'weight.zip'
    gdown.download(url, output, quiet=False)


if __name__ == '__main__':
    download()
