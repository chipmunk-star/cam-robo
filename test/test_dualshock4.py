import sdl2

#
sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)

count = sdl2.joystick.SDL_NumJoysticks()
print('num juysticks: ', count)

#
for i in range(count):
    joystic = sdl2.SDL_JoystickOpen(i)
    name = sdl2.SDL_JoystickName(joystic)
    print('{}: {}'.format(i, name))
    sdl2.SDL_JoystickClose(joystic)

#
joystick = sdl2.SDL_JoystickOpen(0)
name = sdl2.SDL_JoystickName(joystick)
print(name)

num_axes = sdl2.SDL_JoystickNumAxes(joystick)
print('num axes; ', num_axes)

num_buttons = sdl2.SDL_JoystickNumButtons(joystick)
print('num buttons: ', num_buttons)

num_hats = sdl2.SDL_JoystickNumHats(joystick)
print('num hats: ', num_hats)

num_balls = sdl2.SDL_JoystickNumBalls(joystick)
print('num balls: ', num_balls)

#
import ctypes
import time

event = sdl2.SDL_Event()
while True:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_JOYAXISMOTION:
            print('axis[{}] => {}'.format(event.jaxis.axis, event.jaxis.value))
        elif event.type == sdl2.SDL_JOYBUTTONDOWN:
            print('button[{}] => down'.format(event.jbutton.button))
        elif event.type == sdl2.SDL_JOYBUTTONUP:
            print('button[{}] => up'.format(event.jbutton.button))
    time.sleep(0.1)
