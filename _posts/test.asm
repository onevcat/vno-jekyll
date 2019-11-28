assume cs:codesg

codesg segment
  start:mov ax, 0
				mov bx, 0
        jmp short s
        add ax, 1    ;跳过该指令的执行
				add ax, ax
      s:inc ax
codesg ends

end start
```
