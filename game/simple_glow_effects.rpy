
# 方法1：颜色发光效果
transform color_glow:
    alpha 1.0
    matrixcolor TintMatrix("#ffffff")
    
    on hover:
        # 颜色变化实现发光效果 每0.2秒变化一次
        parallel:
            linear 0.2 matrixcolor TintMatrix("#ffff88")  #  淡黄色
            linear 0.2 matrixcolor TintMatrix("#ffffff")
            linear 0.2 matrixcolor TintMatrix("#88ffff")  # 淡蓝色
            linear 0.2 matrixcolor TintMatrix("#ffffff")
            repeat
        parallel:
            linear 0.2 alpha 1.0
            linear 0.2 alpha 0.8
            repeat
    on idle:
        linear 0.3 matrixcolor TintMatrix("#ffffff")
        linear 0.3 alpha 1.0


# 方法2：渐变发光 放大
transform gradient_glow:
    alpha 1.0 # 设置初始透明度为1
    matrixcolor TintMatrix("#ffffff") # 设置初始颜色为白色
    
    # on hover:
    #     parallel:
    #     # 白色发光效果
    #         linear 0.8 matrixcolor BrightnessMatrix(0.3)
    #         linear 0.8 matrixcolor BrightnessMatrix(0)
    #         repeat
    #     parallel:
    #         # 亮度变化
    #         linear 0.2 alpha 1.0
    #         linear 0.2 alpha 0.7
    #         repeat
    # on idle:
    #     parallel:
    #         linear 0.3 matrixcolor TintMatrix("#ffffff")
    #     parallel:
    #         linear 0.3 alpha 1.0
    on hover:
        matrixcolor BrightnessMatrix(0.2)  # 保持柔和的白色亮度
        easein 0.3 zoom 1.02  # 轻微放大
    
    on idle:
        matrixcolor BrightnessMatrix(0)  # 恢复原状
        easein 0.3 zoom 1.0

# 方法3：简单脉冲发光
transform simple_pulse_glow:
    alpha 1.0
    matrixcolor TintMatrix("#ffffff")
    
    on hover:
        parallel:
            # 简单颜色脉冲
            linear 0.3 matrixcolor TintMatrix("#ffcc88")
            linear 0.3 matrixcolor TintMatrix("#ffffff")
            repeat
        parallel:
            # 透明度脉冲
            linear 0.3 alpha 1.0
            linear 0.3 alpha 0.8
            repeat
    on idle:
        parallel:
            linear 0.3 matrixcolor TintMatrix("#ffffff")
        parallel:
            linear 0.3 alpha 1.0

# 方法5：暖色调发光
transform warm_glow:
    alpha 1.0
    matrixcolor TintMatrix("#ffffff")
    
    on hover:
        parallel:
            # 暖色调变化
            linear 0.3 matrixcolor TintMatrix("#ffaa66")
            linear 0.3 matrixcolor TintMatrix("#ffcc88")
            linear 0.3 matrixcolor TintMatrix("#ffaa66")
            linear 0.3 matrixcolor TintMatrix("#ffffff")
            repeat
        parallel:
            # 亮度变化
            linear 0.2 alpha 1.0
            linear 0.2 alpha 0.9
            repeat
    on idle:
        parallel:
            linear 0.3 matrixcolor TintMatrix("#ffffff")
        parallel:
            linear 0.3 alpha 1.0

# 方法6：冷色调发光
transform cool_glow:
    alpha 1.0
    matrixcolor TintMatrix("#ffffff")
    
    on hover:
        parallel:
            # 冷色调变化
            linear 0.3 matrixcolor TintMatrix("#66aaff")
            linear 0.3 matrixcolor TintMatrix("#88ccff")
            linear 0.3 matrixcolor TintMatrix("#66aaff")
            linear 0.3 matrixcolor TintMatrix("#ffffff")
            repeat
        parallel:
            # 亮度变化
            linear 0.2 alpha 1.0
            linear 0.2 alpha 0.9
            repeat
    on idle:
        parallel:
            linear 0.3 matrixcolor TintMatrix("#ffffff")
        parallel:
            linear 0.3 alpha 1.0
