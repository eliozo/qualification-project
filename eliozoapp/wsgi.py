#'''WSGI entry'''
import eliozo
handler = eliozo.create_app()


if __name__ == '__main__':
    # Entry point when run via Python interpreter.
    print("== Running in debug mode ==")
    handler.run(host='0.0.0.0', port=5000, debug=True)
    #ddgatve.create_app().run(host='0.0.0.0', port=5000, debug=True)
else:
    application = handler