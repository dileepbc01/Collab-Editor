declare global {
  namespace NodeJS {
    interface ProcessEnv {
      PORT: string;
      NODE_ENV: "development" | "production" | "test";
      HOST: string;
      CORS_ORIGIN: string;
      // Add other environment variables you need here
    }
  }
}

export {};
