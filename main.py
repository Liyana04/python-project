from fasthtml.common import *

app,rt = fast_app()

def render_content():
    form = Form(
        Fieldset(
            Input(
                type="text",
                name="name",
                placeholder="Name",
                required=True,
                maxlength=15,
            ),
            Input(
                type="text",
                name="message",
                placeholder="Message",
                required=True,
                maxlength=50,
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
        P("Our form will be here..."),
        Div(
            "Made with 💙 by Yana",
            A("Yana", href = "https://www.linkedin.com/in/nur-liyana-aris/", target="_blank"),
        ),
        Hr(),
        P("The messages will be displayed here....."),
    )


@rt('/change')
def get(): 
    # return P('Nice to be here!')
    return Titled("Changed", P("Nice to be here!"), A("Go back to home", href="/"))

@rt('/')
def get(): 
    # return Titled(Div(P('Hello World!'), hx_get="/change")) Tiled used Pico here for the styling
    # return Titled(Div(P('Hello World!')), P(A("Link", href="/change"))) this is the link
    return Titled("My Guestbook 📖", render_content())

serve()