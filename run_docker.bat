@echo off

echo Checking Docker images...
docker images | findstr selenium > nul
if %errorlevel% equ 0 (
    echo selenium-app image already exists.
) else (
    echo Building selenium-app image...
    docker compose build
)

echo Starting Docker containers...
docker compose up -d
docker logs -f python-app
echo.
echo Containers are running.
echo Press any key to stop the containers...
echo.
pause

echo Stopping containers...
docker compose down
echo Process completed.
