500 stdcall NDdeShareAddA(str long ptr ptr long)
501 stdcall NDdeShareDelA(str str long)
502 stdcall NDdeShareEnumA(str long ptr long ptr ptr)
503 stdcall NDdeShareGetInfoA(str str long ptr long ptr ptr)
504 stdcall NDdeShareSetInfoA(str str long ptr long long)
505 stdcall NDdeGetErrorStringA(long ptr long)
506 stdcall NDdeIsValidShareNameA(str)
507 stdcall NDdeIsValidAppTopicListA(str)
509 stdcall NDdeGetShareSecurityA(str str long ptr long ptr)
510 stdcall NDdeSetShareSecurityA(ptr ptr long ptr)
511 stdcall NDdeGetTrustedShareA(str str ptr ptr ptr)
512 stdcall NDdeSetTrustedShareA(str str long)
513 stdcall NDdeTrustedShareEnumA(str long ptr long ptr ptr)
600 stdcall NDdeShareAddW(wstr long ptr ptr long)
601 stdcall NDdeShareDelW(wstr wstr long)
602 stdcall NDdeShareEnumW(wstr long ptr long ptr ptr)
603 stdcall NDdeShareGetInfoW(wstr wstr long ptr long ptr ptr)
604 stdcall NDdeShareSetInfoW(wstr wstr long ptr long long)
605 stdcall NDdeGetErrorStringW(long wstr long)
606 stdcall NDdeIsValidShareNameW(wstr)
607 stdcall NDdeIsValidAppTopicListW(wstr)
609 stdcall NDdeGetShareSecurityW(wstr wstr long ptr long ptr)
610 stdcall NDdeSetShareSecurityW(ptr ptr long ptr)
611 stdcall NDdeGetTrustedShareW(wstr wstr ptr ptr ptr)
612 stdcall NDdeSetTrustedShareW(wstr wstr long)
613 stdcall NDdeTrustedShareEnumW(wstr long ptr long ptr ptr)

@ stub NDdeSpecialCommandA
@ stub NDdeSpecialCommandW
