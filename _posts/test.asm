assume cs:codesg
  codesg segment
    start:mov ax, 0
          mov bx, 0
          jump far ptr s
          db 256 dup(0)
        s:add ax, 1
          inc ax
  codesg ends
end start
