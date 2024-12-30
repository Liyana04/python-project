import os
from datetime import datetime

# pytz is python library for timezone
import pytz
from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *

# Load environment variables
load_dotenv() 

MAX_NAME_CHAR =15
MAX_MESSAGE_CHAR = 50
TIMESTAMP_FMT = "%Y-%m-%d %I:%M:%S %p Asia/Singapore"

# initialize supabase client
supabase = create_client(os.getenv("SUPABASE_URL"),os.getenv("SUPABASE_KEY"))


# this is a header
app, rt = fast_app(
    hdrs=(Link(rel="icon", type="assets/x-icon", href="/assets/favicon.png"),),
)


# app,rt = fast_app() this is also the header


def get_asia_time():
    asia_tz = pytz.timezone("Asia/Singapore")
    return datetime.now(asia_tz)


def add_message(name, message):
    timestamp = get_asia_time().strftime(TIMESTAMP_FMT)
    supabase.table("MyGuestBook").insert(
        {"name": name, "message": message, "timestamp":timestamp}
    ).execute()
    # sheet.append_row([name, message, timestamp])


def get_messages():
    # sort by 'id' in descending order to get the latest entry
    response = (
        supabase.table("MyGuestBook").select("*").order("id", desc=True).execute()
        )
    return response.data


def render_message(entry):
    return (
        Article(
            Header(f"Name: {entry['name']}"),
            P(entry["message"]),
            Footer(Small(Em(f"Posted: {entry['timestamp']}"))),
        ),
    )


def render_message_list():
    # from supabase
    messages = get_messages()

    # dummy data
    # messages=[
    #     {"name": "Peter", "message": "Hi There", "timestamp": "now"},
    #     {"name": "John", "message": "Cool", "timestamp": "yesterday"},
    # ]

    return Div(
        *[render_message(entry) for entry in messages],
        id="message-list",
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
        # P("Our form will be here..."),
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


# new route for submit message
@rt("/submit-message", methods=["POST"])
def post(name: str, message: str):
    add_message(name, message)
    return render_message_list()


serve()