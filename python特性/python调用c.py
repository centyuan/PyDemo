"""
1.编写c
2.编译成.so
3.python使用ctypes 导入.so
from ctypes import cdll
dll = cdll.LoadLibrary('./demo.so')

#include <stdio.h>
int foo(){
    int i,k,m;
    for(i=0;i<1000;i++){
        for(k=0;k<1000;k++){
            for(m=0;m<1000;m++){}
        }
    }
}
"""
from ctypes import cdll
dll = cdll.LoadLibrary('./demo.so')
dll.foo()
