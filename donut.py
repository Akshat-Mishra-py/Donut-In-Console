import numpy as np
import time



# Constants
GRID = 40
HALF_GRID = GRID//2
CENTER = np.array([HALF_GRID, HALF_GRID,HALF_GRID])
LIGHTING = 1 # Light Ratio for changing Shading

# Changing Draw mode
ASCII_MODE = 1
if ASCII_MODE == 0:
    string =" `.-\':_,^=;><+!rc*/z?sLTv)J7(|FifI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    FILLER = [*string]

elif ASCII_MODE == 1:
    FILLER = (' ', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█')

elif ASCII_MODE == 2:
    FILLER = (' ','⡀', '⡄', '⡆', '⡇', '⣇', '⣧', '⣷', '⣿')

else:
    FILLER = (' ','`','.', '-','\'', ':','_','^', '=', '+', '*', '#', '%', '@')


LIGHT = [-1,-1,2] #Light Direction Vector

# Rotation Axis & Normalisation
AXIS =  [1,0,1]
ROTATION_AXIS = np.array(AXIS, dtype=np.float64)
ROTATION_AXIS = ROTATION_AXIS/np.linalg.norm(ROTATION_AXIS)

ROTATION_SPEED = 5 #Per Frame

TORUS = None

# Donuts Radii
R = major_Rad = GRID//3.5
r = minor_rad = R//2


def Rotate(X, Y, Z, ux, uy, uz, theta) -> np.array:
    '''Returns New (X,Y,Z) after Rotation of theta on axis of (ux,uy,uz)'''

    sin = np.sin(theta)
    cos = np.cos(theta)
    one_cos= 1-np.cos(theta)

    rotation_matrix = np.array([[cos + ((ux**2)*one_cos), ux*uy*one_cos-uz*sin, ux*uz*one_cos+uy*sin],
                                [uy*ux*one_cos+uz*sin, cos + ((uy**2)*one_cos), uy*uz*one_cos-ux*sin],
                                [uz*ux*one_cos-uy*sin, uz*uy*one_cos+ux*sin, cos + ((uz**2)*one_cos)]])

    # Calculating new vector and approximating and clipping to (0,Grid)
    vector = np.stack([X,Y,Z], axis=-1)
    vector = np.einsum('ij, kj -> ki',  rotation_matrix , (vector - CENTER)) 
    vector +=  CENTER
    vector = vector.astype(int)
    vector = vector.clip(0,GRID)

    X, Y, Z = vector.T
    return X,Y,Z


# Generating Space Mesh

x = np.linspace(-HALF_GRID,HALF_GRID,GRID)
y = np.linspace(-HALF_GRID,HALF_GRID,GRID)
z = np.linspace(-HALF_GRID,HALF_GRID,GRID)

# Creating Voxel mesh
X,Y,Z = np.meshgrid(x,y,z,indexing='ij')
condition =((R-np.sqrt((X)**2+Y**2))**2 + Z**2) <= r**2
X, Y, Z = np.where(condition)
TORUS = np.array([X,Y,Z])

rotate = 0
while True:
    # Rotate X,Y,Z 
    t1 = time.time()
    rotate += 5
    X,Y,Z = Rotate(TORUS[0],TORUS[1],TORUS[2], ROTATION_AXIS[0],ROTATION_AXIS[1],ROTATION_AXIS[2], np.deg2rad(rotate))

    # Generating Normals Pass
    Q = np.sqrt(X**2 + Y**2) + 1e-8
    nX = 2*X*(1-R/Q) 
    nY = 2*Y*(1-R/Q)
    nZ = 2*Z

    normal = np.stack([nX, nY,nZ], axis = -1)
    norm = np.linalg.norm(normal)
    normal = normal/norm


    # Calculating lights
    light = np.array(LIGHT)
    light = light / np.linalg.norm(light)


    brightness = np.einsum("ij,j->i",normal, light)
    brightness = np.clip(brightness, 0,1)
    brightness = np.interp(brightness,[brightness.min(), brightness.max()], [0.2,1])

    # Creating Buffers
    screen = np.zeros((GRID,GRID))
    zbuffer = np.full((GRID, GRID), np.inf)

    z_max,z_min = Z.max(), Z.min()
    Z = -np.interp(Z, (z_min, z_max), (0,1))

    # Resterizing Donuts
    l = 0
    for i,j,k in zip(X,Y,Z):
        if k<zbuffer[i][j]:
            zbuffer[i][j] = k
            screen[i][j] = (brightness[l]*LIGHTING-(k*( 1- LIGHTING)))*(len(FILLER)-1)
        l+=1


    # Converting to AASCII
    string = ""
    for i in range(GRID):
        for j in range(GRID):
            val = abs(screen[i][j])
            string +=str( FILLER[int(val)])*2
        string += "\n"

    string = string.removesuffix('\n')


    print('\033[H\033[36m', end='')
    print(string,flush=True, end='')


    t2 = time.time()
    if 1/25 + t1-t2 > 0:
        time.sleep(1/25 + t1-t2)
