import argparse

# Parser : So that we can remove the inputs and other things
parser = argparse.ArgumentParser(
    description="Voxel Animated Donut ASCII Art"
)
anim = parser.add_argument_group("Animation Options")
anim.add_argument("-G", "--grid", type=int, default=50,
                  help="3D Grid for Donut to reside in.")

anim.add_argument("-L", "--light_ratio", type=float, default=0.5, 
                  help="Light to Depth shading ratio.")

anim.add_argument("-AM", "--ascii_mode", type=int, default=1,
                  help="""Different ascii styles:
                  0: Simple Text
                  1: Block Based {Default}
                  2: Dot Based
                  3: Text based {Extra Contrast}""")

anim.add_argument("-LD", "--light_direction", nargs=3, type=float, 
                  help="Sun Light direction hitting Donut")

anim.add_argument("-A","--axis", nargs=3, type=float, 
                  help="Rotation Axis of Donut")

anim.add_argument("-RS", "--rotation_speed", type=int, default=5,
                  help="Degrees of rotation per frame")

anim.add_argument("-FR","--frame_rate", type=int, default=25,
                  help="No. of frames per second")

anim.add_argument("-CT","--center_tabs", type=int, default=0,
                  help="No. of tabs to be added to center the Donut on the screen")
