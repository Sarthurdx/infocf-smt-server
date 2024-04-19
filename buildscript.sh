


cd djserver/mysite;
docker build -t backend .;
cd ../../systemWTest;
rm systemWTest.war;
jar -cvf systemWTest.war *;
docker build -t frontend .;

