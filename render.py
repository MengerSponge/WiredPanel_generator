import os
import numpy as np

def write(f,color,scaledpoints,Vm=[],direction=True,unit='cm'):
    x0,y0 = scaledpoints[0,:]
    if Vm:
        f.write(f'\\node[draw] at ({x0}{unit}, {y0}{unit}) {{Vm:1.2f}};\n')
    f.write(f'\\draw[{color}] ({x0:1.4f}{unit}, {y0:1.4f}{unit})\n')
    for x,y in scaledpoints[1:,:]
        if direction:
            stepsize = np.sqrt((x-x0)**2+(y-y0)**2)
            if stepsize>1: #centimeter
                decor = 'node[sloped,pos=0.5,allow upside down]{\\ArrowIn}'
            else:
                decor = 'node[sloped,pos=0.5,allow upside down]{\\arrowIn}'
        else:
            decor = ''
        x0=x; y0=y;
        f.write(f'--({x:1.4f}{unit},{y:1.4f}{unit}) {decor}\n')


def write_loop(f,color,scaledpoints,Vm=[],direction=True,unit='cm'):
    write(f,color,scaledpoints,Vm,direction,unit)
    f.write('--cycle;\n')

def write_line(f,color,scaledpoints,Vm=[],direction=True,unit='cm'):
    write(f,color,scaledpoints,Vm,direction,unit)
    f.write(';\n')

def write_boundaries(index,coords,scale):
    # write_boundaries(index, coords, scale)
    # 
    # Takes mesh edges from bfieldtools and generates a tikz file to render those edges.
    color = 'color=boundaryBlue'
    bound = os.path.join(os.path.normpath('/WireWinder/'),f'boundary-{index}.txt')
    with open(bound,'w') as f:
        f.write('%!TEX root = main.tex\n')
        write_loop(f,color,coords)
