FROM airhacks/java
MAINTAINER Jose Manuel Sanchez
ENV VERSION 3.1.0.Final
ENV INSTALL_DIR /opt
ENV WILDFLY_HOME ${INSTALL_DIR}/keycloak-${VERSION}
ENV DEPLOYMENT_DIR ${WILDFLY_HOME}/standalone/deployments/
RUN curl -O  https://downloads.jboss.org/keycloak/${VERSION}/keycloak-${VERSION}.zip \
    && unzip keycloak-${VERSION}.zip -d ${INSTALL_DIR} \
    && rm keycloak-${VERSION}.zip \
    && chmod a+x ${WILDFLY_HOME}/bin/standalone.sh
ENTRYPOINT ${WILDFLY_HOME}/bin/standalone.sh -b=0.0.0.0
EXPOSE 8080 9990

