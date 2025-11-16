from flask import Flask, render_template, abort, url_for, json, jsonify, request, session, redirect, send_from_directory

def getWorksheets():
    user = session.get('user')
    username = user.get('name') if user and 'name' in user else None

    template_context = {
        'lang': session.get('lang', 'lv'),
        'title': 'Darbalapas',
        'username': username
    }
    return render_template('worksheets_content.html', **template_context)