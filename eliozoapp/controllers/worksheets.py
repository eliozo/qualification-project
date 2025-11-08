from flask import Flask, render_template, abort, url_for, json, jsonify, request, session, redirect, send_from_directory

def getWorksheets():

    template_context = {

        'lang': session.get('lang', 'lv'),
        'title': 'Darbalapas'
    }
    return render_template('worksheets_content.html', **template_context)