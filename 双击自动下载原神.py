import requests

url = 'https://autopatchcn.yuanshen.com/client_app/download/launcher/20230625145853_3mVP4q9cR5z7F88A/mihoyo/yuanshen_setup_20230619213504.exe'

# 设置请求头信息,伪装成浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 获取响应内容
data = response.content

# 生成文件名
filename = url.split('/')[-1]

# 保存文件
with open(filename, 'wb') as f:
    f.write(data)

print('文件下载完成:', filename)
