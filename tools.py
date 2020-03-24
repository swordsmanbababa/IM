import redis
import random

r = redis.Redis(host="127.0.0.1", port=6379)
last_name = [
    '赵','钱','孙','李','周','吴','郑','王',
    '冯','陈','褚','卫','蒋','沈','韩','杨',
    '朱','秦','尤','许','何','吕','施','张',
    '孔','曹','严','华','金','魏','陶','姜','山本'
]
first_name = ['丽','娟','刚','伟','国','加','倩','惠','子','存']
i = 0
while i < 3:
    lindex = random.randint(0, 32)
    findex = random.randint(0, 9)
    sindex = random.randint(0, 1)
    name = last_name[lindex] + first_name[findex]
    sex = ['男','女'][sindex]
    age = random.randint(20, 60)
    key = "U_" + str(i + 1)
    r.hset(key, "userid", (i + 1))
    r.hset(key,"name",name)
    r.hset(key, "passwd", "1234")
    r.hset(key, "state", 1)
    r.lpush("User",key)
    i = i + 1

#
# def redis_hash_del(hashkey):
#     '''
#     delete redis hash key
#     '''
#     r = redis.Redis(host='localhost',port=6379)
#     if r.exists(hashkey):
#         hashkey_all = r.hkeys(hashkey)
#         for i in range(len(hashkey_all)):
#             r.hdel(hashkey, hashkey_all[i])
#
# i=0
# while i < 12:
#     key = "U_" + str(i + 1)
#     redis_hash_del(key)
#     i=i+1

# r = redis.Redis(host='localhost',port=6379)
# for to_userid in range(0,410):
#     key = key = "message_" + str(1) + "_TO_" + str(to_userid)
#     r.lpop(key)