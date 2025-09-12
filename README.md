# Deserted Island Adventure

A survival-themed exploration game developed with Ren'Py.

## Game Introduction

Players take on the role of a survivor stranded on a deserted island, exploring different areas of the island (beach, jungle, cave), collecting materials to craft tools, and facing wild animals and weather changes while struggling to survive on the deserted island.

## Game Features

- **Regional Map Exploration System**: Click on different areas of the map to explore
- **Resource Collection and Tool Crafting**: Collect wood, stone, food and other resources to craft survival tools
- **Survival Mechanics**: Manage health, hunger, thirst and energy
- **Rich Environmental Interactions**: Each area has unique exploration content and challenges

## Game Controls

### Map Interface
- Click on area buttons on the map to enter corresponding areas
- Use function buttons in the top-right corner for tool crafting, status checking, etc.
- Top-left corner displays current survival status

### Area Exploration
- Each area has multiple exploration options
- Different actions will yield different resources and results
- Some actions may carry risks and require careful consideration

### Survival Management
- **Health**: Decreases when taking damage, game ends when it reaches zero
- **Hunger**: Decreases over time, need to find food
- **Thirst**: Decreases over time, need to find water sources
- **Energy**: Consumed during activities, can be restored by resting

## Installation and Running

1. Ensure Ren'Py SDK is installed
2. Place the project folder in the Ren'Py projects directory
3. Open the project in Ren'Py Launcher
4. Click "Launch Project" to start the game

## Resource Files

The game requires the following image resource files (see `资源文件需求文档.md` for details):

### Required Files
- `game/images/bg_beach.png` - Beach background
- `game/images/bg_jungle.png` - Jungle background  
- `game/images/bg_cave.png` - Cave background
- `game/images/bg_island_map.png` - Island map background
- `game/images/map_beach_idle.png` - Beach button (normal state)
- `game/images/map_beach_hover.png` - Beach button (hover state)
- `game/images/map_jungle_idle.png` - Jungle button (normal state)
- `game/images/map_jungle_hover.png` - Jungle button (hover state)
- `game/images/map_cave_idle.png` - Cave button (normal state)
- `game/images/map_cave_hover.png` - Cave button (hover state)

### Optional Files
- Various UI interface elements and icons

## Game File Structure

```
game/
├── script.rpy          # Main game script
├── map_screen.rpy      # Map interface definitions
├── options.rpy         # Game configuration
├── screens.rpy         # Interface style definitions
├── gui.rpy            # GUI configuration
└── images/            # Image resource directory
```

## Development Notes

- Game developed using Ren'Py engine
- Main script file: `script.rpy`
- Map interface definitions: `map_screen.rpy`
- Game configuration: `options.rpy`

## Future Expansions

- Add more areas and exploration content
- Implement more complex crafting systems
- Add weather system and time progression
- Increase survival challenges and events
- Add achievement system and save functionality

## Technical Information

- **Engine**: Ren'Py
- **Language**: Python + Ren'Py Script
- **Resolution**: 1920x1080
- **Audio**: None (visual-only game)

## License

This project is for learning and development reference only.
