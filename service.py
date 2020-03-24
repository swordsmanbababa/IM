import redis
import time

from user import User

r = redis.Redis(host="localhost", port=6379)
channel_key = "chat_2"
ps_key=r.pubsub()
ps_key.subscribe([channel_key])

channel = "chat_1"
ps = r.pubsub()
ps.subscribe([channel])

channel = "chat_3"
ps_touser = r.pubsub()
ps_touser.subscribe([channel])

for key in ps_key.listen():
    key_cuurent=''
    if type(key['data']) != int:
        key_cuurent=key['data'].decode("utf-8")
    print("key="+key_cuurent)
    for item in ps.listen():  # 监听状态：有消息发布了就拿过来
        print(item)
        if type(item['data']) != int:
            message = item['data'].decode("utf-8")
            for to_user in ps_touser.listen():
                print("to_user")
                print(to_user)
                if type(to_user['data']) != int:
                    to_userid_msg = to_user['data'].decode("utf-8")
                    if to_userid_msg!='':
                        print("in")
                        r.publish("U_" + to_userid_msg, message)
                        break
                    else:
                        for user_key in User.userkeylist:
                            print("user_key"+user_key.decode("utf-8"))
                            if (user_key.decode("utf-8") != key_cuurent):
                                r.publish(user_key, message)
                                print(message)
                    break


        break


