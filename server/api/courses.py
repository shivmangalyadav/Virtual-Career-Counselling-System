from flask import Flask, render_template, request, jsonify, Blueprint
from database import Course

course_dt = Course()
channelmod = Blueprint('channels', __name__)

@channelmod.route('/course', methods=['GET'])
def course():
    courses = {}
    course_name = course_dt.course_data()
    for i in course_name:
        courses[i[0]] = i[1]
    
    json1 = jsonify(courses)

    return json1

@channelmod.route('/stream')
def stream():
    streams = {}
    data = request.get_json()
    stream_name = course_dt.stream_data(data['cid'])
    print(stream_name)
    for j in stream_name:
        streams[j[0]] = j[1]
        print(streams)

    return jsonify(streams)
    
@channelmod.route('/program')
def program():
    programs = {}
    data = request.get_json()
    program_name = course_dt.program_data(data['cid'], data['sid'])
    for k in program_name:
        programs[k[0]] = { k[1]:k[2], k[3]:k[4] }
    
    return jsonify(programs)

@channelmod.route('/channels')
def channel():
    channels = {}
    data = request.get_json()
    channel_name = course_dt.channel_data(data['pid'])
    for c in channel_name:
        channels[c[0]] = { c[1]:c[2], c[3]:c[4] }

    return jsonify(channels)

@channelmod.route('/channel')
def single_channel():
    channel = {}
    data = request.get_json()
    channel_name = course_dt.single_channel_data(data['pid'], data['chid'])
    for ch in channel_name:
        channel[ch[0]] = { ch[1]:ch[2], ch[3]:ch[4] }

    return jsonify(channel)
