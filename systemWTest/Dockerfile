


FROM tomcat:9-jdk11-temurin-focal

RUN mkdir /usr/local/tomcat/resources/

COPY systemWTest.war /usr/local/tomcat/webapps/

COPY Query.jar /usr/local/tomcat/resources/
COPY RF.jar /usr/local/tomcat/resources/
COPY server.xml /usr/local/tomcat/conf/server.xml
COPY web.xml /usr/local/tomcat/conf/web.xml
RUN chmod a+x /usr/local/tomcat/resources/Query.jar
RUN chmod a+x /usr/local/tomcat/resources/RF.jar
RUN chmod a+r /usr/local/tomcat/conf/server.xml
RUN chmod a+r /usr/local/tomcat/conf/web.xml
EXPOSE 8443
CMD ["catalina.sh", "run"]
