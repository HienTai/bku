uses crt;
var fi,fo: text;
     a: integer;
begin
    clrscr;
    assign(fi, 'lol.inp');reset(fi);
    assign(fo, 'lol.out');rewrite(fo);
    readln(fi,a);
    writeln(fo,'10*A=',A*10);
    close(fo);
    close(fi);
    readln;
end.