# Map Screen Definition

screen map_screen():
    # Map background
    add "bg map"
    
    # Map title
    text "Island Map" xalign 1 ypos 50 size 40 color "#ffffff" outlines [(2, "#000000")]
    
    # Beach area button
    imagebutton:
        idle "map_beach_idle"
        hover "map_beach_hover"
        action Jump("beach_event")
        xpos 200 ypos 800
        focus_mask True
    
    # Forest area button
    imagebutton:
        idle "map_forest_idle"
        hover "map_forest_hover"
        action Jump("forest_event")
        xpos 1800 ypos 50
        focus_mask True
    
    # Mountain area button
    imagebutton:
        idle "map_mountain_idle"
        hover "map_mountain_hover"
        action Jump("mountain_event")
        xpos 1000 ypos 400
        focus_mask True