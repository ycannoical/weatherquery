sudo service docker start

sudo docker build -t weathertest:latest . 

sudo docker run -p 5000:5000 -it weathertest
	