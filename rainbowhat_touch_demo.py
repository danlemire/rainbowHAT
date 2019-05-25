import rainbowhat as rh
@rh.touch.A.press()
def touch_a(channel):
    print('Button A pressed')
    rh.lights.rgb(1, 0, 0)

@rh.touch.A.release()
def release_a(channel):
    print('Button A released')
    rh.lights.rgb(0, 0, 0)

@rh.touch.B.press()
def touch_b(channel):
    print('Button B pressed')
    rh.lights.rgb(0, 1, 0)

@rh.touch.B.release()
def release_b(channel):
    print('Button B released')
    rh.lights.rgb(0, 0, 0)

@rh.touch.C.press()
def touch_c(channel):
    print('Button C pressed')
    rh.lights.rgb(0, 0, 1)

@rh.touch.C.release()
def release_c(channel):
    print('Button C released')
    rh.lights.rgb(0, 0, 0)
