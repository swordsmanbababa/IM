
import redis
import random

from user import User

r1 = redis.Redis(host="127.0.0.1", port=6379)
# key="user_friends"
# while i < 100:
#


# last_name = [
#     '赵','钱','孙','李','周','吴','郑','王',
#     '冯','陈','褚','卫','蒋','沈','韩','杨',
#     '朱','秦','尤','许','何','吕','施','张',
#     '孔','曹','严','华','金','魏','陶','姜','山本'
# ]
# first_name = ['丽','娟','刚','伟','国','加','倩','惠','子','存']
# i = 0
# while i < 100:
#     lindex = random.randint(0, 32)
#     findex = random.randint(0, 9)
#     sindex = random.randint(0, 1)
#     name = last_name[lindex] + first_name[findex]
#     age = random.randint(20, 60)
#     key = "U_" + str(i + 1)
#     r.hset(key,"name",name)
#     r.hset(key,"passwd","123")
#     r.hset(key,"state","1")
#     r.hset(key,"userid",str(i + 1))
#     i = i + 1
#
# User.userkeylist.append("sdsa")
# User.userkeylist.append("sada")
# #
# r1.publish("chat_2", "key123")
# r1.publish("chat_1", "content1")
# r1.publish("chat_3", "４")
#
# r1.sadd("U_Reqfndlst" + "as", 21)


# print(r1.sscan("U_"+'1'+"Reqfndlst",cursor=0))
#
# print (r1.sadd("151",1,2,3,4,5,6,7)       )    #输出的结果是7
# print (r1.sscan(151,cursor=2,match=1,count=1))

num = r1.scard("U_" + '2' + "Reqfndlst")
print( r1.srandmember("U_" + '2' + "Reqfndlst", num))