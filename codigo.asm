.Model
.Stack
.Code

suma proc a:DWORD,b:DWORD
mov ax, a
add ax, c
ret
suma endp

main proc
local resultado:DWORD
mov ax, 13
push ax
mov ax, 16
push ax
call suma
mov resultado, ax
mov ax, resultado

main endp
end main