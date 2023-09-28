@echo off

setlocal
SET DBCFG=..\hw07\.config\database.cfg
echo CONFIG FILE: %DBCFG%
FOR /F "tokens=1,3 eol=#" %%i IN ( %DBCFG% ) DO  SET "%%~i=%%~j" 
echo docker run --name postgres -p %port%:%port% -e POSTGRES_PASSWORD=%password% -d %username%
docker stop  postgres
docker rm  postgres
docker run --name postgres -p %port%:%port% -e POSTGRES_PASSWORD=%password% -d %username%
endlocal


                    

