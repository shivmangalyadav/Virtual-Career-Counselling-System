from flask import Flask, render_template, request, jsonify, Blueprint
# from flask_jwt import JWT, jwt_required, current_identity
import api.course_channel.database_connect as db

# from userauth import authenticate, identity

# app = Flask(__name__)

channelmod = Blueprint('channels', __name__)

# app.config['SECRET_KEY'] = 'super-secret'
# jwt = JWT(app, authenticate, identity)



@channelmod.route('/course', methods=['GET'])
# @jwt_required()
def course():
    courses = {}
    # courses.clear()
    course_name = db.course_data()
    for i in course_name:
        courses[i[0]] = i[1]
    
    json1 = jsonify(courses)

    return json1


# @app.route('/course', methods=['GET'])
# # @jwt_required()
# def course():
#     course_name = db.course_data()
#     json1 = jsonify(course_name)

#     return json1

@channelmod.route('/stream')
def stream():
    streams = {}
    data = request.get_json()
    stream_name = db.stream_data(data['cid'])
    print(stream_name)
    for j in stream_name:
        streams[j[0]] = j[1]
        print(streams)

    return jsonify(streams)
    

@channelmod.route('/program')
def program():
    programs = {}
    data = request.get_json()
    program_name = db.program_data(data['cid'], data['sid'])
    # print(program_name)
    for k in program_name:
        # print(k)
        programs[k[0]] = { k[1]:k[2], k[3]:k[4] }
    
    
    return jsonify(programs)

@channelmod.route('/channels')
def channel():
    channels = {}
    data = request.get_json()
    channel_name = db.channel_data(data['pid'])
    # print(channel_name)
    for c in channel_name:
        channels[c[0]] = { c[1]:c[2], c[3]:c[4] }
    # print(channels)

    return jsonify(channels)

@channelmod.route('/channel')
def single_channel():
    channel = {}
    data = request.get_json()
    channel_name = db.single_channel_data(data['pid'], data['chid'])
    # print(channel_name)
    for ch in channel_name:
        channel[ch[0]] = { ch[1]:ch[2], ch[3]:ch[4] }
    # print(channels)

    return jsonify(channel)


# if __name__ == "__main__":
#     app.run(debug = True)