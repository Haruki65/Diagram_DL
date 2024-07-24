import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    
    # Conv Layer 1
    to_ConvConvRelu(name='conv1', s_filer=96, n_filer=(32,32), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40, caption="Conv1"),

    # Conv Layer 2
    to_ConvConvRelu(name='conv2', s_filer=96, n_filer=(32,32), offset="(1,0,0)", to="(conv1-east)", width=(2,2), height=40, depth=40, caption="Conv2"),
    
    # MaxPool Layer 1
    to_Pool(name="pool1", offset="(1,0,0)", to="(conv2-east)", width=2, height=20, depth=20, opacity=1.0, caption="MaxPool"),
    # to_Dropout(name="dropout1", p=0.2, offset="(0,0,0)", to="(pool1-east)", width=2, height=20, depth=20, opacity=1.0),
    
    # Conv Layer 3
    to_ConvConvRelu(name='conv3', s_filer=48, n_filer=(64,64), offset="(1,0,0)", to="(pool1-east)", width=(4,4), height=20, depth=20, caption="Conv3"),
    
    # Conv Layer 4
    to_ConvConvRelu(name='conv4', s_filer=48, n_filer=(128,128), offset="(1,0,0)", to="(conv3-east)", width=(6,6), height=10, depth=10, caption="Conv4"),
    
    # MaxPool Layer 2
    to_Pool(name="pool2", offset="(1,0,0)", to="(conv4-east)", width=2, height=5, depth=5, opacity=1.0, caption="MaxPool"),
    
    # Conv Layer 5
    to_ConvConvRelu(name='conv5', s_filer=24, n_filer=(256,256), offset="(1,0,0)", to="(pool2-east)", width=(8,8), height=5, depth=5, caption="Conv5"),
    
    # Conv Layer 6
    to_ConvConvRelu(name='conv6', s_filer=24, n_filer=(384,384), offset="(1,0,0)", to="(conv5-east)", width=(10,10), height=3, depth=3, caption="Conv6"),

    # Conv Layer 7
    to_ConvConvRelu(name='conv7', s_filer=24, n_filer=(256,256), offset="(1,0,0)", to="(conv6-east)", width=(8,8), height=5, depth=5, caption="Conv7"),

    # Conv Layer 8
    to_ConvConvRelu(name='conv8', s_filer=24, n_filer=(128,128), offset="(1,0,0)", to="(conv7-east)", width=(6,6), height=10, depth=10, caption="Conv8"),
    
    # MaxPool Layer 3
    to_Pool(name="pool3", offset="(1,0,0)", to="(conv8-east)", width=2, height=5, depth=5, opacity=1.0, caption="MaxPool"),
    
    # Fully Connected Layers
    to_FC(name="fc1", s_filer=1, n_filer=4096, offset="(1,0,0)", to="(pool3-east)", width=10, height=1, depth=1, caption="Fully Connected"),
    to_FC(name="fc2", s_filer=1, n_filer=10, offset="(1.5,0,0)", to="(fc1-east)", width=8, height=1, depth=1, caption="Fully Connected"),
    
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()
