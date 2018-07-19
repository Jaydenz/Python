# import requests, json

# API_KEY = {'API-Key': '3L5RSCUDCPWDYA7JEGPVZVIKZQ6TK2OMB2IA'}

# r1 = requests.get('https://api.vultr.com/v1/snapshot/list', headers=API_KEY)
# snapshot_list = json.loads(r1.text)

# r2 = requests.get('https://api.vultr.com/v1/server/list', headers=API_KEY)
# server_list = json.loads(r2.text)

# os_list = json.loads(requests.get('https://api.vultr.com/v1/os/list').text)



from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'./temp.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)