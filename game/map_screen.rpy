# Map Screen Definition

screen map_screen():
    # Map background
    add "bg map"
    
    # Map title
    text "Island Map" xalign 1 ypos 50 size 40 color "#ffffff" outlines [(2, "#000000")]
    
    # Beach area button with warm glow
    imagebutton:
        idle "map_beach_idle"
        hover "map_beach_hover"
        mouse "mousehover"
        action Jump("beach_event")
        xpos 200 ypos 800
        focus_mask True
        at warm_glow
    
    # Forest area button with cool glow
    imagebutton:
        idle "map_forest_idle"
        mouse "mousehover"
        action Jump("forest_event")
        xpos 1800 ypos 50
        focus_mask True
        at cool_glow
    
    # Mountain area button with gradient glow
    imagebutton:
        idle "map_mountain_idle"
        mouse "mousehover"
        action Jump("mountain_event")
        xpos 1000 ypos 400
        focus_mask True
        at gradient_glow