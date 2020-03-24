

import redis




class Client:

    def __init__(self,  id):
        self.message = ""
        self.userid = id

    def clientListener(self,key):
        r = redis.Redis(host="localhost", port=6379)
        # with open('static/current_id.txt', 'r') as f:
        #     key = f.read()
        channel = key
        print("key="+channel)
        ps = r.pubsub()
        ps.subscribe([channel])
        # while 1:
        for item in ps.listen():  # 监听状态：有消息发布了就拿过来
            if type(item['data']) != int:
                message = item['data'].decode("utf-8")
                self.message=message
                print('message='+message)


