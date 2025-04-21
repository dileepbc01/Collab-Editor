# Use official Bun image
FROM oven/bun:1.1.3

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN bun install

# Expose desired port (change as needed)
EXPOSE 3000

# Start the app (replace with your entry point if different)
CMD ["bun", "run", "start"]
