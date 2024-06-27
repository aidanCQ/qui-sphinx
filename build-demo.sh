rm -rf ./demo/build/html
./build-ui.sh
cd ./demo && poetry run make html
cd ../
