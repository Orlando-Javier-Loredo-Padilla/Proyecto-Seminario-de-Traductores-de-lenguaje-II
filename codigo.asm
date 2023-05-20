.386
.model flat, stdcall
option casemap:none

include c:\masm32\include\masm32rt.inc

.code

suma proc a:DWORD,b:DWORD
mov eax, a
add eax, c
ret
suma endp

main proc
local resultado:DWORD
mov eax, 13
push eax
mov eax, 16
push eax
call suma
mov resultado, eax
mov eax, resultado
print str$(eax)
invoke ExitProcess, 0

main endp
end main