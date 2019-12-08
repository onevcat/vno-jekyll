assume cs:codesg ds:datasg ss:stacksg

datasg segment
	db 'welcome to masm!'
	db 02h, 24h, 71h
datasg ends

stacksg segment
	dw 8 dup(0)
stacksg ends

codesg segment
start: 	mov ax, datasg
				mov ds, ax
				mov ax, stacksg
				mov ss, ax
				mov sp, 10h  ;指向栈顶
				
				xor bx, bx
				mov ax, 07C8h

				mov cs, 3
	 s3:  push cs
				push ax
				push bx

				mov es, ax
				mov si, 0
				mov di, 0

				mov cx, 10h

	 s1:  mov al, ds:[si]
				mov es:[di], al
				
				inc si
				add di, 2

				loop s1
				
				mov di, 1
				pop bx
				mov al, ds:10h[bx]
				inc bx

				mov cx, 10h
	 s2:  mov es:[di], al
				add di, 2
				loop s2

				pop ax
				add ax, 086B
				pop cx

				loop s3

codesg ends
end start







