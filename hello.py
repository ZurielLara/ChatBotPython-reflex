"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from hello import style
from hello.state import State

def action_bar()-> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Escribe...",
            on_change=State.set_question,
            style=style.input_style,
            ),
        rx.button(
            "Enviar",
            on_click=State.answer, 
            style=style.button_style
            ),
        )

def qa(mensaje1: str, mensaje2: str)->rx.Component:
    return rx.box(
        rx.box(
            rx.text(mensaje1, style=style.mensaje1_style),
            text_align="center",
        ),
        rx.box(
            rx.text(mensaje2, style=style.mensaje2_style),
            text_align="center",
        ),
        margin_y="1em",
    )

def chat()->rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def index() -> rx.Component:
    return rx.container(
        rx.avatar_group(
            rx.avatar(rx.avatar_badge(
                box_size="1.25em",
                bg="red.500"
            ),
                name="Bot", size ="md"),
            rx.avatar(rx.avatar_badge(
                box_size="1.25em",
                bg="green.500"
            ),
                name="I'm"),
            ),
        chat(),
        action_bar(),
        )
    


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
