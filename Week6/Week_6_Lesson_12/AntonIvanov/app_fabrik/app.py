from . import run_app
from flask import session, current_app

app = run_app()

@app.before_first_request
def set_mode():
    test_var = current_app.config.get("TEST_VARIABLE")
    session['mode'] = test_var


if __name__ == "__main __":
    app.run()
