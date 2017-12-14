#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
 
int main( int argc, char *argv[], char **environ )
{
    char buf[12] = { 0, };
    char cmd[2048] = { 0, };
    unsigned int i = 0;    
 
    char **e;
    size_t len;
 
    printf( "input path :" );
    fgets( buf, 10, stdin );
 
    for( i = 0; i <= 11; i++ ) {
        if( buf[i] == '\'' ) exit(0);
        if( buf[i] == '&' ) exit(0);
        if( buf[i] == ';' ) exit(0);
        if( buf[i] == '|' ) exit(0);
        if( buf[i] == '\"' ) exit(0);
        if( buf[i] == ' ' ) exit(0);
    }
 
    
    sprintf( cmd, "/bin/ls -al /dev/%s", buf );
 
    for( e = environ; *e; ++e ) {
        len = strlen( *e );
        memset( *e, 0x00, len );
    }
 
    setregid( 1003, 1003 );
    system( cmd );
 
    return 0;
}
