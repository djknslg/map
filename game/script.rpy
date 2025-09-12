# Simple Map Click Game

# Define characters
define narrator = Character(None)

# Game start
label start:
    # Show game title
    scene bg black
    with fade
    
    centered "Map Adventure Game"
    
    scene bg black
    with fade
    
    # Go to map screen
    call show_map
    
    return

# Show map screen
label show_map:
    call screen map_screen
    return

# Beach area event
label beach_event:
    scene bg beach
    with fade
    
    narrator "You have arrived at the beach."
    narrator "The waves are gently crashing against the shore."
    narrator "You can see some driftwood scattered on the sand."
    
    menu:
        "Explore the beach":
            narrator "You find some useful materials on the beach."
        "Look for food":
            narrator "You discover some edible seaweed and shells."
        "Return to map":
            call show_map
    
    call show_map
    return

# Forest area event
label forest_event:
    scene bg forest
    with fade
    
    narrator "You enter the dense forest."
    narrator "Tall trees surround you, and sunlight filters through the leaves."
    narrator "You can hear the sounds of wildlife in the distance."
    
    menu:
        "Explore deeper":
            narrator "You venture deeper into the forest and find some berries."
        "Collect wood":
            narrator "You gather some fallen branches for firewood."
        "Return to map":
            call show_map
    
    call show_map
    return

# Mountain area event
label mountain_event:
    scene bg mountain
    with fade
    
    narrator "You climb up to the mountain area."
    narrator "The view from here is breathtaking."
    narrator "You can see the entire island from this vantage point."
    
    menu:
        "Look for minerals":
            narrator "You find some interesting rocks and crystals."
        "Rest and enjoy the view":
            narrator "You take a moment to appreciate the beautiful scenery."
        "Return to map":
            call show_map
    
    call show_map
    return