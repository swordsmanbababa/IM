from flask import Flask, request, render_template,session
import redis
r1 = redis.Redis(host="localhost", port=6379)

class User:
    userkeylist=[]
    userlist=[]
    friendList=[]
    def  __init__(self,userid,name,passwd,state=0):
        self.userid=userid
        self.name=name
        self.passwd=passwd
        self.state=state

    @staticmethod
    def idTokey(userid):
        return "U_" + str(userid)

    @staticmethod
    def keyToUser(key):
        user = r1.hvals(key)
        user = User(user[0].decode(), user[1].decode(), user[2].decode(), user[3].decode())
        return user

    @staticmethod
    def getalluserkeys():
        User.userkeylist=[]
        keylen=r1.llen("User")
        i=0
        while i<keylen:
            User.userkeylist.append(r1.lindex("User",i))
            i=i+1
    @staticmethod
    def getafriends(userid):
        User.friendList=[]
        num=r1.scard("U_"+userid+"fndlst")
        User.friendList=r1.srandmember("U_" + userid+ "fndlst",num)
        for i,item in enumerate(User.friendList) :
            User.friendList[i]=str(item.decode('utf-8'))




    @staticmethod
    def getalluser():
        User.userlist=[]
        if(User.userkeylist==[]):
            User.getalluserkeys()

        keylen=len(User.userkeylist)
        i=0
        while i<keylen:
            user=r1.hvals(User.userkeylist[i])
            user = User(user[0].decode(),user[1].decode(),user[2].decode(),user[3].decode())
            User.userlist.append(user)
            i=i+1

User.getalluser()


