from aip import AipOcr

APP_ID = '16418417'
API_KEY = 'oNQOtegx1gbSA77SrS9a4kFM'
SECRET_KEY = 'z5nBPshSwZ8PeXEsXl1nbnmOH6hlFjGh'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('C:\\Users\\HP\\Desktop\\image01.JPG')
result = client.basicGeneral(image)
print(result)