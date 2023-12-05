# Use the official .NET SDK image as the base image
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /app

# Copy the .NET project file and restore any dependencies (only .csproj and nuget.config)
COPY *.csproj ./
COPY nuget.config ./
RUN dotnet restore

# Copy the rest of your application code and build it
COPY . ./
RUN dotnet publish -c Release -o out

# Build the runtime image
FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app
COPY --from=build /app/out ./

# Set the entry point for the container
ENTRYPOINT ["dotnet", "DotNet_PoC.dll"]
