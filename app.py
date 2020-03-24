import threading

from flask import Flask, request, render_template,session
import redis
from werkzeug.utils import redirect

from client import Client
from user import User
clientList={}

r1 = redis.Redis(host="localhost", port=6379)
app = Flask(__name__)
app.config['SECRET_KEY'] = "65sdfsdfsd"

@app.route('/', methods=['GET'])
def signin_form():

    return render_template('login.html')
   # return render_template('forbid.html')

@app.route('/forbid', methods=['GET'])
def forbid():
    # return render_template('login.html')
   return render_template('forbid.html')

def test():
    i=0
    while 1:
        i=i+1

@app.route('/signin', methods=['POST'])
def signin():

    userid = request.form['userid']
    password = request.form['password']
    key = "U_" + str(userid)
    client=Client(userid)
    t = threading.Thread(target=client.clientListener,args=(key,))
    clientList[userid]=client
    t.start()
    print(t)
    # with open('static/current_id.txt', 'w') as f:
    #     f.write(key)
    passwd = r1.hget(key,'passwd').decode("utf-8")
    if password and password == passwd:
        # session[str(userid)] = userid;
        User.getalluser()
        user_curret=User.keyToUser(key)
        User.getafriends(userid)
        return render_template('index.html', users=User.userlist,user_curret=user_curret,userid=userid,friends=User.friendList,len=len(User.friendList))
    return redirect("")


def room_message(title,id,to_userid=-1):
    key = "message_" + str( id)
    # title = r1.rpop(key)
    if title:
        # title = title.decode("utf-8")
        print("cur"+User.idTokey(id))
        r1.publish("chat_2",User.idTokey(id))
        r1.publish("chat_1", title)
        if(to_userid!=-1):
            r1.publish("chat_3", to_userid)

        print(title)
    return ''





@app.route('/room/message/send', methods=['GET','POST'])
def room_message_send():
    userid = request.args.get('userid')
    to_userid = request.args.get('to_userid')
    message = request.args.get("news")
    print("news:"+message)
    print("isdcddcd"+userid)
    # message = request

    # if message:
    #     # for revid in range(0, len(User.userlist)):
    #         key = "message_" + str(userid)
    #         # key = "message_" + str(userid)+"_TO_"+str(revid)
    #         r1.lpush(key, message)
    print("to_userid")
    print(to_userid)
    if to_userid==None:
        room_message(message,userid)
    else:
        room_message(message,userid,to_userid)
    return "ok"


@app.route('/user/message/send', methods=['GET','POST'])
def user_message_send():
    userid = session['userid']
    to_userid = request.form['to_userid']
    message = request.form['message']
    if message:
        key = "message_" + str( userid)
        # key = "message_" + str(userid) + "_TO_" + str(to_userid)
        r1.lpush(key, message)

    return "ok"

@app.route('/addfriends',methods=['GET','POST'])
def addfriends():
    userid = request.args.get('userid')
    to_userid = request.args.get('to_userid')
    print("to_userid"+to_userid)
    r1.sadd("U_"+str(to_userid)+"Reqfndlst",userid)
    return 'ok'
@app.route('/addfriendsres',methods=['GET','POST'])
def addfriendsres():
    userid = request.args.get('userid')
    to_userid = request.args.get('to_userid')
    r1.sadd("U_" + str(to_userid) + "fndlst", userid)
    r1.sadd("U_" + str(userid) + "fndlst", to_userid)

lock = threading.Lock()
@app.route('/room/message/receive', methods=['GET','POST'])
def receive():
    lock.acquire()
    userid = request.args.get('userid')
    # print("+++++++++++++++id"+userid)
    client=clientList.get(userid)
    msg=client.message
    client.message=''
    lock.release()
    return msg

@app.route('/iffriensreq', methods=['GET','POST'])
def iffriensreq():
    userid = request.args.get('userid')
    print("userid+"+userid)
    while 1:
        num=r1.scard("U_"+userid+"Reqfndlst")
        print("num="+str(num))
        if num and num!=0:
            res=r1.spop("U_"+userid+"Reqfndlst")
            print("adasdaf"+res.decode())
            return res.decode()
        else:
            break
    return ''


@app.route('/checkfriends', methods=['GET','POST'])
def checkfriends():
    userid = request.args.get('userid')
    to_userid = request.args.get('to_userid')
    print(userid+"===")
    print(to_userid+"===")

    User.getafriends(userid)
    flag = 0
    for item in User.friendList:
        print("item"+item)
        if item==to_userid or to_userid=='':
            flag=1
    if flag==1:
        return 'ok'
    else:
        return ''






if __name__ == '__main__':
    app.run(threaded=True)


