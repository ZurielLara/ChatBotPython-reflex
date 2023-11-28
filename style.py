#Estilos

#Estilos Comunes apra el chat
shadow="rgba(0,0,0,0.15) 0px 2px 8px"
chat_margin ="20%"
message_style= dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

mensaje1_style=message_style|dict(
    bg="#F5EFFE",margin_left=chat_margin
)
mensaje2_style=message_style|dict(
    bg="#DEEADF",margin_left=chat_margin
)

input_style=dict(
    border_width="1px",padding="1em",box_shadow=shadow
)
button_style=dict(
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image="linear-gradiente(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
    box_sizing="border-box",
    color="black",
    opacity="0.6",
    _hover={
        "opacity": 1,
    },
)