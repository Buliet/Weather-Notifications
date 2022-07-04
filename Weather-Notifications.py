import requests
import datetime

def bark_push(data):
    # 填写 bark url
    url = "https://api.day.app/xxx/"
    msg = '预警/' + data + "?group=Weath"
    msg_url = url + msg
    res = requests.get(msg_url)
    ret = res.json()
    print(res.text)
    if ret['message'] == 'success':
        print('消息推送成功\n')
    else:
        print('消息推送失败\n')

def get_info():
    time = datetime.datetime.now()
    print(time)
    # 获取预警信息
    url = "http://www.12379.cn/data/alarm_list_all.html"
    res = requests.post(url, timeout=None)
    res.encoding = 'utf-8'
    ret = res.json()
    warning = []
    # print(ret['alertData'])
    # 判断是否有对应城市预警信息已经对应类型
    # 一般预警平台会存在多条信息，第一条是最新的
    for i in ret['alertData']:
        # 设置预警城市
        if ('定远县' in i['headline'] or '定远县' in i['description']) and '雨' in i['headline']:
            # 解除不通知
            if ('解除' in i['headline']):
                break
            warning.append(i['description'])
            break

    # 无预警退出
    # 有预警格式化并推送信息
    if not warning:
        print('无预警')
    else:
        msg = warning[0]
        print(msg)
        bark_push(msg)

if __name__ == "__main__":
    get_info()