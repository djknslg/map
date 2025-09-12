### 地图与 ImageButton 悬浮/点击事件说明

本项目的地图界面与可点击区域由 `screen map_screen` 定义，使用多组 `imagebutton` 来实现鼠标悬浮（hover）与点击（click）效果切换。

---

## 1. 地图入口与基础结构

- **入口**：`label start` → `call show_map` → `call screen map_screen`
- **文件位置**：
  - 地图屏幕：`game/map_screen.rpy`
  - 流程/事件：`game/script.rpy`
  - GUI 尺寸：`game/gui.rpy`（本项目初始化为 1920x1080）
  - 相关图片：`game/images/`

地图屏幕核心结构摘录：

```rpy
screen map_screen():
    # 背景
    add "bg map"

    # 标题（可选）
    text "Island Map" xalign 1 ypos 50 size 40 color "#ffffff" outlines [(2, "#000000")]

    # 海滩按钮
    imagebutton:
        idle "map_beach_idle"
        hover "map_beach_hover"
        action Jump("beach_event")
        xpos 200 ypos 800
        focus_mask True

    # 森林按钮
    imagebutton:
        idle "map_forest_idle"
        hover "map_forest_hover"
        action Jump("forest_event")
        xpos 1800 ypos 50
        focus_mask True

    # 山地按钮
    imagebutton:
        idle "map_mountain_idle"
        hover "map_mountain_hover"
        action Jump("mountain_event")
        xpos 1000 ypos 400
        focus_mask True
```

- **背景**：`add "bg map"` 使用 `game/images/bg map.png`。
- **按钮切换**：`idle`/`hover` 分别对应非悬浮与悬浮时显示的图片。
- **点击事件**：`action Jump("label_name")` 点击后跳转到对应剧情 `label`。
- **命中区域**：`focus_mask True` 让 PNG 透明区域不响应鼠标（命中依据图片不透明像素）。
- **坐标**：`xpos`/`ypos` 基于屏幕左上角，单位为像素（分辨率 1920x1080）。

---

## 2. 事件与返回地图

在 `game/script.rpy` 中，每个地点都有对应的 `label` 与内容。示例（海滩）：

```rpy
label beach_event:
    scene bg beach
    with fade

    narrator "You have arrived at the beach."

    menu:
        "Explore the beach":
            narrator "You find some useful materials on the beach."
        "Look for food":
            narrator "You discover some edible seaweed and shells."
        "Return to map":
            call show_map

    call show_map
    return
```

- 建议每个事件最后都 `call show_map` 回到地图，或在菜单中提供“返回地图”。

---

## 3. 新增一个地点按钮（步骤与示例）

1) 准备四张图片（最少两张）：
   - 背景已存在：`game/images/bg map.png`
   - 新地点按钮：`game/images/map_newplace_idle.png`、`game/images/map_newplace_hover.png`

2) 在 `game/map_screen.rpy` 的 `screen map_screen()` 中添加：

```rpy
    imagebutton:
        idle "map_newplace_idle"
        hover "map_newplace_hover"
        action Jump("newplace_event")
        xpos 1400 ypos 700
        focus_mask True
```

3) 在 `game/script.rpy` 中新增事件 `label`：

```rpy
label newplace_event:
    scene bg black
    with fade
    narrator "You arrive at the new place."
    menu:
        "Return to map":
            call show_map
    return
```

---

## 4. 悬浮与点击的常用增强

在 `imagebutton` 内可添加以下属性/回调：

- 声音反馈：
  - `hover_sound "audio/hover.ogg"`
  - `activate_sound "audio/click.ogg"`
- 工具提示（需配合 `tooltip` 使用）：
  - `tooltip "海滩"`（并在外层布局中显示 `GetTooltip()`）
- 悬浮/离开时执行：
  - `hovered [SetVariable("current_hint", "进入海滩"), Show("notify", message="海滩")]`
  - `unhovered SetVariable("current_hint", None)`
- 组合动作：
  - `action [Play("sound", "audio/click.ogg"), Jump("beach_event")]`
- 条件可用/选中态：
  - `sensitive some_flag`（False 时不可点击）
  - `selected is_at_beach`（用于高亮当前选择）

示例：

```rpy
    imagebutton:
        idle "map_beach_idle"
        hover "map_beach_hover"
        tooltip "海滩"
        hovered SetVariable("current_hint", "进入海滩")
        unhovered SetVariable("current_hint", None)
        action [Play("sound", "audio/click.ogg"), Jump("beach_event")]
        xpos 200 ypos 800
        focus_mask True
```

---

## 5. 资源与命名建议

- 背景：`game/images/bg map.png`
- 地点按钮：`map_<name>_idle.png` / `map_<name>_hover.png`
- 透明区域：若使用 `focus_mask True`，请确保 PNG 的透明区域足够干净，避免误触。

---

## 6. 常见问题排查

- **悬浮无变化**：检查 `hover` 图是否存在、命名是否与声明一致；确认没有被其他层级覆盖（必要时给按钮设置更高的 `zorder`）。
- **无法点击**：
  - `action` 是否正确（如 `Jump("label")` 对应的 `label` 是否存在）。
  - 若用了 `sensitive`，确认条件为 True。
  - 若用了 `focus_mask True`，确认按钮图片尺寸与放置区域一致且非透明像素位于可点击位置。
- **点击区域不准确**：PNG 的非透明像素即为命中区域；如需规则矩形区域，可去掉 `focus_mask True` 或改用 `hotspot`/`imagemap`。
- **位置不对**：根据 `game/gui.rpy` 初始化分辨率（本项目为 1920x1080）调整 `xpos`/`ypos`。

---

## 7. 进阶：使用 Imagemap/Hotspot（可选）

如果想用一张整体地图并在其上定义多个不规则可点击区域，可考虑：

```rpy
screen map_screen():
    imagemap:
        ground "bg map"
        hover  "bg map"  # 或者提供 hover 版本

        hotspot (x, y, w, h) action Jump("beach_event")
        hotspot (x2, y2, w2, h2) action Jump("forest_event")
```

当需要不规则区域时，可为 `hotspot` 指定 `focus_mask` 图片来精确命中。

---

## 8. 参考位置

- 屏幕定义：`game/map_screen.rpy`
- 事件标签：`game/script.rpy`
- 分辨率与 GUI：`game/gui.rpy`
- 图片资源：`game/images/`

如需我帮你新增具体地点或接入音效/提示，请告诉我地点名称、坐标与资源文件名。


