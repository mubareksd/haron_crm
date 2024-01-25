from flask import render_template


def error_handler_template(code, title, message):
    def error_handler(error):
        return render_template(
            'error.html',
            error_code=code,
            error_title=title,
            error_message=message
        ), code
    return error_handler


page_not_found = error_handler_template(
    404,
    'Page not found',
    'The requested page was not found on the server.'
)
method_not_allowed = error_handler_template(
    405,
    'Method not allowed',
    'The method is not allowed for the requested URL.'
)
internal_server_error = error_handler_template(
    500,
    'Internal server error',
    'The server encountered an internal error and was unable to complete your request.'
)
