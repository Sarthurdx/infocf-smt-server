


FROM tomcat:9-jdk11-temurin-focal

RUN mkdir /usr/local/tomcat/resources/

COPY systemWTest.war /usr/local/tomcat/webapps/

COPY Query.jar /usr/local/tomcat/resources/
COPY RF.jar /usr/local/tomcat/resources/
RUN chmod a+x /usr/local/tomcat/resources/Query.jar
RUN chmod a+x /usr/local/tomcat/resources/RF.jar
CMD ["catalina.sh", "run"]
