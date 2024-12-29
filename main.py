import os

from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *

MAX_NAME_CHAR =15
MAX_MESSAGE_CHAR = 50
app,rt = fast_app()


def render_message(entry):
    return (
        Article(
            Header(f"Name: {entry['name']}"),
            P(entry["message"]),
            Footer(Small(Em(f"Posted: {entry['timestamp']}"))),
        ),
    )


def render_message_list():
    messages=[
        {"name": "Peter", "message": "Hi There", "timestamp": "now"},
        {"name": "John", "message": "Cool", "timestamp": "yesterday"},
    ]

    return Div(
        *[render_message(entry) for entry in messages],
    )


def render_content():
    form = Form(
        Fieldset(
            Input(
                type="text",
                name="name",
                placeholder="Name",
                required=True,
                maxlength=MAX_NAME_CHAR,
            ),
            Input(
                type="text",
                name="message",
                placeholder="Message",
                required=True,
                maxlength=MAX_MESSAGE_CHAR,
            ),
            Button("Submit", type="submit"),
            role="group",
        ),
        method="post",
        hx_post="/submit-message",  # Send a POST request to the /submit-message endpoint
        hx_target="#message-list",  # Only swap the message list
        hx_swap="outerHTML",  # Replace the entire content of the target element with the response
        hx_on__after_request="this.reset()",  # Reset the form after submission
    )

    return Div(
        P(Em("Write something nice!")),
        form,
        P("Our form will be here..."),
        Div(
            "Made with 💙 by Yana ",
            A("Yana ", href = "https://www.linkedin.com/in/nur-liyana-aris/", target="_blank"),
        ),
        Hr(),
        P("The messages will be displayed here....."),
        render_message_list(),
    )


# @rt('/change')
# def get(): 
#     # return P('Nice to be here!')
#     return Titled("Changed", P("Hello! Nice to be here!"), A("Go back to home", href="/"))

@rt('/')
def get(): 
    # return Titled(Div(P('Hello World!'), hx_get="/change")) Tiled used Pico here for the styling
    # return Titled(Div(P('Hello World!')), P(A("Link", href="/change"))) this is the link
    return Titled("My Guestbook 📖", render_content())

serve()