# imagem mais utilizada do java ultimamente
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

#  Execução
FROM eclipse-temurin:17-jdk-jammy
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]


#Imagem que utilizei foi Eclipse Temurim pois imagem mais leve e mais populares no momento para utilizar-la.
